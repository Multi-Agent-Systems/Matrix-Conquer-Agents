#TEAM BLUE : 1
import random as rd 


def move (grid, M, N, x, y):
    p = rd.random()

    pLeft = 1/2*(x/(M-1))
    pRight = 0.5 - pLeft
    pUp = 0.5 + 1/2*(y/(N-1))
    pDown = 1.5 - pUp

    if (p<0.5):
        if (p<pLeft):
            return "LEFT"
        else:
            return "RIGHT"
    elif (p>0.5):
        if (p<pUp):
            return "UP"
        else:
            return "DOWN"
    else:
        return "NONE"