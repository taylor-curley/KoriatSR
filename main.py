# -*- coding: utf-8 -*-
"""
Koriat and Goldsmith's Strategic Regulation framework
From "Monitoring and Control Processes in the Strategic Regulation
of Memory Accuracy"
@author: tmc27
"""

import numpy as np

"""
Simulation 1
"""
Iterations = 100
numItems = 100
Prc = np.arange(0,1.1,.1)
S = 1

QResults = np.zeros(((Iterations)+1, len(Prc)+1))
QResults[0,1:] = Prc
QResults[1:,0] = np.arange(1,Iterations+1)
AResults = np.zeros(((Iterations)+1, len(Prc)+1))
AResults[0,1:] = Prc
AResults[1:,0] = np.arange(1,Iterations+1)

for x in range(Iterations):
    for y in range(len(Prc)):
        PA = (np.random.randint(0,11,numItems))/10
        PC = np.zeros(numItems)
        for i in range(len(PA)):
            if PA[i]>=Prc[y]:
                PC[i] = PA[i] + [(1 - 1)*(.5-PA[i])]
            else:
                PA[i] = PC[i] = None
        
        Quantity = (len(PC[~np.isnan(PC)])*np.average(PC[~np.isnan(PC)]))
        Accuracy = Quantity/len(PC[~np.isnan(PC)])
        QResults[x+1,y+1] = Quantity/numItems
        AResults[x+1,y+1] = Accuracy
        

    
