import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from generator import build_generator
from discriminator import build_discriminator

def load_data(filename):
    return [value for value in np.load(filename)]

def flat_data_or_label(data):
    return [value for row in data for value in row]

def generate_fake_samples(generator, n_samples):
    #GENERATE THE RANDOM NOISE
    noise = np.random.normal(0, 1, (n_samples, 10))
    #GENERATE THE FAKE DATA
    return generator.predict(noise)

def plot_data(real_samples, fake_samples, d_loss_real, d_loss_fake, g_loss):
    #PLOT THE GRAPHS
    plt.figure(figsize=(12, 6))
    plt.hist(real_samples, bins=30, alpha=0.5, label='Real Samples')
    plt.hist(fake_samples, bins=30, alpha=0.5, label='Fake Samples')
    plt.title('REAL & FAKE SAMPLES')
    plt.legend()
    #==============================================================================
    plt.figure(figsize=(12, 6))
    real_data = load_data('./spectrumai/data/x_tst.npy')
    real_label = load_data('./spectrumai/data/d_tst.npy')
    for i in range(len(real_data)):
        if real_label[i]:
            plt.plot(np.arange(0, 59), real_data[i], color = 'red')
        else:
            plt.plot(np.arange(0, 59),  real_data[i], color = 'green')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title('REAL DATASET')
    plt.grid(True)
    #==============================================================================
    plt.figure(figsize=(10, 6))
    plt.plot(d_loss_real, label="Discriminator Loss", color = 'red')
    plt.plot(d_loss_fake, label="Discriminator Loss Fake", color = 'blue')
    plt.plot(g_loss, label="Generator Loss", color = 'green')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title('LOSS DISCRIMINATOR & GENERATOR')
    plt.grid(True)
    #==============================================================================
    plt.show()

def custom_mse_with_weighted_penalty(y_true, y_pred, alpha=0.1):
    mse = tf.reduce_mean(tf.square(y_true - y_pred))

    penalty = tf.reduce_mean(tf.where(y_pred < 0,-y_pred, 0)) + tf.reduce_mean(tf.where(y_pred > 1, y_pred -1, 0))
    return mse + alpha * penalty

def train_gan(generator, discriminator, gan_model, real_data, epochs=1000, batch_size=128, visualize=False, fake_samples=None):
    #HALF OF THE BATCH_SIZE - IN THIS CASE 64
    half_batch = batch_size // 2

    for epoch in range(epochs):
        #TRAIN THE DISCRIMINATOR
        #SELECT A RANDOM HALF BATCH OF REAL DATA
        idx = np.random.randint(0, len(real_data), half_batch)
        real_samples = np.array([real_data[i] for i in idx])

        #GENERATE A HALF BATCH OF FAKE DATA 
        fake_samples = generate_fake_samples(generator, half_batch)

        real_labels = np.ones((half_batch, 1))
        fake_labels = np.zeros((half_batch, 1))

        #TRAIN THE DISCRIMINATOR
        d_loss_real = discriminator.train_on_batch(real_samples, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_samples, fake_labels)

        #TRAIN THE GENERATOR
        noise = np.random.normal(0, 1, (batch_size, 10))
        valid_labels = np.ones((batch_size, 1))
        g_loss = gan_model.train_on_batch(noise, valid_labels)

        print(f'Epoch: {epoch+1}/{epochs}, D Loss Real: {d_loss_real}, D Loss Fake: {d_loss_fake}, G Loss: {g_loss}')

        if epoch % 1000 == 0:
            generator.save(f'generator_model_{epoch}.keras')

    plot_data(real_samples, fake_samples, d_loss_real, d_loss_fake, g_loss)

def create_gan_model(alpha=2.0, descrimiator_lr=0.0001, generator_lr=0.0001, epochs=1000, save_model=False, model_path='./spectrumai/models/gan_model.keras'):    

    discriminator_optimizer = Adam(learning_rate=descrimiator_lr)

    generator_optimizer = Adam(learning_rate=generator_lr)

    discriminator = build_discriminator(discriminator_optimizer)

    generator = build_generator()

    #BUILD COMBINED GAN MODEL
    initial_noise = tf.keras.Input(shape=(10,))
    initial_fake = generator(initial_noise)
    #TRAINABLE FALSE - SO WE CONTROL IT MANUALLY
    discriminator.trainable = False
    predict_validity = discriminator(initial_fake)
    gan_model = tf.keras.Model(initial_noise, predict_validity)

    loss_function = lambda y_true, y_pred: custom_mse_with_weighted_penalty(y_true, y_pred, alpha=alpha)

    gan_model.compile(optimizer=generator_optimizer, loss=loss_function, metrics=['accuracy'])

    real_data = load_data('./spectrumai/data/x_tst.npy')
    real_label = load_data('./spectrumai/data/d_tst.npy')

    #TRAIN THE GAN WITH ALL NECESSARY INFORMATION
    train_gan(generator, discriminator, gan_model, real_label, epochs=epochs, visualize=False)

    if save_model:
        print(f'Saving model {model_path}')
        generator.save(model_path)

create_gan_model(epochs=1000, alpha=2.3, save_model=True, model_path='./spectrumai/models/gan_model_new.keras')