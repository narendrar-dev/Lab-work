
def dls(graph, node, goal, depth, visited):
  
    if node == goal:
        return True


    if depth == 0:
        return False

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth - 1, visited):
                return True

    return False


def iddfs(graph, start, goal, max_depth):
   
    for depth in range(max_depth + 1):
        visited = set()
        print(f"Searching at depth: {depth}")

        if dls(graph, start, goal, depth, visited):
            print(f"Goal '{goal}' found at depth {depth}")
            return True

    print(f"Goal '{goal}' not found within depth {max_depth}")
    return False



if __name__ == "__main__":
    # Graph representation (Adjacency List)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = input("Enter start node: ").strip()
    goal_node = input("Enter goal node: ").strip()
    max_depth = int(input("Enter maximum depth: "))

    result = iddfs(graph, start_node, goal_node, max_depth)

    if result:
        print("Search Successful ✅")
    else:
        print("Search Failed ❌")
