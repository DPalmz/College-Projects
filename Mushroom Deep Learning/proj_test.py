import numpy as np
from config import NUM_TRAINING_ITERATIONS, CONVERGENCE_THRESHOLD, LEARNING_RATE
from formulas import err
import models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from random import random

f = None
curr_point = 0
target = []
attrs = []
total_runs = 0
data = None
num_incorrect = 0
prev_sample_err = 0
curr_sample_err = 0

#Preprocessing
##########################################
mushroomRows = ['edible or poisonous', 'cap shape', 'cap surface', ' cap color', 'bruises', 'odor',
                    'gill attachment', 'gill spacing', 'gill size', 'gill color', 'stalk shape', 'stalk root',
                    'stalk surface above the ring', 'stalk surface below the ring', 'stalk color below the ring',
                    'stalk color above the ring', 'veil type', 'veil color',
                    'ring number', 'ring type', 'spore print color', 'population',
                    'habitat']  # names of categories for mushrooms

database = pd.read_csv("agaricus-lepiota.data", names=mushroomRows)  # reading in data

database.rename_axis('edible poisonous').reset_index()  # to take first column off of index
encodedData = pd.get_dummies(database, dummy_na='true')

train, mem = train_test_split(encodedData, train_size=0.8) # for 80% training data
validation, test = train_test_split(mem, test_size=0.5) # for 10% validation and test
train.to_csv('training.csv')
validation.to_csv('val.csv')
test.to_csv('testing.csv')
def parse_data(fname):
    # reset all the data
    global curr_point
    global total_runs
    global target
    global attrs
    global num_incorrect
    global prev_sample_err
    global curr_sample_err
    global data
    global f
    global currOutputE
    global currOutputP

    curr_point = 0
    total_runs = 0
    target = []
    attrs = []
    num_incorrect = 0
    prev_sample_err = 0
    curr_sample_err = 0
    currOutputE = 0
    currOutputP = 0


    # set the proper data file
    data_file = 'err.txt'
    if fname == 'training.csv':
        data_file = 'training_err.txt'
    elif fname == 'val.csv':
        data_file = 'val_err.txt'
    elif fname == 'testing.csv':
        data_file = 'testing_err.txt'


    # clear the file
    open(data_file, 'w+').close()

    # open the data file for logging
    #data = cfile(data_file, 'w')
    data = open(data_file, 'w') #cfile broke

    #f = open(, 'r').readlines()

    currData = pd.read_csv(fname)
    target = currData[['edible or poisonous_e', 'edible or poisonous_p']].copy()
    currData = currData.rename(columns={'Unnamed: 0': 'Useless'}, )
    #currData.columns.values[0] = 'Useless'
    attrs = currData.drop(['Useless', 'edible or poisonous_e', 'edible or poisonous_p',
                             'edible or poisonous_nan'], axis=1)
    print(currData)
    print("target: ")
    print(target)
    print('attributes: ')
    print(attrs)



    #for row in encodedData:    Replaced with pandas
     #   row = [x.strip() for x in row.split(',')]
      #  row = [int(num) for num in row]
       # target.append(int(row[1])) #row[0] represent p class, row[1] represent e class.
                                   #if you represent e and p classes into one elment (0 for p and 1 for e, etc.), please modifiy.
        #attrs.append(row[2:])


