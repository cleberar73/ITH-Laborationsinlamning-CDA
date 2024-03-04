from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

def build_discriminator(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]):
    model = Sequential()

    #INPUT LAYER
    model.add(Dense(128,activation="relu", input_shape=(1,)))

    #HIDDEN LAYER - Next layer, we want to bake to 1 (one) when output
    #ACTIVATE(when numbers are positive) and deactivate(opposite): Negative become zeros and Positive no change
    #So we get 0's and 1's 
    model.add(Dense(64,activation="relu"))
    model.add(Dense(32,activation="relu"))

    #OUTPUT LAYER - Suitable for True/False, Random number
    #Hard to climb the mountain w/ a rounded stone and then let it go down or manage go up/down by itself
    model.add(Dense(1,activation="sigmoid"))

    #COMPILE THE MODEL
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    return model