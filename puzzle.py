from collections import deque

GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))


def get_neighbors(state):
    neighbors = []

    # find blank (0) safely
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            # swap
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def bfs(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == GOAL:
            return path + [current]

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current]))

    return None


def print_state(state):
    for row in state:
        print(row)
    print()


# ---- MAIN PROGRAM ----
print("Enter initial state (use 0 for blank):")

start = []
for i in range(3):
    while True:
        try:
            row = tuple(map(int, input().split()))
            if len(row) != 3:
                raise ValueError
            start.append(row)
            break
        except:
            print("Please enter exactly 3 numbers separated by spaces.")

start = tuple(start)

# validate input (optional but helpful)
flat = [num for row in start for num in row]
if sorted(flat) != list(range(9)):
    print("Invalid input! Use numbers 0–8 exactly once.")
else:
    path = bfs(start)

    if path:
        print("\nSolution found in", len(path) - 1, "moves:\n")
        for step in path:
            print_state(step)
    else:
        print("No solution found (this configuration may be unsolvable).")
