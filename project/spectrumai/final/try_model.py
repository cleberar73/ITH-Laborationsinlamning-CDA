import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.models import load_model

def load_data(filename):
    return [value for value in np.load(filename)]

def flat_data_or_label(data):
    return [value for row in data for value in row]

#ADJUST THE FUNCTION PARAMETERS n_samples ACCORDING TO THE EPOCHS E.G 10, 100, 1000 ETC
def generate_samples_using_trained_model(model, n_samples=2000):
    noise = np.random.normal(0, 1, size=(n_samples, 10))
    return model.predict(noise)

def plot_real_data(sorted_data,real_data, real_label,y_values):
    #PLOT THE GRAPHS
    plt.figure(figsize=(12, 6))
    plt.hist(sorted_data, bins=30, alpha=0.5, label='SORTED DATA')
    plt.hist(y_values, bins=30, alpha=0.5, label='Y Values')
    plt.legend(loc="upper right")
    plt.title("SORTED DATA & Y VALUES")
    plt.show()

#LOAD THE GAN MODEL AFTER SAVED
trained_generator = load_model('./spectrumai/models/gan_model_new.keras')

#THIS IS THE PREDICT FROM THE GAN_TRAINED_MODEL 
#ADJUST THE FUNCTION PARAMETERS n_samples ACCORDING TO THE EPOCHS E.G 10, 100, 1000 ETC
generated_samples = generate_samples_using_trained_model(trained_generator, n_samples=2000)

real_data = load_data('./spectrumai/data/x_tst.npy')
real_label = load_data('./spectrumai/data/d_tst.npy')

flattened_real_data = flat_data_or_label(real_data)
flattened_real_label = flat_data_or_label(real_label)

print('='*80)
print(f'Generated Mean: {generated_samples.mean()}')
print(f'Generated Min: {generated_samples.min()}')
print(f'Generated Max: {generated_samples.max()}')
print('-'*80)
print(f'Real Mean: {sum(flattened_real_data)/len(flattened_real_data)}')
print(f'Real Min: {min(flattened_real_data)}')
print(f'Real Max: {max(flattened_real_data)}')
print('='*80)
#SAME LENGTH
print(f'Real data LEN: {len(real_data)}')
print(f'Real label LEN: {len(real_label)}')
print('='*80)
#AFTER FLATTING NOT THE SAME LENGTH
print(f'Flattened Real data LEN: {len(flattened_real_data)}')
print(f'Flattened Real label LEN: {len(flattened_real_label)}')
print('='*80)

#SORT THE DATA
sorted_data = np.sort(generated_samples)

#CREATE AN ARRAY OF Y VALUES RANGING FROM 0 TO 1
y_values = np.arange(1, len(sorted_data) +1) / len(sorted_data)

#PLOT THE GRAPH
plot_real_data(sorted_data, real_data,real_label, y_values)
