# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:55:13 2020

@author: Sohrab
"""
import mlrose
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


djibouti= pd.read_csv("Downloads/dji38.csv")

#We define the coordinates of city i:
def coord(i):
    coordinates=(djibouti.iloc[i,0],djibouti.iloc[i,1])
    return coordinates
coord_list=[coord(i) for i in range(38)]
coord_list
#We define here the distance between the i-th and j-th city thanks to the dataframe:
def djib_distance(i,j):
    distance=math.sqrt((djibouti.iloc[i,0]-djibouti.iloc[j,0])**2+(djibouti.iloc[i,1]-djibouti.iloc[j,1])**2)
    return distance

fitness_coords = mlrose.TravellingSales(coords = coord_list)
fitness_coords
problem_fit = mlrose.TSPOpt(length =38, fitness_fn = fitness_coords, maximize=False)
best_state,best_fitness,fit_curve=mlrose.genetic_alg(problem_fit, pop_size=1000,
                                                     mutation_prob=0.1, max_attempts=10,
                                                     max_iters=50, curve=True,
                                                     random_state=None)
#We show below the best road to take and the total length of this road:
print(best_state)

print(best_fitness)
print(fit_curve)

fig = plt.figure(figsize=(16, 13))
plt.plot(fit_curve)
plt.title("Convergence curve for TSP Djibouti")
plt.show()




