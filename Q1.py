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

N = 15
all_Gx = np.zeros((100,N))
final_values = []

for run in range(100):
    # gradient descent
    x1 = np.random.uniform(-10, 10)
    x2 = np.random.uniform(-10, 10)
    x_i = ([x1, x2])
    alpha = 0.3
    epsilon = 0.01
    for i in range(N):
        grad = -part_dev_G(x_i)
        x_i = x_i + alpha * grad
        all_Gx[run,i] = G(x_i)
    final_values.append(all_Gx[run,-1])

# Compute average G(x) at each iteration across all runs
average_Gx = np.mean(all_Gx, axis=0)

# Plot average G(x) over time
plt.plot(range(N), average_Gx)
plt.xlabel('Iteration')
plt.ylabel('Average G(x)')
plt.title('Average G(x) over 100 Gradient Descent Runs')
plt.grid()
plt.show()

# Compute and print std deviation of final values
std_dev = np.std(final_values)
print(f"Standard Deviation of final G(x) values: {std_dev}")