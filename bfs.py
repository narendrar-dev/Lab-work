from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph.get(node, []):   # safe access
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


n = int(input("Enter the number of nodes: "))
graph = {}

for i in range(n):
    neighbours = list(map(int, input(f"Enter the neighbors of node {i} (space separated): ").split()))
    graph[i] = neighbours

start_node = int(input("Enter the starting node for BFS: "))
print("BFS Traversal starting from node", start_node)

bfs(graph, start_node)