# -*- coding: utf-8 -*-
"""
Koriat and Goldsmith

Simulation of distribution of judgments

Parameters produce all figures other than Figure 2.
@author: tmc27
"""

import numpy as np

Iterations = 100
Prc = np.arange(0,1.1,.1)
Correspondence = np.arange(0,1.1,.1)
Dist = np.arange(-1,1.1,.1)
numItems = 100

for x in range(Iterations):
    for y in range(len(Prc)):
        for d in Dist:
            for s in Correspondence:
                p = q = 1.8**(-d*10)
                PA = np.divide(np.around(np.random.beta(p,q,numItems)*10, decimals = 0),10)
                PC = np.zeros(numItems)
                for i in range(len(PA)):
                        if PA[i]>=Prc[y]:
                            PC[i] = PA[i] + [(1 - s)*(.5-PA[i])]
                        else:
                            PA[i] = PC[i] = None
                Quantity = (len(PC[~np.isnan(PC)])*np.average(PC[~np.isnan(PC)]))
                Accuracy = Quantity/len(PC[~np.isnan(PC)])
                print(Accuracy)
