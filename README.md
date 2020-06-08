# Metaheuristics-project

The objective is to solve different problems using metaheuristics. We have
2 discrete optimization problems and 6 continuous problems to solve.
For each function we report:
- The chosen algorithm and a justification of this choice
- The parameters of the algorithm
- The final results, both solution and fitness
- The number of function evaluations
- The stopping criterion
- The computational time
- The convergence curve (fitness as a function of time)

We want to solve two TSP problems.
One with 38 cities (Djibouti) and the other with 194 cities (Qatar).

We want to minimize the following functions:
- Shifted Sphere Function
- Schwefel's Problem
- Shifted Rosenbrock Function
- Shifted Rastrigin's Function
- Shifted Griewank Function
- Shifted Ackley Function


For this project we have to minimize 6 functions,and solve two TSP problems.
We shall begin the report with the 6 functions.

1st function: Shifted Sphere Function
 - As this function is convex and differentiable everywhere,we implement an algorithm which computes the gradient in any dimension,then we implement the gradient descent algorithm.
 - In both dimension 50 and 500,this algorithm does around 50 to 60 iterations depending on the initial vector that we choose(which we here initialize randomly) and the learning rate(0.1 in our case),and the fitness value is very close to -450 as expected (in both dimensions).
About the convergence curve,it decreases rapidly,that is after 10 iterations,the curve almost reaches the minimum -450
 - Convergence curve:

![gda](https://user-images.githubusercontent.com/58103877/84086815-071c7100-a9e9-11ea-8d8f-1217b9a956c4.png)


2nd function: Schwefel’s Problem
 - We use the BFGS method.The computational time is around 1.2 seconds,and the fitness value around -450 in dimension 50.In dimension 500 the algorithm seems not to be efficient as the computations are too long.

3rd function: Rosenbrock’s function
 - We use the Nelder-Mead simplex method.The computational time is around 1.5 seconds and the fitness value around 11600 in dimensions 50. In dimension 500 the algorithm seems not to be efficient as the computations are too long.

5th function:Griewank’s function
 - We use the differential evolution algorithm from the Scipy library.There are around 40 iterations,the computational time is around 14 seconds,and the fitness value is around 178,in dimensions 50.


6th function:Ackley’s function
 - We use again the differential evolution algorithm from Scipy.Around 70 iterations,a computational time around 18 seconds,a fitness value around -140 in dimension 50.Again in dimension 50,the computational time is too long.


TSP Problem Djibouti(38 cities):
 - We used mlrose’s TSPOpt() function.
 - The best route is the following:
 - [ 7 13 31 6 21 14 10 19 24 11 2 9 0 20 16 35 23 25 36 37 27 15 30 32
     33 34 29 28 5 17 26 12 3 4 8 22 1 18].
 - The optimal tour length associated to this best route is around 20692 kilometers.
 - Convergence curve:

