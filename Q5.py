plt.figure(figsize=(10, 6))
plt.plot(gd_gx, 'yo-', label='Gradient Descent')
plt.plot(rs_gx, 'bo-', label='Random Search')
plt.plot(hybrid_gx,color='purple', marker ='o', linestyle ='-', label='Hybrid')
plt.plot(sa_gx, color='orange', marker ='o', linestyle ='-',label='Simulated Annealing')

plt.xlabel('Iteration')
plt.ylabel('Average G(x)')
plt.title('Superimposed Convergence Comparison')
plt.legend()
plt.grid()
plt.show()

