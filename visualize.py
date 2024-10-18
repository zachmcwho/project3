import matplotlib.pyplot as plt

# Data from the user
n_values = [1000, 5000, 10000, 50000, 100000]
heap_times = [0.010939836502075195, 0.039893388748168945, 0.04288673400878906, 0.25827980041503906, 0.6841700077056885]
linear_times = [0.05983901023864746, 1.2144503593444824, 1.6386168003082275, 30.540292501449585, 273.91663575172424]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(n_values, heap_times, label='Heap-based Priority Queue Time', marker='o', color='b')
# plt.plot(n_values, linear_times, label='Linear-based Priority Queue Time', marker='o', color='r')

plt.xlabel('Number of Nodes (n)')
plt.ylabel('Time (seconds)')
plt.title('Heap-based vs Linear-based Priority Queue Times')
plt.legend()
plt.grid(True)

# Display the plot

plt.show()
