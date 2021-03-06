

import mlrose
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


qatar= pd.read_csv("Downloads/qatar194.csv")

#We define the coordinates of city i:
def coord(i):
    coordinates=(qatar.iloc[i,0],qatar.iloc[i,1])
    return coordinates
coord_list=[coord(i) for i in range(194)]
coord_list


fitness_coords = mlrose.TravellingSales(coords = coord_list)
fitness_coords
problem_fit = mlrose.TSPOpt(length =194, fitness_fn = fitness_coords, maximize=False)
best_state,best_fitness,fit_curve=mlrose.genetic_alg(problem_fit, pop_size=200,
                                                     mutation_prob=0.1, max_attempts=10,
                                                     max_iters=50, curve=True)
#We show below the best road to take and the total length of this road:
print(best_state)

print(best_fitness)
print(fit_curve)


plt.plot(-(fit_curve))
plt.title("Convergence curve for TSP Qatar")
plt.xlabel("Number of iterations")
plt.ylabel("Fitness values")
plt.show()