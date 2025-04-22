import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import time

def Griewangk(x, a=1, b=5):
    return 1+ x[0]**2/4000 + x[1]**2/4000 - np.cos(x[0])*np.cos(0.5*x[1]*np.sqrt(2))

N = 100
all_Gx = np.zeros((100,N))
final_values = []
global_best = None
global_fmin = float('inf')

for run in range(100):
    x_best = np.random.uniform(-10, 10, 2)
    f_min = Griewangk(x_best)

    for i in range (N):
        x_new = np.random.uniform(-10,10,2)
        f_new =Griewangk(x_new)
        all_Gx[run, i] = f_min

        if f_new < f_min:
            x_best = x_new
            f_min = f_new

    final_values.append(f_min)

    if f_min < global_fmin:
        global_best = x_best
        global_fmin = f_min

# Compute average G(x) at each iteration across all runs
average_Gx = np.mean(all_Gx, axis=0)

plt.plot(range(N), average_Gx)
plt.xlabel('Iteration')
plt.ylabel('Average G(x)')
plt.title('Average G(x) over 100 Random Search Runs')
plt.grid()
plt.show()

# Standard deviation of final values
std_dev = np.std(final_values)
print(f"Standard Deviation of final G(x) values: {std_dev}")
print(f"Best x found: {global_best}, Griewangk(x) = {global_fmin}")


