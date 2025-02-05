"""
This module implements a Breadth-First Search (BFS) algorithm for debugging practice.
"""

from collections import deque

def bfs(graph, start):
    """
    Performs a Breadth-First Search on a graph starting from a given node.

    Args:
        graph (dict): A dictionary representing an adjacency list of the graph.
        start: The starting node.

    Returns:
        list: The BFS traversal order.
    """

    if start not in graph:
        raise ValueError(f"Start node '{start}' not in graph.")

    visited = set()
    traversal = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

# Example graph (Adjacency List Representation)
test_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
result = bfs(test_graph, 'A')
print("BFS Traversal:", result)
