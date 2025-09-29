import heapq

def a_star_search(graph, heuristics, start, goal):
    pq = [(heuristics[start], start, [start], 0)]  # (f, node, path, g)
    visited = set()

    while pq:
        f, node, path, g = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(pq, (f_new, neighbor, path + [neighbor], g_new))

    return None, float("inf")


# Example graph (replace with actual edges!)
graph = {
    'S': {'A': 2, 'B': 5},
    'A': {'C': 4, 'D': 6},
    'B': {'D': 3, 'E': 7},
    'C': {'G': 5},
    'D': {'G': 4},
    'E': {'G': 2},
    'G': {}
}

heuristics = {
    'S': 20,
    'A': 10,
    'B': 25,
    'C': 12,
    'D': 16,
    'E': 17,
    'G': 0
}

start, goal = 'S', 'G'
path, cost = a_star_search(graph, heuristics, start, goal)

print("Best shortest path:", " -> ".join(path))
print("Total cost:", cost)
