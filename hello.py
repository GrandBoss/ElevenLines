import numpy as np
import brain as B

CONST_LEARNING_CYCLE_COUNT = 6000

CONST_NODE_COUNT = range(3,8)
CONST_LAYER_COUNT = range(1,4)


input = np.array([
				 [0,0,1,1,0,0,1,1],
				 [0,0,1,1,0,0,1,1],
                 [1,0,0,1,1,0,0,1],
                 [0,0.5,1.5,0,0,0.5,1.5,0],
                 [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],
                 [0,1,0,1,0,1,0,1],
                 [1,1,0,0,1,1,0,0],
                 [1,0.5,1,-1,1,0.5,1,-1],
                 [1,1,0,1,1,1,0,1],
                 [1,0,1,1,1,0,1,1],
                 [0,0,0,1.5,0,0,0,1.5],
                 [0.5,0,0.5,0,0.5,0,0.5,0],
                 [1,1,1,1,1,1,1,1],
                 [1,1,1,0,1,1,1,0]]
                 )

ground_truth = np.array([[0,1,1,1,1,1,1,1, 0,0,0,0,0,0]]).T 
#ground_truth = np.array([[1,0,1,0,0,1,1, 0,1,0,1,0,1]]).T 
#ground_truth = np.array([[1,0,1,0,1,0,1, 0,1,0,1,0,1]]).T 

"""
input = np.array([[0,0,1],
			[0,1,1],
			[1,0,1],
			[1,1,1]])
 
ground_truth = np.array([[0],
			[1],
			[1],
			[0]])"""

def printTopList(top_list):
    pos = 1
    print("")
    print("#####______________TOP_________________#####")
    for entry in top_list:   
        if(pos <= 5):
            print("Position "+str(pos)+".:")  
            tick(entry, (pos == 1))
        if(pos == len(top_list)-5):
            print("")
            print("#####______________LAST_________________#####")
        if(pos >= len(top_list)-2):
            print("Position "+str(pos)+".:")  
            tick(entry, (pos == 1))
        pos += 1

def tick(learner, detailed = False):
    print("  Nodes: "+str(learner.nodes))
    if detailed:
        print("  Output: "+str(np.around(learner.layer[len(learner.layer)-1].T, decimals = 0)))
        print("  Full Output: "+str(learner.layer[len(learner.layer)-1].T))
        print("  Error: "+str(learner.getMeanError()))
    else:
        print("  Output: "+str(np.around(learner.layer[len(learner.layer)-1].T, decimals = 0)))
        print("  Error: "+str(np.around(learner.getMeanError(), decimals = 6)))
    print("  Time: ", learner.elapsed_time)
    print("  Error*Time : ", learner.getErrorCoefficient())
    print("----------------------------")

def getMaxProgress():
    layer_count = (max(CONST_LAYER_COUNT)+1-min(CONST_LAYER_COUNT))+1
    node_count = (max(CONST_NODE_COUNT)+1-min(CONST_NODE_COUNT))
    i = 1
    step = 1
    summa = 0
    while i <= layer_count:
        summa += step
        step += node_count
        i+=1
    return summa    

def tick2(count, learner):
    i = 0
    sum = getMaxProgress()
    while i < sum:
        if i<count:            
            print('.', end='', flush=True)
        else:
            print('_', end='', flush=True)    
        i+=1
    print("("+str(count)+"/"+str(sum)+")["+str(learner.nodes)+"]", end='', flush=True)
    print("")
            
np.random.seed(2)      

brain = B.Brain(input, ground_truth, CONST_LAYER_COUNT, CONST_NODE_COUNT)
brain.progress = tick2
brain.doLearnAll(CONST_LEARNING_CYCLE_COUNT)


print("")
print("ERROR LIST #___________________________________________________________________######################")
printTopList(brain.top_error_list)
print("")
print("TIME LIST #____________________________________________________________________######################")
printTopList(brain.top_time_list)
print("")
print("TIME ERROR LIST #______________________________________________________________######################")
printTopList(brain.top_time_error_list)

"""
print("Most Precise: #___________________________________________________________________" )
tick(brain.top_error_list[0], True)
print("Fastest: #___________________________________________________________________")
tick(brain.top_time_list[0], True)
print("Overall best: #___________________________________________________________________")
tick(brain.top_time_error_list[0], True)
"""
