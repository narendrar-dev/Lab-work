class priorityqueue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort()

    def dequeue(self):
        return self.elements.pop(0)[1]

def uniform_cost_search(graph, start, goal):
    frontier = priorityqueue()
    frontier.enqueue(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier.elements:
        current = frontier.dequeue()

        if current == goal:
            break

        for neighbor, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                frontier.enqueue(neighbor, priority)
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    
    return path, cost_so_far.get(goal, float('inf'))
def main():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 3},
        'D': {'B': 2},
        'E': {'B': 5, 'F': 1},
        'F': {'C': 3, 'E': 1}
    }

    start_node = input("Enter the start node: ")
    goal_node =  input("Enter the goal node: ")
    path, cost = uniform_cost_search(graph, start_node, goal_node)
    print(f"Uniform Cost Search Path: {path} with total cost: {cost}")


if __name__ == "__main__":   
    main()  
