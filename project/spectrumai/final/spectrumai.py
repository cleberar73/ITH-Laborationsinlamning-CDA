# import tensorflow
import numpy as np
# import pandas as pd
# from tensorflow import keras
# import matplotlib.pyplot as plt
# from keras.optimizers import Adam
# from keras.models import Sequential
# from keras.metrics import categorical_crossentropy
# from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPool2D, Activation

try:
    #LOAD THE DATA FROM THE .npy FILE
    spectrumai_data = np.load("./spectrumai/data/x_tst.npy", mmap_mode='r', allow_pickle=True, encoding='ASCII')
    print(f"\nData loaded successfully!")
except FileNotFoundError:
    print(f"\nFile not found: {spectrumai_data}")

try:
    #LOAD THE DATA LABELS FROM THE .npy FILE
    spectrumai_labels = np.load("./spectrumai/data/d_tst.npy", mmap_mode='r', allow_pickle=True, encoding='ASCII')
    print(f"\nData labels loaded successfully!")
except FileNotFoundError:
    print(f"\nFile not found: {spectrumai_labels}")

print(f"Data : ", spectrumai_data[:][:])
print(f"Label : ", spectrumai_labels[:])
print(f"\nLenght: ", len(spectrumai_labels))