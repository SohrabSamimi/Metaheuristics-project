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
We shall begin the report with the 6 functions:

1st function: Shifted Sphere Function
As this function is convex and differentiable everywhere,we implement an algorithm which computes the gradient in any dimension,then we implement the gradient descent algorithm.
In both dimension 50 and 500,this algorithm does around 50 to 60 iterations depending on the initial vector that we choose(which we here initialize randomly) and the learning rate(0.1 in our case),and the fitness value is very close to -450 as expected (in both dimensions).
About the convergence curve,it decreases rapidly,that is after 10 iterations,the curve almost reaches the minimum -450
Convergence curve:

![Alt text](Downloads\Convergence Curve GDA.bmp?raw=True "Title")



 

2nd function: Schwefel’s Problem
We use the BFGS method.The computational time is around 1.2 seconds,and the fitness value around -450 in dimension 50.In dimension 500 the algorithm seems not to be efficient as the computations are too long.

3rd function: Rosenbrock’s function
We use the Nelder-Mead simplex method.The computational time is around 1.5 seconds and the fitness value around 11600 in dimensions 50. In dimension 500 the algorithm seems not to be efficient as the computations are too long.

5th function:Griewank’s function
We use the differential evolution algorithm from the Scipy library.There are around 40 iterations,the computational time is around 14 seconds,and the fitness value is around 178,in dimensions 50.


6th function:Ackley’s function
We use again the differential evolution algorithm from Scipy.Around 70 iterations,a computational time around 18 seconds,a fitness value around -140 in dimension 50.Again in dimension 50,the computational time is too long.


TSP Problem Djibouti(38 cities):
We used mlrose’s TSPOpt() function.
The best route is the following:
[ 7 13 31 6 21 14 10 19 24 11 2 9 0 20 16 35 23 25 36 37 27 15 30 32
33 34 29 28 5 17 26 12 3 4 8 22 1 18]
The optimal tour length associated to this best route is around 20692 kilometers.
Convergence curve:
 


TSP Problem Qatar(194 cities):
We use again TSPOpt().
The optimal tour is the following:
[ 72 192 149 93 86 89 76 105 46 161 183 126 44 91 96 95 118 142
39 42 6 20 133 111 16 18 131 15 154 38 78 124 136 63 178 128
73 163 61 3 10 77 34 110 188 175 181 90 101 58 24 121 82 1
60 30 41 85 35 144 174 98 88 116 56 64 141 87 165 33 36 62
79 117 74 53 187 182 114 109 29 8 43 69 155 68 123 107 157 80
122 164 170 55 138 145 171 84 94 190 150 125 48 25 113 129 189 166
13 75 139 81 176 168 92 51 26 130 5 140 120 40 185 67 71 37
70 108 66 143 173 177 186 191 97 59 112 193 146 65 49 50 83 47
17 152 103 27 52 158 12 102 132 0 11 2 162 31 100 7 21 9
19 104 45 137 160 179 119 172 147 184 32 153 14 54 99 169 180 23
148 115 156 135 159 4 28 22 151 106 57 127 167 134]
The total tour length associated is around 82307 km.
The computational time is around 5 seconds
Convergence curve:
 


