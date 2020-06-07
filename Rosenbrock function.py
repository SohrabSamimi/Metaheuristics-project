import scipy
from scipy.optimize import minimize
import time

def rosenbrock(x):
    a=0
    for i in range(len(x)-1):
        a=a+100*(x[i+1]-(x[i])**2)**2+(x[i]-1)**2
    return a    

D=50
x=np.random.uniform(-5,10,D)
t0=time.time()
result=minimize(rosenbrock,x,args=(),bounds=(-5,10),method='Nelder-Mead',tol=1e-3)
t1=time.time()
print("Computational time: ",t1-t0)
print("Solution: ",result.x)
print("Fitness Value: ",result.fun)

D=500

x=np.random.uniform(-5,10,D)
t0=time.time()
result=minimize(rosenbrock,x,args=(),bounds=(-5,10),method='Nelder-Mead',tol=1e-3)
t1=time.time()
print("Computational time: ",t1-t0)
print("Solution: ",result.x)
print("Fitness Value: ",result.fun)




