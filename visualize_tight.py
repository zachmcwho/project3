import matplotlib.pyplot as plt

# Data for visualization
n_values =  [1000, 2000, 3000, 4000, 5000, 6000]
heap_times = [0.2947671413421631, 1.0653650760650635, 2.193634271621704, 4.00280499458313, 5.651551008224487, 7.672486782073975]
linear_times =  [0.14450502395629883, 0.6112771034240723, 1.3947031497955322, 2.631787061691284, 4.143615961074829, 5.824986219406128]


# Create a plot
# plt.figure(figsize=(10, 6))
plt.plot(n_values, heap_times, label='Heap Time', marker='o')
plt.plot(n_values, linear_times, label='Linear Time', marker='o')

# Adding titles and labels
plt.title('Performance of Dijkstra Algorithm with Heap and Linear PQ')
plt.xlabel('Number of Nodes (n)')
plt.ylabel('Time (seconds)')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()


# n = 1000, density = 1, # edges = 999000.0, heap time = 0.2947671413421631, linear time = 0.14450502395629883
# n = 2000, density = 1, # edges = 3998000.0, heap time = 1.0653650760650635, linear time = 0.6112771034240723
# n = 3000, density = 1, # edges = 8997000.0, heap time = 2.193634271621704, linear time = 1.3947031497955322
# n = 4000, density = 1, # edges = 15996000.0, heap time = 4.00280499458313, linear time = 2.631787061691284
# n = 5000, density = 1, # edges = 24995000.0, heap time = 5.651551008224487, linear time = 4.143615961074829
# n = 6000, density = 1, # edges = 35994000.0, heap time = 7.672486782073975, linear time = 5.824986219406128