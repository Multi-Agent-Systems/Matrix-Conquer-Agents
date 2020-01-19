import collections
import random

def bfs(grid,x,y,adi,adj):
    #initation of the queue with the starting point
    queue = collections.deque([[(x,y)]])
    #declaring the set of visited nodes
    visited = set([(x,y)])
    while queue:
        #poping the node from the queue
        path = queue.popleft()
        i, j = path[-1]
        #grid[i][j]=2
        #testing if we reach the target or not
        if (i,j) == (adi,adj):
            #return the length of the path in case of succes
            return (len(path),path)
        #generating all possible moves (we could add diagonal moves for our problem by adding 4 other moves)
        for di, dj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
            if 0 <= di < len(grid) and 0 <= dj < len(grid[0])  and (di, dj) not in visited:
                queue.append(path + [(di, dj)])
                visited.add((di, dj))
    #retuning -1 in case of failure
    


def move(grid, M, N, x, y,x1,y1,x2,y2):

    a1,b1=bfs(grid,x,y,x1,y1)
    a2,b2=bfs(grid,x,y,x2,y2)
    print("#############dist1#############"+str(a1))
    print("#############dist2#############"+str(a2))
    if a1<a2:
        dx,dy=b1[-1]
    else:
        dx,dy=b2[-1]

    #mv=[ (dx, dy) for dx, dy in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)) if 0 <= dx < len(grid) and 0 <= dy < len(grid[0])]
    #dx,dy=random.choice(mv)
    if (dx<=x ):
        return("LEFT")
    elif (dx>=x):
        return("RIGHT")
    elif ( dy>=y):
        return("DOWN")
    elif ( dy<=y):
        return("UP")

    