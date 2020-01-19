tmp=0
method=0
def move(grid, M, N, x, y):
    global tmp
    global method
    if ( tmp == 0 and x+3<M and y+3<N and grid[x+1][y]!=2):
        method=1
    elif ( tmp == 0 and x-3>M and y+3<N and grid[x-1][y]!=2):
        method=2
    elif ( tmp == 0 and x+3<M and y-3>N and grid[x][y-1]!=2):
        method=3
    elif ( tmp == 0 and x-3>M and y-3>N and grid[x-1][y]!=2):
        method=4
    tmp+=1   
    if method==1:
        if 1<=tmp<=3:
            return("RIGHT")
        elif 4<=tmp<=6:
            return("DOWN")
        elif 7<=tmp<=9:
            return("LEFT")
        elif 10<=tmp<=12:
            if tmp==12:
                tmp=0
            return("UP") 
    elif method ==2:
        if 1<=tmp<=3:
            return("LEFT")
        elif 4<=tmp<=6:
            return("DOWN")
        elif 7<=tmp<=9:
            return("RIGHT")
        elif 10<=tmp<=12:
            if tmp==12:
                tmp=0
            return("UP") 
    elif method ==3:
        if 1<=tmp<=3:
            return("RIGHT")
        elif 4<=tmp<=6:
            return("UP")
        elif 7<=tmp<=9:
            return("LEFT")
        elif 10<=tmp<=12:
            if tmp==12:
                tmp=0
            return("DOWN") 
    elif method ==4 :
        if 1<=tmp<=3:
            return("LEFT")
        elif 4<=tmp<=6:
            return("UP")
        elif 7<=tmp<=9:
            return("RIGHT")
        elif 10<=tmp<=12:
            if tmp==12:
                tmp=0
            return("DOWN") 