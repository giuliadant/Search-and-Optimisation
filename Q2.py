import matplotlib.pyplot as plt
import numpy as np

def Griewangk(x):
    return 1 + x[0]**2/4000 + x[1]**2/4000 - np.cos(x[0]) * np.cos(0.5 * x[1] * np.sqrt(2))

N = 50
all_Gx = np.zeros((100, N))  #stores values of G(x) for each run, for each iteration
final_values = [] #list to store final value of G(x) from each of the 100 runs

#Initialize global best values
global_fmin = float('inf') #stores the lowest G(x) found across all runs
global_best = None #stores the x coordinates where global minimum was found

#Random search
for run in range(100):
    #Start with a random point
    x_best = np.random.uniform(-10, 10, 2)
    f_min = Griewangk(x_best) #function value at best point

#Generate N new random points
    for i in range(N):
        x_new = np.random.uniform(-10, 10, 2)
        f_new = Griewangk(x_new) #function value at new point

        if f_new < f_min:
            x_best = x_new
            f_min = f_new

        all_Gx[run, i] = f_min  #store best current value so far at this iteration

    final_values.append(f_min) #best value of run

    #If this run's result is best of all runs, update global best and minimiser
    if f_min < global_fmin:
        global_fmin = f_min
        global_best = x_best.copy()

# Compute average G(x) at each iteration across all runs
average_Gx = np.mean(all_Gx, axis=0)

plt.plot(range(N), average_Gx, 'bo-')
plt.xlabel('Iteration')
plt.ylabel('Average G(x)')
plt.title('Average G(x) for Random Search')
plt.grid()
plt.show()

# Standard deviation of final values
std_dev = np.std(final_values)
print(f"Standard Deviation of final G(x) values: {std_dev}")
print(f"Best G(x) found after 100 runs:{global_fmin}")
print(f"Minimizer x at = {global_best}")


