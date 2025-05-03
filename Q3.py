#Hybrid Optimization: Random Search followed by Gradient Descent
def run_hybrid(G, part_dev_G, N_random=50, N_gd=50, alpha=0.5, runs=100):
    final_values = []
    final_points = []
    all_Gx = np.zeros((runs, N_gd))

    for run in range(runs):
        x_best = np.random.uniform(-10, 10, 2)
        f_min = G(x_best)
        for _ in range(N_random):
            x_new = np.random.uniform(-10, 10, 2)
            f_new = G(x_new)
            if f_new < f_min:
                x_best = x_new
                f_min = f_new

        x_i = x_best.copy()
        for i in range(N_gd):
            gradient = part_dev_G(x_i)
            x_i = x_i - alpha * gradient
            all_Gx[run, i] = G(x_i)
        final_values.append(all_Gx[run, -1])
        final_points.append(x_i.copy())

    average_Gx = np.mean(all_Gx, axis=0)
    best_index = np.argmin(final_values)
    best_gx = final_values[best_index]
    best_x = final_points[best_index]

    # Plot
    plt.plot(range(N_gd), average_Gx, color='purple', marker ='o', linestyle ='-', label='Hybrid')
    plt.xlabel('Iteration')
    plt.ylabel('Average G(x)')
    plt.title('Average G(x) for Hybrid Optimisation')
    plt.grid()
    plt.show()

    std_dev = np.std(final_values)
    average_final_Gx = np.mean(final_values)
    print(f"Standard Deviation of final G(x) values: {std_dev}")
    print(f"Average final G(x) across 100 runs: {average_final_Gx}")
    print(f"Best G(x) found after 100 runs: {best_gx}")
    print(f"Minimizer x corresponding to best G(x): {best_x}")

    return average_Gx, final_values


hybrid_gx, hybrid_finals = run_hybrid(Griewangk, part_dev_G)

