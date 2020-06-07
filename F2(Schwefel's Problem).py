
import numpy as np
import time
#We define the Schwefel function:
def Schwefel(x):
    a=max([abs(x[i]-shift[i]) for i in range(len(x))])-450
    return a

#Dimension of the problem
D=50
#We define the shift at random 
shift=np.random.uniform(-100,100,D)
x0=np.random.uniform(-100,100,D)
#we use the BFGS method:
from scipy.optimize import minimize
t0=time.time() 
result=minimize(Schwefel,x0, args=(),bounds=(-10,10), method='BFGS', tol=1e-3)
t1=time.time()
print("Computational time: ",t1-t0)
print("Solution: ",result.x)
print("Fitness Value: ",result.fun)



D=500
shift=np.random.uniform(-100,100,D)
x0=np.random.uniform(-100,100,D)
#we use the BFGS method:
from scipy.optimize import minimize
t0=time.time() 
result=minimize(Schwefel,x0, args=(),bounds=(-10,10), method='BFGS', tol=1e-3)
t1=time.time()
print("Computational time: ",t1-t0)
print("Solution: ",result.x)
print("Fitness Value: ",result.fun)