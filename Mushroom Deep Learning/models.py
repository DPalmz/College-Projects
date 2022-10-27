import numpy as np
import random
import traceback

from config import LEARNING_RATE
from formulas import sig, inv_sig, inv_err

curr_node_id = 0


class Layer:
    def __init__(self, num_nodes, input_vals, layer_num):
        self.num_nodes = num_nodes
        self.input_vals = np.array(input_vals)
        self.layer_num = layer_num
        self.weight = [[random.random() for col in range(len(input_vals))] for row in range(num_nodes)]
        self.weight_delta = [[0 for col in range(len(input_vals))] for row in range(num_nodes)]
        self.layer_net = [0 for col in range(num_nodes)]
        self.layer_out = [0 for col in range(num_nodes)]
        self.bias = (random.random() * 2) - 1

    def forward_propagate(self, row):
        # evaluation part
        # Get input, compute the output of layer nodes.
            inputs = row
        #for layer in self.layer_net:
            new_inputs = []  # make sure all
            for j in range(self.num_nodes):
                for i in range(len(self.weight) - 1):
                    try:
                        activation = np.array(self.weight[-1])
                        activation += np.array(self.weight[i]) * self.input_vals[i]
                        self.layer_out += sig(activation[i])
                    except:
                        traceback.print_exc()
                #print(activation)


    def activate(self, inputs):


        return activation

        # raise Exception('Implement this part.')



    def backprop(self, other):
        # use backpropagation method to update weights
        for i in reversed(range(len(self.layer_out))):
            layer = self.layer_out[i]
            errors = np.empty([self.num_nodes, len(self.input_vals)])
            if i != len(self.layer_out) - 1:
                for j in range(len(layer)):
                    try:
                        error = 0.0
                        for neuron in self.layer_out[i + 1]:
                            error += (np.array(self.weight[j]) * self.weight_delta[j])
                        errors[j] = error
                    except:
                        traceback.print_exc()
            else:
                for j in range(len(layer)):
                    neuron = layer[j]

                       # errors[j] = (self.layer_out - other[j])  # other is the expected values
                        #wasn't working, didn't have time

            for j in range(len(layer)):
               try:
                    neuron = layer[j]
                    temp = errors
                    for ii in range(len(errors)):
                        temp[ii, 0] = self.layer_out[0]
                        temp[ii, 1] = self.layer_out[1]

                    self.weight_delta = errors[j] * inv_sig(temp)
               except:
                   traceback.print_exc()
        #raise Exception('Implement this part.')

    def update_weights(self, target):
        for i in range(len(self.layer_out)):
            inputs = target[:-1]
            if i != 0:
                inputs = self.layer_out[i - 1]
            for w in range(int(self.layer_out[i, 1])):
                for j in range(len(inputs)):
                    try:
                        self.layer_out[j] -= LEARNING_RATE * np.prod(self.weight_delta, axis=1) * inputs[j]
                    except:
                        traceback.print_exc()
                self.weight[-1] -= LEARNING_RATE * self.weight_delta

    def train_network(self, train, l_rate, n_epoch, n_outputs):

        for row in train:
            output = self.forward_propagate(self.layer_out)
            self.layer_out = output
            #expected = [0 for i in range(n_outputs)]
            #expected[row[-1]] = 1
            #backward_propagate_error(self.layer_out, expected)
            self.update_weights(self.layer_out, row, l_rate)


#class cfile(file):
 #   def __init__(self, name, mode='r'):
  #      self = file.__init__(self, name, mode)

   # def w(self, string):
    #    self.writelines(str(string) + '\n')
     #   return None
