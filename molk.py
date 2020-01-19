import random
tmp=0
method=0
cycles=0
def test(num_meth,M, N, x, y):
    if num_meth==1:
        return(x+3<M and y+3<N)
    elif num_meth==2:
        return(x-3>M and y+3<N)
    elif num_meth==3:
         return(x+3<M and y-3>N)
    else:
        return(x-3>M and y-3>N)

def move(grid, M, N, x, y):
    global tmp
    global method
    global cycles
    if (tmp==0):
        method=random.randint(1,4)
        while(test(method,M, N, x, y)):
            method=method=random.randint(1,4)
    tmp+=1
    if tmp==12:
        cycles+=1   
    if method==1:
        if 1<=tmp<=3:
            return("RIGHT")
        elif 4<=tmp<=6:
            return("DOWN")
        elif 7<=tmp<=9:
            if tmp==9 and cycles>0:
                tmp=0
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
            if tmp==9 and cycles>0:
                tmp=0
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
            if tmp==9 and cycles>0:
                tmp=0
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
            if tmp==9 and cycles>0:
                tmp=0
            return("RIGHT")
        elif 10<=tmp<=12:
            if tmp==12:
                tmp=0
            return("DOWN") 