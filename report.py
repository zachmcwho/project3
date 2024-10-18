from main import generate_graph
from main import find_shortest_path_with_array
from main import find_shortest_path_with_heap
from time import time

def run_dijkstra_experiment(seed: int, size: int, density: float, noise: float, source: int, target: int, runs: int = 1):
    total_heap_time = 0
    total_array_time = 0
    total_edges = 0
    
    positions, weights = generate_graph(seed, size, density, noise)
    for _ in range(runs):
        num_edges = sum(len(edges) for edges in weights.values())
        total_edges += num_edges

        # Run heap-based Dijkstra
        start = time()
        _, _ = find_shortest_path_with_heap(weights, source, target)
        end = time()
        total_heap_time += (end - start)

        # Run array-based Dijkstra
        start = time()
        _, _ = find_shortest_path_with_array(weights, source, target)
        end = time()
        total_array_time += (end - start)

    # Compute averages
    avg_edges = total_edges / runs
    avg_heap_time = total_heap_time / runs
    avg_array_time = total_array_time / runs

    print(f"n = {size}, density = {density}, # edges = {avg_edges}, heap time = {avg_heap_time}, linear time = {avg_array_time}")
    return avg_edges, avg_heap_time, avg_array_time


if __name__ == '__main__':
    results = []

    # For testing: smaller n values from each table
    test_cases = [
        (1000, 0.01), (5000, 0.002),  # First table small n's
        (1000, 1), (2000, 1)          # Second table small n's
    ]

    test_cases = [
        # First table values
        (1000, 0.01), 
        (5000, 0.002), 
        (10000, 0.001), 
        (50000, 0.0002), 
        (100000, 0.0001),

        # Second table values
        (1000, 1), 
        (2000, 1), 
        (3000, 1), 
        (4000, 1), 
        (5000, 1), 
        (6000, 1)
    ]

    for n, density in test_cases:
        avg_edges, avg_heap_time, avg_array_time = run_dijkstra_experiment(312, n, density, 0.02, 2, 9)
        results.append((n, density, avg_edges, avg_heap_time, avg_array_time))

    # Print final results for testing
    for result in results:
        print(f"n = {result[0]}, density = {result[1]}, # edges = {result[2]}, heap time = {result[3]}, linear time = {result[4]}")
