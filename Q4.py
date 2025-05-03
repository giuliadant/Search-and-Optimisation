import numpy as np
import matplotlib.pyplot as plt

def G(x):
    return 1 + x[0]**2 / 4000 + x[1]**2 / 4000 - np.cos(x[0]) * np.cos(0.5 * x[1] * np.sqrt(2))

#Simulated Annealing Algorithm
def simulated_annealing(G, T=0.5, k_max=50, runs=100):
    #Exponentianl Annealing Schedule
    def temperature(k, t0=100, decay=0.5):
        return t0 * (decay ** k)

    all_Gx = np.zeros((runs, k_max))
    final_values = []
    final_points = []

    for run in range(runs):
        x = np.random.uniform(-10, 10, 2)
        y = G(x)
        best_x, best_y = x.copy(), y
        gx_list = []

        for k in range(1, k_max + 1):
            t = temperature(k)
            x_new = x + np.random.uniform(-T, T, 2)
            x_new = np.clip(x_new, -10, 10)
            y_new = G(x_new)
            delta_y = y_new - y
            if delta_y <= 0 or np.random.rand() < np.exp(-delta_y / t):
                x, y = x_new, y_new
            if y < best_y:
                best_x, best_y = x.copy(), y
            gx_list.append(y)

        all_Gx[run, :] = gx_list
        final_values.append(best_y)
        final_points.append(best_x)

    average_Gx = np.mean(all_Gx, axis=0)
    best_index = np.argmin(final_values)
    best_gx = final_values[best_index]
    best_x = final_points[best_index]
    # Plot
    plt.plot(range(k_max), average_Gx, color='orange', marker='o', linestyle='-', label='Simulated Annealing')
    plt.xlabel('Iteration')
    plt.ylabel('Average G(x)')
    plt.title('Average G(x) for Simulated Annealing')
    plt.grid()
    plt.show()

    std_dev = np.std(final_values)
    average_final_Gx = np.mean(final_values)

    print(f"Standard Deviation of final G(x) values: {std_dev}")
    print(f"Average final G(x) across 100 runs: {average_final_Gx}")
    print(f"Best G(x) found after 100 runs: {best_gx}")
    print(f"Minimizer x corresponding to best G(x): {best_x}")

    return average_Gx, final_values


sa_gx, sa_finals = simulated_annealing(Griewangk)