if __name__ == '__main__':
    print( "Parsing the training dataset...")
    # parse the training dataset and store its information into globals
    parse_data('training.csv')




    # set up the layers to be used    
    x = models.Layer(6, attrs.iloc[curr_point, 0:], 1) #[curr_point] still causing problems
    y = models.Layer(3, x.layer_out, 2)
    n_outputs = len(set([row[-1] for row in attrs]))
    x.layer_out = [[random() for i in range(1 + 1)] for i in range(n_outputs)]  # first 1 is from 1 hidden layer
    y.layer_out = [[random() for i in range(1 + 1)] for i in range(n_outputs)]

    print ("Beginning training the neural network:")
    # iterate through to train the neural network
    while total_runs < NUM_TRAINING_ITERATIONS:        

        # set up the first layer and evaluate it




        #raise Exception('Implement this part.')
        x.forward_propagate(curr_point)
        # set up the second layer and evaluate it

        y.forward_propagate(curr_point)
        #raise Exception('Implement this part.')

        # backpropogate
        y.backprop(target.iloc[curr_point, 0:])
        y.update_weights(target.iloc[curr_point, 0:])
        x.backprop(target.iloc[curr_point, 0:]) #[curr_point] if time
        x.update_weights(target.iloc[curr_point, 0:])

        # get the current error
        #raise Exception('Implement this part.')
        curr_err = err(y.layer_out, target.iloc[curr_point, 0:]) #call err function to calculate

        # round up and down to check err


        currOutputE, currOutputP = np.prod(y.layer_out, axis=1) #fucked up second layer

        currOutputE = currOutputE / len(y.layer_out) #mean
        currOutputP = currOutputP / len(y.layer_out)
        if currOutputE >= 0.5:
            temp = 1
        else:
            temp = 0

        # increment the number incorrect if its wrong
        if(temp != target[curr_point]):
            num_incorrect += 1

        # check to see if we have converged
        if total_runs % 100 == 0:
            prev_sample_err = curr_sample_err
            curr_sample_err = curr_err
            if abs(prev_sample_err - curr_sample_err) < CONVERGENCE_THRESHOLD:
                print ("Data has converged at the " + str(total_runs) + "th run.")
                break;

        # print information about the current iteration
        print ("Current iteration: " + str(total_runs))
        print ("Current error: " + str(curr_err) + "\n")
        data.w(curr_err)

        # iterate
        total_runs += 1
        curr_point += 1

        if curr_point >= len(f):
            curr_point = 0

    # close the file
    data.close()



    print ("Neural network is done training! Hit enter to validation processing.")
    print ("Error percentage on training set: " + str(float(num_incorrect)/NUM_TRAINING_ITERATIONS))
    raw_input()


    print ("Parsing the validation dataset...")
    # parse the validation dataset and store its information into globals
    parse_data('val.csv')

    

    print ("Begining validating the neural network:")
    # iterate through to train the neural network
    while total_runs < len(f):        

        # set up the first layer and evaluate it
        x.forward_propagate(curr_point)
        #raise Exception('Implement this part.')

        # set up the second layer and evaluate it
        y.forward_propagate(curr_point)
        #raise Exception('Implement this part.')

        # get the current error
        curr_err = err
        #raise Exception('Implement this part.')

        # round up and down to check err
        if y.layer_out[0] >= 0.5:
            temp = 1
        else:
            temp = 0

        # increment the number incorrect if its wrong
        if(temp != target[curr_point]):
            num_incorrect += 1

        # check to see if we have converged
        if total_runs % 100 == 0:
            prev_sample_err = curr_sample_err
            curr_sample_err = curr_err
            if abs(prev_sample_err - curr_sample_err) < CONVERGENCE_THRESHOLD:
                print ("Data has converged at the " + str(total_runs) + "th run.")
                break;

        # print information about the current iteration
        print ("Current iteration: " + str(total_runs))
        print ("Current error: " + str(curr_err) + "\n")
        data.w(curr_err)

        # iterate
        total_runs += 1
        curr_point += 1

        if curr_point >= len(f):
            curr_point = 0

    # close the file
    data.close()



    print ("Neural network is done validating! Hit enter to test it.")
    print ("Error percentage on validation set: " + str(float(num_incorrect)/NUM_TRAINING_ITERATIONS))
    raw_input()

    print ("Begin testing the neural network:")
    # parse the testing data and store its information into globals
    parse_data('testing.csv')

    # iterate through to test the neural network
    while curr_point < len(f):
        
        # set up the first layer and evaluate it
        x.forward_propagate(curr_point)
        raise Exception('Implement this part.')

        # set up the second layer and evaluate it
        y.forward_propagate(curr_point)
        raise Exception('Implement this part.')

        # get the current error
        raise Exception('Implement this part.')

        # round up and down to check err
        if y.layer_out[0] >= 0.5:
            temp = 1
        else:
            temp = 0

        # increment the number incorrect if its wrong
        if(temp != target[curr_point]):
            num_incorrect += 1


        # print information about the current iteration
        print ("Current iteration: " + str(total_runs))
        print ("Current Error: " + str(curr_err) + "\n")
        data.w(curr_err)

        # iterate
        total_runs += 1
        curr_point += 1

    data.close()
    print ("Testing done! Check out the generated output files ('testing_err.txt' and 'training_err.txt')")
    print ("Error percentage on testing set: " + str(float(num_incorrect)/len(f)))
