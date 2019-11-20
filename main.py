# Libraries
import random as rd 
import bilel as Ag1
import ilyes as Ag2
import aziz as Ag3
import molk as Ag4

# Define Matrix class

class Matrix:
    def __init__(self,N,M):
        self.N = N
        self.M = M
        self.grid = [ [ 0 for j in range(M) ] for i in range(N) ]

    def set(self,v,x,y):
        if (self.grid[x][y] == 0):
            self.grid[x][y] = v

    def info(self):
        for row in self.grid:
            print (' '.join(map(str,row)))
        blue = 0
        red = 0
        for row in self.grid:
            for x in row:
                if x == 1:
                    blue = blue + 1
                if x == 2:
                    red = red + 1
        print ('BLUE TEAM SCORE:',blue)
        print ('RED TEAM SCORE:',red)

# Initantiate Matrix

#N = rd.randint(80,360)
#M = rd.randint(80,360)
N = rd.randint(20,30)
M = rd.randint(20,30)

matrix = Matrix(N,M)

# Define Player Class

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def info(self):
        print(self.name,'is in',self.x,self.y)

    def move(self,team,dir,matrix):
        if (dir.upper() == 'UP'):
            self.x = max(self.x-1, 0)
        if (dir.upper() == 'DOWN'):
            self.x = min(self.x+1, matrix.N-1)
        if (dir.upper() == 'LEFT'):
            self.y = max(self.y-1,0)
        if (dir.upper() == 'RIGHT'):
            self.y = min(self.y+1, matrix.M-1)
        matrix.set(team, self.x, self.y)
    


# Define Team Class

class Team:
    def __init__(self,name,p1,p2):
        self.name = name
        self.p1 = p1
        self.p2 = p2
    def info(self):
        print('Team:',self.name)
        self.p1.info()
        self.p2.info()

# Instantiate Teams

blueTeam = Team('BLUE', Player('Bilel',0,0), Player('Ilyes',0,0) )
redTeam = Team('RED', Player('Aziz',0,0), Player('Molk',0,0) )


# Generate position for first player of first team

x = rd.randint(0,N-1)
y = rd.randint(0,M-1)

blueTeam.p1.x = x
blueTeam.p1.y = y

# Generate position for first player of second team

while (x == blueTeam.p1.x and y == blueTeam.p1.y):
    x = rd.randint(0,N-1)
    y = rd.randint(0,M-1)

redTeam.p1.x = x
redTeam.p1.y = y

# Generate position for second player of first team

while ((x == blueTeam.p1.x and y == blueTeam.p1.y) or (x == redTeam.p1.x and y == redTeam.p1.y)):
    x = rd.randint(0,N-1)
    y = rd.randint(0,M-1)

blueTeam.p2.x = x
blueTeam.p2.y = y

# Generate position for second player of second team

while ((x == blueTeam.p1.x and y == blueTeam.p1.y) or (x == redTeam.p1.x and y == redTeam.p1.y) or (x == blueTeam.p2.x and y == blueTeam.p2.y)):
    x = rd.randint(0,N-1)
    y = rd.randint(0,M-1)

redTeam.p2.x = x
redTeam.p2.y = y



blueTeam.p1.move(1,'NONE',matrix)
blueTeam.p2.move(1,'NONE',matrix)

redTeam.p1.move(2,'NONE',matrix)
redTeam.p2.move(2,'NONE',matrix)


# Print dimensions and positions

matrix.info()
blueTeam.info()
redTeam.info()


# Game Loop:

i=0

while (i < 4*N*M):
    # The Agents scripts must code one single function called move:
    # move (grid, M, N, x, y)
    # With grid: the raw matrix (not the class)
    # M,N: matrix's dimensions
    # x,y: the current position of the player
    # move() must return a move string: "UP", "DOWN", "RIGHT", "LEFT", "NONE"
    blueTeam.p1.move(1,Ag1.move(matrix.grid,M,N,blueTeam.p1.x,blueTeam.p1.y),matrix)
    redTeam.p2.move(1,Ag3.move(matrix.grid,M,N,redTeam.p1.x,redTeam.p1.y),matrix)
    blueTeam.p1.move(1,Ag2.move(matrix.grid,M,N,blueTeam.p2.x,blueTeam.p2.y),matrix)
    redTeam.p2.move(1,Ag4.move(matrix.grid,M,N,redTeam.p2.x,redTeam.p2.y),matrix)
    matrix.update()
    matrix.info()
