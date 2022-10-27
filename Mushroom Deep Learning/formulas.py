import math

import numpy
import numpy as np


def sig(x):
    # use logistic function as activation function

    return 1.0 / (1.0 + numpy.exp(-x))  # sigmoid function


def inv_sig(x):
    # derivative of the output of neuron with respect to its input

    return x * (1.0 - x)  # derivative of sigmoid


def err(o, t):
    # squared error function, o is the actual output value and t is the target output
    temp = o
    for i in range(len(o)):
        temp[i, 0] = t[0]
        temp[i, 1] = t[1]

    return np.square(np.subtract(o, temp)).mean()  # using numpy in case of subtracting arrays for error


def inv_err(o, t):
    # derivative of squared error function with respect to o
    return 0.25 * (np.subtract(o, t).mean()) ** (-1 / 2)  # it's been so long since I needed to do a derivative
                                                        # in case of error, try changing from np.subtract?


# Calculate neuron activation for an input

def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation
