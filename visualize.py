import matplotlib.pyplot as plt

# n = 1000, density = 0.01, # edges = 10000.0, heap time = 0.013672113418579102, linear time = 0.019278764724731445
# n = 5000, density = 0.002, # edges = 50000.0, heap time = 0.06822896003723145, linear time = 0.47414493560791016
# n = 10000, density = 0.001, # edges = 100000.0, heap time = 0.07007694244384766, linear time = 0.7180957794189453
# n = 50000, density = 0.0002, # edges = 500000.0, heap time = 0.33640289306640625, linear time = 13.327552080154419
# n = 100000, density = 0.0001, # edges = 1000000.0, heap time = 0.8973870277404785, linear time = 89.96755123138428

# Data from the user
n_values = [1000, 5000, 10000, 50000, 100000]
heap_times = [0.013672113418579102, 0.06822896003723145, 0.07007694244384766, 0.33640289306640625, 0.8973870277404785]
linear_times = [0.019278764724731445, 0.47414493560791016, 0.7180957794189453, 13.327552080154419, 89.96755123138428]


# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(n_values, heap_times, label='Heap-based Priority Queue Time', marker='o', color='b')
plt.plot(n_values, linear_times, label='Linear-based Priority Queue Time', marker='o', color='r')

plt.xlabel('Number of Nodes (n)')
plt.ylabel('Time (seconds)')
plt.title('Heap-based vs Linear-based Priority Queue Times')
plt.legend()
plt.grid(True)

# Display the plot

plt.show()
