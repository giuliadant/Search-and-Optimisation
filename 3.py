import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(x,y):
    return x**2 + y**2 + 1

x=np.linspace(-20.0,20.0,100)
y=np.linspace(-20.0,20.0,100)
X,Y = np.meshgrid(x,y) #2D Arrays
Z= f(X,Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X,Y,Z,color ='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig('3D plot.png')
plt.show()

#partial dev found manually with respect to x and y
def part_dev_f(x,y):
    return 2*x, 2*y

#gradient descent
x_i = 10
y_i = 5
alpha = 0.3
epsilon = 0.02
N = 100

for i in range(N):
    dx, dy = part_dev_f(x_i,y_i)
    dx, dy = -dx,-dy
    if abs(dx) < epsilon and abs(dy) < epsilon:
        print(f"Converged after {i} steps")
        break
    x_i = x_i + alpha * dx
    y_i = y_i + alpha * dy
    print(f"Step {i}: x = {x_i}, y={y_i} f(x,y) = {f(x_i,y_i)}")



