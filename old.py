
# def find_shortest_path_with_heap(
#         graph: dict[int, dict[int, float]],
#         source: int,
#         target: int                                                
# ) -> tuple[list[int], float]:
    
#     pq = HeapPQ()  
#     dist = defaultdict(lambda: math.inf)
#     visited = set()
#     prev = {}
#     dist[source] = 0
#     pq.insert1(source, 0) 

#     while pq:
#         u, u_dist = pq.extract_min()

#         if u in visited:
#             continue
#         visited.add(u)

#         # Early exit if we reached the target node
#         if u == target:
#             path = []
#             while u is not None:
#                 path.insert(0,u)
#                 u = prev.get(u, None)
#             return path, dist[target]

#         for neighbor, weight in graph[u].items():
#             if (neighbor not in visited) and (dist[u] + weight < dist[neighbor]):
#                 dist[neighbor] = dist[u] + weight
#                 prev[neighbor] = u

#                 if neighbor not in visited:
#                     pq.insert1(neighbor, dist[neighbor])
#                 else:
#                     pq.decrease_key(neighbor, dist[neighbor])

#     return [], -1

# def find_shortest_path_with_array(
#         graph: dict[int, dict[int, float]],
#         source: int,
#         target: int
# ) -> tuple[list[int], float]:
    
#     pq = LinearPQ()  
#     dist = defaultdict(lambda: math.inf)
#     dist[source] = 0
#     pq.insert1(source, 0)
#     visited = set()
#     prev = {} 

#     while pq:
#         u, u_dist = pq.extract_min()

#         if u in visited:
#             continue
#         visited.add(u)

#         # Early exit if we reached the target node
#         if u == target:
#             path = []
#             while u is not None:
#                 path.insert(0,u)
#                 u = prev.get(u, None)
#             return path, dist[target]

#         for neighbor, weight in graph[u].items():
#             if dist[u] + weight < dist[neighbor]:
#                 dist[neighbor] = dist[u] + weight
#                 prev[neighbor] = u

#                 if neighbor not in visited:
#                     pq.insert1(neighbor, dist[neighbor])
#                 else:
#                     pq.decrease_key(neighbor, dist[neighbor])

#     return [], -1