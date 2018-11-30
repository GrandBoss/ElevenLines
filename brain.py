import numpy as np
import learner as L
import copy

class Brain: 
    def __init__(self,  input, ground_truth, layer_range, node_range):        
        self.input = input
        self.ground_truth = ground_truth
        self.layer_range = layer_range
        self.node_range = node_range
        self.top_time_list = []
        self.top_error_list = []
        self.top_time_error_list = []

        self.nodes = []
        self.nodes.append(len(self.input[0])) 
        for target_list in range(min(self.layer_range)-1):
            self.nodes.append(min(self.node_range)) 
        self.nodes.append(1) 
        
    def doLearnAll(self, num_of_times = 100):
        count = 0
        while len(self.nodes)-2 < max(self.layer_range)+1:  
            count += 1
            learner = L.Learner(self.input, self.ground_truth)
            learner.doLearn(self.nodes, num_of_times)
            self.tick(learner)
            self.progress(count, learner)
            self.addLearnerToTopLists(learner)
            self.nodes = self.increaseNodesOrLayers(self.nodes)   

    def tick(self, learner):
            learner = learner
    def progress(self, count):
            count = count

    def addLearnerToTopLists(self, learner):
        self.addLearnerToTopErrorList(learner)
        self.addLearnerToTopTimeList(learner)
        self.addLearnerToTopTimeErrorList(learner)

    def addLearnerToTopErrorList(self, learner):
        i = 0
        inserted = False
        while not inserted and (i < len(self.top_error_list)):
            if self.top_error_list[i].getMeanError() > learner.getMeanError():
                self.top_error_list.insert(i, copy.deepcopy(learner))
                inserted = True
            i += 1
        
        if not inserted:
            self.top_error_list.append(copy.deepcopy(learner))   
            
    def addLearnerToTopTimeList(self, learner):
        i = 0
        inserted = False
        while not inserted and (i < len(self.top_time_list)):
            if self.top_time_list[i].getElapsedTime() > learner.getElapsedTime():
                self.top_time_list.insert(i, copy.deepcopy(learner))
                inserted = True
            i += 1
        
        if not inserted:
            self.top_time_list.append(copy.deepcopy(learner))        
            
    def addLearnerToTopTimeErrorList(self, learner):
        i = 0
        inserted = False
        while not inserted and (i < len(self.top_time_error_list)):
            if self.top_time_error_list[i].getErrorCoefficient() > learner.getErrorCoefficient():
                self.top_time_error_list.insert(i, copy.deepcopy(learner))
                inserted = True
            i += 1
        
        if not inserted:
            self.top_time_error_list.append(copy.deepcopy(learner))             
    
    def increaseNodesOrLayers(self, nodes):    
        increased = False
        layer_num = 1    
        while not increased and (layer_num < len(nodes)-1) :
            if nodes[layer_num] < max(self.node_range)+1:
                nodes[layer_num] += 1 
                increased = True
            else:
                layer_num += 1

        if not increased:
            nodes.insert(1, 1) 
            for i in range(1, len(nodes)-1):
                nodes[i] = min(self.node_range)

        return nodes