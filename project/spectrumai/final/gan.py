#GAN - Generative Adversarial Networks
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    return [value for value in np.load(filename)]

def flat_data_or_label(data):
    return [value for row in data for value in row]

#LOADING THE DATA 
real_data = load_data("./spectrumai/data/x_tst.npy") #[value for value in np.load("./spectrumai/data/x_tst.npy")]
real_label = load_data("./spectrumai/data/d_tst.npy") #[value for value in np.load("./spectrumai/data/d_tst.npy")]

max_real_data = max(max(row) for row in real_data)
min_real_data = min(min(row) for row in real_data)

#HERE I AM FLATTING THE ENTIRE ARRAY
flattened_real_data = flat_data_or_label(real_data) #[value for row in real_data for value in row]
flattened_real_label = flat_data_or_label(real_label) #[value for row in real_label for value in row]
#HERE ARE TWO WAYS TO GET THE SUM OF THE ENTIRE ARRAY
sum_real_data = sum(flattened_real_data)
sum_real_data = sum(sum(row) for row in real_data)

#HERE ARE TWO WAYS NOW TO GET THE MEAN
mean_real_data = sum_real_data/len(flattened_real_data)
# mean_real_data = sum(flattened_real_data)/len(flattened_real_data)

#GET TO KNOW YOUR REAL DATA
print(f"="*80)
print(f"First element from the array: ", (real_data[:1]))
# print(f"="*80)
# POP 0 WOULD BE EQUIVALENT TO THE PREVIOUS ELEMENT FROM THE LINE ABOVE   
# print(f"One element from array: ", real_data.pop(1)) 
print(f"="*80)
print(f"Size of the real_data array: ", len(real_data))
print(f"Size flattened array for real_data: ", len(flattened_real_data))
print(f"Size flattened array for real_label: ", len(flattened_real_label))
print(f"Size each array subset real data: ", len(real_data[0]))
print(f"="*80)
print(f"Max for the entire real_data: ", max_real_data)
print(f"Min for the entire real_data: ", min_real_data)
print(f"Sum for the entire real_data: ", sum_real_data)
print(f"Mean for the entire real_data: ", mean_real_data)
print(f"="*80)
