from queue import Queue

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = Queue()
    queue.put([start])  # Start path

    while not queue.empty():
        path = queue.get()
        x, y = path[-1]  # Current position

        if (x, y) == end:
            return path  # Return all coordinates

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            next_x, next_y = x + dx, y + dy

            # Check bounds and avoid walls
            if (0 <= next_x < rows and 0 <= next_y < cols and
                maze[next_x][next_y] != '#' and
                (next_x, next_y) not in path):

                new_path = list(path)
                new_path.append((next_x, next_y))
                queue.put(new_path)

# Maze example
maze = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', 'E', '#'],
    ['#', '#', '#', '#', '#', '#']
]

start = (1, 1)  # S
end = (4, 4)    # E

# Run BFS
path = bfs(maze, start, end)

if path:
    print("Path found! Coordinates:")
    for coord in path:
        print(coord)
else:
    print("No path exists.")

