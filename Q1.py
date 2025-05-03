import matplotlib.pyplot as plt
import numpy as np

def G(x):
    return 1 + x[0]**2 / 4000 + x[1]**2 / 4000 - np.cos(x[0]) * np.cos(0.5 * x[1] * np.sqrt(2))


#partial dev found manually with respect to x and y
def part_dev_G(x):
    const = np.sqrt(2)/2
    dx = ((2 * x[0]) / 4000 + np.sin(x[0]) * np.cos(const * x[1]))
    dy = ((2 * x[1]) / 4000 + const * np.cos(x[0]) * np.sin(const * x[1]))
    return np.array([dx, dy])

N = 50
alpha = 0.4
all_Gx = np.zeros((100,N)) #Stores values of G(x) for each run, for each iteration
final_values = [] #list to store final value of G(x) from each of the 100 runs
final_points = [] #list to store final values of x from each run

for run in range(100): #run gradient for 100 times, each time starting with a random point
    x_i = np.random.uniform(-10, 10, size=2)
    # gradient descent
    for i in range(N):
        gradient = part_dev_G(x_i)
        x_i = x_i - alpha * gradient
        all_Gx[run,i] = G(x_i) #evaluates function at current iteration in run number
    final_values.append(all_Gx[run,-1]) #function value at last iteration of run
    final_points.append(x_i.copy())  # store the minimizer

# Compute average G(x) at each iteration across all runs
average_Gx = np.mean(all_Gx, axis=0)
average_final_Gx = np.mean(final_values)

# Find the index of the best final G(x) across all 100 runs
best_index = np.argmin(final_values)

# Get the best G(x) and the corresponding minimizer x
best_gx = final_values[best_index]
best_x = final_points[best_index]

# Plot average G(x) over time
plt.plot(range(N), average_Gx, 'yo-')
plt.xlabel('Iterations')
plt.ylabel('G(x)')
plt.title('Average G(x) for Gradient Descent')
plt.grid()
plt.show()

# Compute and print std deviation of final values
std_dev = np.std(final_values)
print(f"Standard Deviation of final G(x) values: {std_dev}")
print(f"Average final G(x) across 100 runs: {average_final_Gx}")
print(f"Best G(x) found after 100 runs:{best_gx}")
print(f"Minimizer x at = {best_x}")


