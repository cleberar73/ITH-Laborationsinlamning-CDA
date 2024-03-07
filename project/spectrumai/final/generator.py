from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, LeakyReLU

#THIS IS USED TO START THE BUILDER
# def build_generator(input_dim=10):
def build_generator(input_dim=10):
    model = Sequential()

    #INPUT LAYER
    model.add(Dense(32, input_dim=input_dim))

    #HIDDEN LAYER
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(64))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(128))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))

    model.add(Dropout(0.5))

    #OUTPUT LAYER
    model.add(Dense(1, activation='sigmoid'))
    return model

