import numpy as np
import time
from scipy.optimize import differential_evolution

#Function which returns the product of all components of an array:
def product(x):
    prod=1
    for i in x:
        prod=prod*i
    return prod    

#We define a function which returns the sum of the square of all components of an array:
def square(x):
    sum=0
    for i in range(len(x)):
        sum=sum+(x[i])**2
    return sum

     
#We define the Griewank function in dimension D=50,thanks to the two previous functions:
def Griewank(x):
    sq=np.zeros(D)
    for i in range(D):
        sq[i]=np.cos((x[i]-shift[i])/np.sqrt(i+1))
    s=(1/4000)*square(x-shift) - product(sq)+179
    return s


D=50
#We here define the shift as a random vector,shift was used in the definition of the Ackley function,
#but we did not initialize it:    
shift=np.random.uniform(-600,600,D)
bounds=[(-600,600) for i in range(D)]                       

t0=time.time()
result = differential_evolution(Griewank,bounds,disp=True, mutation=(0.1,1), tol=0.0005,popsize=20,updating='immediate')
t1=time.time()

#Computational time:
print("The computational time is: ",t1-t0)

#We show the minimum and the fitness value at this minimum
print("The solution of the minimization problem is: ",result.x)
print("The fitness value is: ",result.fun)

D=500
shift=np.random.uniform(-600,600,D)
bounds=[(-600,600) for i in range(D)]                       

t0=time.time()
result = differential_evolution(Griewank,bounds,disp=True, mutation=(0.5,1), tol=0.05,popsize=20,updating='immediate')
t1=time.time()

#Computational time:
print("The computational time is: ",t1-t0)

#We show the minimum and the fitness value at this minimum
print("The solution of the minimization problem is: ",result.x)
print("The fitness value is: ",result.fun)





    
