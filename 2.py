import numpy as np
import matplotlib.pyplot as plt

#plotting function
def f(x):
    return x**2 - 4*x + 4.5

x = np.linspace(0.0,4.0,100)
y=f(x)

#derivative found manually
def deriv_f(x):
    return 2*x - 4

#gradient descent
x_i=3 #starting point; actual minimum is 2 (found manually)
alpha = 0.1 #step size
N = 30 #iterations
epsilon = 0.02
descent_x = [] #for superimposing
descent_y = []

for i in range (N):
    descent_x.append(x_i)
    descent_y.append(f(x_i))
    d = -deriv_f(x_i) #negative gradient
    if abs(d) < epsilon:
        print(f"Converged after {i} steps")
        break
    x_i = x_i + alpha * d #update position
    print(f"Step {i}: x = {x_i}, f(x) = {f(x_i)}")


#print(f"Minimum at x ={x_i},f(x)={f(x_i)}") shows final result after loop

#superimpose i.e plot gradient descent steps on top of original function
plt.plot(x,y,label='function')
plt.plot(descent_x,descent_y, 'ro-')
plt.show()
