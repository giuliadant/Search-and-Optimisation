def part_dev_G(x):
    const = np.sqrt(2) / 2
    dx = ((2 * x[0]) / 4000 + np.sin(x[0]) * np.cos(const * x[1]))
    dy = ((2 * x[1]) / 4000 + const * np.cos(x[0]) * np.sin(const * x[1]))
    return np.array([dx, dy])


# Gradient Descent optimization over 100 runs
def gradient_descent(G, part_dev_G, alpha=0.5, N=50, runs=100):
    all_Gx = np.zeros((runs, N))  # stores G(x) values at each iteration for each run
    final_values = []
    final_points = []

    for run in range(runs):
        x_i = np.random.uniform(-10, 10, size=2)  # random initial point in 2D
        for i in range(N):
            gradient = part_dev_G(x_i)
            x_i = x_i - alpha * gradient
            all_Gx[run, i] = G(x_i)  # record current G(x) value
        final_values.append(all_Gx[run, -1])
        final_points.append(x_i.copy())

    average_Gx = np.mean(all_Gx, axis=0)
    best_index = np.argmin(final_values)
    best_gx = final_values[best_index]
    best_x = final_points[best_index]

    # Plot
    plt.plot(range(N), average_Gx, 'yo-', label='Gradient Descent')
    plt.xlabel('Iteration')
    plt.ylabel('Average G(x)')
    plt.title('Average G(x) for Gradient Descent')
    plt.grid()
    plt.show()

    std_dev = np.std(final_values)
    average_final_Gx = np.mean(final_values)

    print(f"Standard Deviation of final G(x) values: {std_dev}")
    print(f"Average final G(x) across 100 runs: {average_final_Gx}")
    print(f"Best G(x) found after 100 runs: {best_gx}")
    print(f"Minimizer x corresponding to best G(x): {best_x}")

    return average_Gx, final_values


gd_gx, gd_finals = gradient_descent(Griewangk, part_dev_G)




