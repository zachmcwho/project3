import matplotlib.pyplot as plt

# Data for visualization
n_values = [1000, 2000, 3000, 4000, 5000, 6000]
heap_times = [0.1875293254852295, 0.7729325294494629, 1.5424747467041016, 2.9967665672302246, 3.7649648189544678, 5.324865341186523]
linear_times = [7.357879877090454, 72.24959182739258, 241.43352627754211, 733.9318873882294, 928.8053805828094, 1066.4691660404205]

# Create a plot
plt.figure(figsize=(10, 6))
# plt.plot(n_values, heap_times, label='Heap Time', marker='o')
plt.plot(n_values, linear_times, label='Linear Time', marker='o')

# Adding titles and labels
plt.title('Performance of Dijkstra Algorithm with Heap and Linear PQ')
plt.xlabel('Number of Nodes (n)')
plt.ylabel('Time (seconds)')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
