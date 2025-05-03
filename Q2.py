#Random Search algorithm over 100 runs
def random_search(G, N=50, runs=100):
    all_Gx = np.zeros((runs, N))
    final_values = []
    final_points = []

    for run in range(runs):
        x_best = np.random.uniform(-10, 10, 2)
        f_min = G(x_best)
        for i in range(N):
            x_new = np.random.uniform(-10, 10, 2) #generate a new random point
            f_new = G(x_new) #evaluate function at new point
            if f_new < f_min: #if it's better, update best
                x_best = x_new
                f_min = f_new
            all_Gx[run, i] = f_min #store best value found so far
        final_values.append(f_min)
        final_points.append(x_best.copy())

    average_Gx = np.mean(all_Gx, axis=0)
    best_index = np.argmin(final_values)
    best_gx = final_values[best_index]
    best_x = final_points[best_index]

    # Plot
    plt.plot(range(N), average_Gx, 'bo-', label='Random Search')
    plt.xlabel('Iteration')
    plt.ylabel('Average G(x)')
    plt.title('Average G(x) for Random Search')
    plt.grid()
    plt.show()

    std_dev = np.std(final_values)
    average_final_Gx = np.mean(final_values)

    print(f"Standard Deviation of final G(x) values: {std_dev}")
    print(f"Average final G(x) across 100 runs: {average_final_Gx}")
    print(f"Best G(x) found after 100 runs: {best_gx}")
    print(f"Minimizer x corresponding to best G(x): {best_x}")

    return average_Gx, final_values


rs_gx, rs_finals = random_search(Griewangk)
