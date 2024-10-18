
import math
from collections import defaultdict
from HeapPriorityQueue import HeapPQ

def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    
    pq = HeapPQ()  
    dist = defaultdict(lambda: math.inf)
    dist[source] = 0
    pq.insert1(source, 0)
    visited = set()
    prev = {} 

    while pq:
        u, u_dist = pq.extract_min()

        if u in visited:
            continue
        visited.add(u)

        # Early exit if we reached the target node
        if u == target:
            path = []
            while u is not None:
                path.insert(0,u)
                u = prev.get(u, None)
            return path, dist[target]

        for neighbor, weight in graph[u].items():
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                prev[neighbor] = u

                if neighbor not in visited:
                    pq.insert1(neighbor, dist[neighbor])
                else:
                    pq.decrease_key(neighbor, dist[neighbor])

    return [], -1
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
from LinearPriorityQueue import LinearPQ

def find_shortest_path_with_array(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    
    pq = LinearPQ()  
    dist = defaultdict(lambda: math.inf)
    dist[source] = 0
    pq.insert1(source, 0)
    visited = set()
    prev = {} 

    while pq:
        u, u_dist = pq.extract_min()

        if u in visited:
            continue
        visited.add(u)

        # Early exit if we reached the target node
        if u == target:
            path = []
            while u is not None:
                path.insert(0,u)
                u = prev.get(u, None)
            return path, dist[target]

        for neighbor, weight in graph[u].items():
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                prev[neighbor] = u

                if neighbor not in visited:
                    pq.insert1(neighbor, dist[neighbor])
                else:
                    pq.decrease_key(neighbor, dist[neighbor])

    return [], -1

    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
