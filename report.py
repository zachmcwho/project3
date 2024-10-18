from main import generate_graph
from main import find_shortest_path_with_array
from main import find_shortest_path_with_heap
from time import time

def run_dijkstra_experiment(seed: int, size: int, density: float, noise: float, source: int, target: int, runs: int = 1):
    total_heap_time = 0
    total_array_time = 0
    total_edges = 0
    start = time()
    positions, weights = generate_graph(seed, size, density, noise)
    end = time()
    total_graph_generation_time = end - start

    for _ in range(runs):
        start = time()
        num_edges = sum(len(edges) for edges in weights.values())
        total_edges += num_edges
        end = time()
        count_num_edges_time = end - start
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

    print(f"n = {size}, density = {density}, # edges = {avg_edges}, graph generation time = {total_graph_generation_time}, edge_count = {count_num_edges_time}, heap time = {avg_heap_time}, linear time = {avg_array_time}")
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



# n = 1000, density = 0.01, # edges = 10000.0, graph generation time = 0.027925968170166016, heap time = 0.009972333908081055, linear time = 0.06981372833251953
# n = 5000, density = 0.002, # edges = 50000.0, graph generation time = 0.08676719665527344, heap time = 0.04288458824157715, linear time = 1.2906315326690674
# n = 10000, density = 0.001, # edges = 100000.0, graph generation time = 0.1685490608215332, heap time = 0.04587721824645996, linear time = 1.6396152973175049
# n = 50000, density = 0.0002, # edges = 500000.0, graph generation time = 0.8950538635253906, heap time = 0.2892265319824219, linear time = 29.280661821365356
# n = 100000, density = 0.0001, # edges = 1000000.0, graph generation time = 1.7518374919891357, heap time = 0.6073780059814453, linear time = 232.17567801475525
# n = 1000, density = 1, # edges = 999000.0, graph generation time = 1.2616255283355713, heap time = 0.1875293254852295, linear time = 7.357879877090454
# n = 2000, density = 1, # edges = 3998000.0, graph generation time = 5.140189170837402, heap time = 0.7729325294494629, linear time = 72.24959182739258
# n = 3000, density = 1, # edges = 8997000.0, graph generation time = 11.587236881256104, heap time = 1.5424747467041016, linear time = 241.43352627754211
# n = 4000, density = 1, # edges = 15996000.0, graph generation time = 21.067107439041138, heap time = 2.9967665672302246, linear time = 733.9318873882294
# n = 5000, density = 1, # edges = 24995000.0, graph generation time = 33.24697208404541, heap time = 3.7649648189544678, linear time = 928.8053805828094
# n = 6000, density = 1, # edges = 35994000.0, graph generation time = 49.50515389442444, heap time = 5.324865341186523, linear time = 1066.4691660404205

# n = 1000, density = 0.01, # edges = 10000.0, graph generation time = 0.02692699432373047, edge_count = 0.0, heap time = 0.015956640243530273, linear time = 0.058843135833740234
# n = 5000, density = 0.002, # edges = 50000.0, graph generation time = 0.08676791191101074, edge_count = 0.0, heap time = 0.03992414474487305, linear time = 1.2534754276275635
# n = 10000, density = 0.001, # edges = 100000.0, graph generation time = 0.17054486274719238, edge_count = 0.000997304916381836, heap time = 0.05086350440979004, linear time = 1.6410696506500244
# n = 50000, density = 0.0002, # edges = 500000.0, graph generation time = 0.8876264095306396, edge_count = 0.003989696502685547, heap time = 0.28925633430480957, linear time = 33.781259059906006
# n = 100000, density = 0.0001, # edges = 1000000.0, graph generation time = 1.793149709701538, edge_count = 0.00498652458190918, heap time = 0.7460343837738037, linear time = 248.63017630577087
# n = 1000, density = 1, # edges = 999000.0, graph generation time = 1.3683679103851318, edge_count = 0.0009984970092773438, heap time = 0.2194204330444336, linear time = 7.3421854972839355
# n = 2000, density = 1, # edges = 3998000.0, graph generation time = 4.964102029800415, edge_count = 0.0, heap time = 0.7948355674743652, linear time = 72.8400149345398
# n = 3000, density = 1, # edges = 8997000.0, graph generation time = 11.12525749206543, edge_count = 0.0, heap time = 1.5365586280822754, linear time = 234.08502650260925
# n = 4000, density = 1, # edges = 15996000.0, graph generation time = 21.025137186050415, edge_count = 0.0, heap time = 2.866142511367798, linear time = 714.9358296394348
# n = 5000, density = 1, # edges = 24995000.0, graph generation time = 32.46184539794922, edge_count = 0.0009989738464355469, heap time = 3.6994435787200928, linear time = 979.9214916229248
# n = 6000, density = 1, # edges = 35994000.0, graph generation time = 49.86312294006348, edge_count = 0.0009975433349609375, heap time = 5.655792474746704, linear time = 1042.1334660053253