import numpy as np
import time

class Learner:
    def __init__(self, input, ground_truth):
        self.input = input
        self.ground_truth = ground_truth

    def sig(self, x):
        return 1/(1+np.exp(-x))
        
    def deriv(self, x):
        return x*(1-x)

    def doLearn(self, nodes, num_of_times):     
        start_time = time.time()

        self.nodes = nodes   
        syn = self.setupSynapses(self.nodes)
        for j in range(num_of_times):
            layer = []
            layer_error = []
            layer_delta = []
            layer.append(self.input)
            for i in range(1, len(self.nodes)):
                layer.append(self.sig(np.dot(layer[i-1], syn[i-1])))

            layer_error.insert(0, self.ground_truth - layer[len(layer)-1])
            layer_delta.insert(0, layer_error[0] * self.deriv(layer[len(layer)-1]))

            for i in range(len(syn)-1, 0, -1):
                tmp_error = np.dot(layer_delta[0], syn[i].T) 
                tmp_delta = tmp_error * self.deriv(layer[i])
                layer_error.insert(0, tmp_error)
                layer_delta.insert(0, tmp_delta)

            current_mean_error = np.mean(np.abs(layer_error[len(layer_error)-1]))
            
            for i in range(len(syn)-1, -1, -1):
                syn[i] += np.dot(layer[i].T, layer_delta[i])

        self.synapses = syn
        self.layer_error = layer_error
        self.layer_delta = layer_delta
        self.layer = layer
        self.elapsed_time = time.time() - start_time
    
    def getMeanError(self):
        return np.sum(np.abs(self.layer_error[len(self.layer_error)-1]))
        #return np.mean(np.abs(self.layer_error[len(self.layer_error)-1]))

    def getErrorCoefficient(self):
        return (self.sig(self.getMeanError())**2) * (self.elapsed_time + 1)

    def getElapsedTime(self):
        return self.elapsed_time
        
    def setupSynapses(self, nodes):  
        syn = []  
        for i in range(len(nodes)-1):
            syn.append( 2 * np.random.random((nodes[i], nodes[i+1])) - 1 )   
        
        return syn