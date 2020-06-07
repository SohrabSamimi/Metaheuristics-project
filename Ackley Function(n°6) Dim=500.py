import numpy as np
import pygmo
import time
from scipy.optimize import differential_evolution
#We define a function which returns the sum of the square of all components of an array:
def square(x):
    sum=0
    for i in range(len(x)):
        sum=sum+(x[i])**2
    return sum

#We define a function which returns the sum of all components of an array:
def my_sum(x):
    sum=0
    for i in x:
        sum=sum+i
    return sum      
D=500   
#We define the Ackley function in dimension D=50,thanks to the two previous functions:
def Ackley(x):
    my_cos=np.array([np.cos(2*np.pi*(x[i]-shift[i])) for i in range(D)])
    a=((-20)*np.exp(-0.2*np.sqrt(1/D*square(x-shift)))
    -np.exp(1/D*my_sum(my_cos))+ 20 +np.exp(1.0)-140)
    return a

#We here define the shift as a random vector,shift was used in the definition of the Ackley function,
#but we did not initialize it:    
shift=np.random.uniform(-32,32,D)
bounds=[(-32,32) for i in range(D)]                       

t0=time.time()
result = differential_evolution(Ackley,bounds,disp=True, mutation=(0.1,1), tol=0.0005,popsize=20,updating='immediate')
t1=time.time()

#Computational time:
print("The computational time is: ",t1-t0)

#We show the minimum and the fitness value at this minimum
print("The solution of the minimization problem is: ",result.x)
print("The fitness value is: ",result.fun)







