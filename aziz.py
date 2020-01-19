import collections
import random

def bfs(grid):
    #initation of the queue with the starting point
    queue = collections.deque([[(0,0)]])
    #declaring the set of visited nodes
    visited = set([(0,0)])
    while queue:
        #poping the node from the queue
        path = queue.popleft()
        i, j = path[-1]
        #grid[i][j]=2
        #testing if we reach the target or not
        if grid[i][j] == 1:
            #return the length of the path in case of succes
            return (path)
        #generating all possible moves (we could add diagonal moves for our problem by adding 4 other moves)
        for di, dj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= di < len(grid) and 0 <= dj < len(grid[0]) and grid[di][dj] != 1 and (di, dj) not in visited:
                queue.append(path + [(di, dj)])
                visited.add((di, dj))
    #retuning -1 in case of failure
    return(path)



def move(grid, M, N, x, y):
    dx,dy=bfs(grid)[0]
    mv=[ (dx, dy) for dx, dy in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)) if 0 <= dx < len(grid) and 0 <= dy < len(grid[0])]
    dx,dy=random.choice(mv)
    if (dx<x and dy==y):
        return("LEFT")
    elif (dx>x and dy==y):
        return("RIGHT")
    elif (dx==x and dy<y):
        return("DOWN")
    else:
        return("UP")

    