"""
This function is called to load the data for the firsr exercise Deep Squat when CNN_GMM_Between_M1 is running

"""

import csv
import numpy as np

# time steps
timesteps = 240
# repetition number
nr = 90

def load_data():
    f = open('/root/autodl-tmp/data/Data_Correct_m02.csv')
    csv_f = csv.reader(f)
    Correct_X = list(csv_f)

    # Convert the input sequences into numpy arrays
    train_input1 = np.asarray(Correct_X, dtype = float)
    n_dim = 117
    correct_input = np.zeros((nr,timesteps,n_dim))
    for i in range(len(train_input1)//n_dim):
           correct_input[i,:,:] = np.transpose(train_input1[n_dim*i:n_dim*(i+1),:])
    
    f = open('/root/autodl-tmp/data/Labels_Correct_m02.csv')
    csv_f = csv.reader(f)
    Correct_Y = list(csv_f)
    
    # Convert the input labels into numpy arrays
    correct_label = np.asarray(Correct_Y, dtype = float)
    
    f = open('/root/autodl-tmp/data/Data_Incorrect_m02.csv')
    csv_f = csv.reader(f)
    Incorrect_X = list(csv_f)

    # Convert the input sequences into numpy arrays
    test_input1 = np.asarray(Incorrect_X)
    n_dim = 117
    incorrect_input = np.zeros((nr,timesteps,n_dim))
    for i in range(len(test_input1)//n_dim):
          incorrect_input[i,:,:] = np.transpose(test_input1[n_dim*i:n_dim*(i+1),:])
            
    f = open('/root/autodl-tmp/data/Labels_Incorrect_m02.csv')
    csv_f = csv.reader(f)
    Incorrect_Y = list(csv_f)
    
    # Convert the input labels into numpy arrays
    incorrect_label = np.asarray(Incorrect_Y, dtype = float)
    
    return correct_input, correct_label, incorrect_input, incorrect_label

# correct_input, correct_label, incorrect_input, incorrect_label = load_data()
# print(correct_input.shape)   #(90, 240, 117)
# print(correct_label.shape)   #(90, 1)
# print(incorrect_input.shape)  # (90, 240, 117)
# print(incorrect_label.shape)