from collections import deque
from collections import Counter
score = 0
def mazeg(maze):
    height = len(maze)

    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if (maze[i][j] == 0 or maze[i][j]==2)} #adding all the possible positions
    for row, col in graph.keys(): #adding the possible actions in a given position
        if row < height - 1 and (maze[row + 1][col]==0 or maze[row + 1][col]==2):
            if(maze[row + 1][col]==2):
                graph[(row, col)].append(("D", (row + 1, col),1))
                graph[(row + 1, col)].append(("U", (row, col),1))
            graph[(row, col)].append(("D", (row + 1, col),0))
            graph[(row + 1, col)].append(("U", (row, col),0))
        if col < width - 1 and (maze[row][col + 1]==0 or maze[row][col + 1]==2):
            if maze[row][col + 1]==2:
                graph[(row, col)].append(("R", (row, col + 1),1))
                graph[(row, col + 1)].append(("L", (row, col),1))
            graph[(row, col)].append(("R", (row, col + 1),0))
            graph[(row, col + 1)].append(("L", (row, col),0))
    return graph

def find_path_bfs(maze,start,goal):
    queue = deque([("", start)])
    scoreT = 0
    visited = set()
    graph = mazeg(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:

            return (path,score)
        if current in visited:
            continue
        visited.add(current)
        if(graph[current] == 2):
            score+=1
        for direction, neighbour, score in graph[current]:
            scoreT = scoreT + score
            queue.append((path + direction, neighbour))
    return "Can't find a route."

def find_path_dfs(maze,start,goal):
    stack = deque([("", start)])
    scoreT = 0
    visited = set()
    graph = mazeg(maze)
    while stack:
        path, current = stack.pop()
        if current == goal:
            return (path,scoreT)
        if current in visited:
            continue
        visited.add(current)

        for direction, neighbour, score in graph[current]:
            scoreT = scoreT + score
            stack.append((path + direction, neighbour))
    return "NO WAY!"
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] #1 : way #1: no way.

print find_path_bfs(maze,(1,1),(10,10))
print find_path_dfs(maze,(1,1),(10,10))
