import matplotlib.pyplot as plt

# Data for visualization
n_values = [1000, 2000, 3000, 4000, 5000, 6000]
heap_times = [
    0.2064115047454834, 
    0.7667218685150147, 
    1.6733731269836425, 
    3.1063557624816895, 
    4.373342704772949, 
    6.031571578979492
]
linear_times = [
    0.0994659423828125, 
    0.39360713958740234, 
    0.9945423603057861, 
    1.958125352859497, 
    3.028878021240234, 
    4.427707290649414
]


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