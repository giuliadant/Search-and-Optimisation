import numpy as np
import matplotlib.pyplot as plt

#plotting function
def f(x):
    return x**2 - 4*x + 4.5

x = np.linspace(0.0,4.0,100)
y=f(x)

print(y)

plt.plot(x,y,label='function')
plt.savefig("plot.png")
plt.show()

#derivative found manually
def deriv_f(x):
    return 2*x - 4

#gradient descent
x=1 #starting point; actual minimum is 2 (found manually)
alpha = 0.1 #step size
N = 20 #iterations

for i in range (N):
    d = -deriv_f(x) #negative gradient
    x = x + alpha * d #update position
    print(f"Step {i}: x = {x}, f(x) = {f(x)}")


#print(f"Minimum at x ={x},f(x)={f(x)}") shows final result after loop