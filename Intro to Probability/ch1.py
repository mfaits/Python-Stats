# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:18:24 2018

@author: FAITSMC
"""

import random
import numpy as np
import matplotlib.pyplot as plt

#%%
#1: Toss a coin n times and print out after every 100 tosses the proportion of heads minus 1/2.
#1b: Modify the program to print out the proportion of heads minus 1/2 and the number of heads minus half the number of tosses

Proportion = 0
count = -1
endFlips = 100001
sizeResults = int((endFlips-1)/100)
Results = np.zeros(sizeResults+1)
Results2 = np.zeros(sizeResults+1)

for n in range(0,endFlips,100):
    count = count + 1
    tossMatrix = np.zeros(n)
    for i in range(1,n):
        tossMatrix[i-1]= random.randint(0,1)
    Proportion = np.sum(tossMatrix)/n
    HeadsMinusHalf = np.sum(tossMatrix) - (n/2)
    Results[count] = Proportion-0.5
    Results2[count] = HeadsMinusHalf

x = np.arange(0,endFlips,100)

plt.figure(1)
plt.plot(x,Results)
plt.title('Proportion of heads minus 1/2')

plt.figure(2)
plt.plot(x,Results2)
plt.title('Number of heads minus half toss count')

#%%
#2: Modify the program CoinTosses so that it tosses a coin n times and records whether or not the proportion of heads is within 0.1 of 0.5 (i.e. between 0.4 and 0.6). Have your program repeat this experiment 100 times. About how large must n be so that approximately 95 out of 100 times the proportion of heads is between 0.4 and 0.6?

Proportion = 0
count = -1
outcomeMatrix = np.zeros(1000)

for n in range(1,1001):
    ProportionMatrix = np.zeros(100)
    for i in range(1,101):
        tossMatrix = np.zeros(n)
        for j in range(1,n+1):
            tossMatrix[j-1] = random.randint(0,1)
        Proportion = np.sum(tossMatrix)/n
        if Proportion > 0.4 and Proportion < 0.6:
            ProportionMatrix[i-1] = 1
        else:
            ProportionMatrix[i-1] = 0
    outcomeMatrix[n-1] = np.sum(ProportionMatrix)/np.size(ProportionMatrix,0)
 
plt.figure(1)           
x = np.arange(1,1001)
plt.plot(x,outcomeMatrix)
plt.axhline(y=0.95, color='r', linestyle='-')

for k in range (1,np.size(outcomeMatrix,0)+1):
    if outcomeMatrix[k-1] > 0.95:
        print('The n that first crosses the 95%% threshold is %d' %(k))
        break
    

#%%