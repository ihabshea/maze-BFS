import turtle
from collections import deque
from collections import Counter
score = 0
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze")
wn.setup(700,700)
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(200)
class RedPen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
class BluePen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
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


def find_path_dfs(maze,start,goal):
    stack = deque([("", start)])
    scoreT = 0
    visited = set()
    graph = mazeg(maze)
    while stack:
        path, current = stack.pop()
        screen_x = -288 + (current[1] * 24)
        screen_y = 288 - (current[0] * 24)
        print(screen_x,screen_y)
        bluepen.goto(screen_x, screen_y)
        bluepen.stamp()
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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    ]
def find_path_bfs(maze,start,goal):
    height = len(maze)
    width = len(maze[0]) if height else 0
    queue = deque([("", start)])
    scoreT = 0
    visited = set()
    graph = mazeg(maze)
    while queue:
        path, current = queue.popleft()
        screen_x = -288 + (current[1] * 24)
        screen_y = 288 - (current[0] * 24)
        print(screen_x,screen_y)
        redpen.goto(screen_x, screen_y)
        redpen.stamp()
        if current == goal:

            return (path,score)
        if current in visited:
            continue
        visited.add(current)
        # if(graph[current] == 2):
        #     score+=1
        for direction, neighbour, score in graph[current]:


            scoreT = scoreT + score
            queue.append((path + direction, neighbour))
    return "Can't find a route."
def setup_maze(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    for y in range(height):
        for x in range(width):
            character = maze[x][y]
            screen_x = -288 + (y * 24)
            screen_y = 288 - (x * 24)
            if character == 1:
                print(screen_x,screen_y)
                pen.goto(screen_x, screen_y)
                pen.stamp()
pen  = Pen()
redpen = RedPen()
bluepen = BluePen()
setup_maze(maze)
print find_path_bfs(maze,(1,1),(24,22))
print find_path_dfs(maze,(1,1),(24,22)) #DFS
while True:
    pass
