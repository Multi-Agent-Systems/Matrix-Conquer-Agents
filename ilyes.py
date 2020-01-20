

def move(m,h,w,x,y):
  
  import numpy as np
  
  m= np.asarray(m)

  up=True
  down=True
  left=True
  right=True

  if (y==0 ):
    left=False
  elif(m[x][y-1]==2 or m[x][y-1]==1):
    left=False   
    
  if (y==w-1 ):
    right=False
  elif(m[x][y+1]==2 or m[x][y+1]==1):
    right=False
    
  if (x==0 ):
    up=False
  elif(or m[x-1][y]==2 or m[x-1][y]==1):
    up=False

  if (x==h-1 ):
    down=False
  elif(m[x+1][y]==2 or m[x+1][y]==1):
    down=False

  up_nbr=0
  if (up):
    up_mat=m[0:x,:]
    for i in up_mat :
      for j in i :
        if j==0:
          up_nbr+=1

  down_nbr=0
  if (down):
    down_mat=m[x+1:h,:]
    for i in down_mat :
      for j in i :
        if j==0:
          down_nbr+=1

  left_nbr=0
  if (left):
    left_mat=m[:,0:y]
    for i in left_mat :
      for j in i :
        if j==0:
          left_nbr+=1

  right_nbr=0
  if (right):
    right_mat=m[:,y+1:w]
    for i in right_mat :
      for j in i :
        if j==0:
          right_nbr+=1

  #print("right",right_nbr)
  #print(right_mat)

  #print("left",left_nbr)
  #print(left_mat)

  #print("up",up_nbr)
  #print(up_mat)

  #print("down",down_nbr)
  #print(down_mat)

  maxi= max(right_nbr,left_nbr,up_nbr,down_nbr)

  
    
    
  elif (maxi==right_nbr):
    return("RIGHT")
  elif(maxi==left_nbr):
    return("LEFT")
  elif(maxi==up_nbr):
    return("UP")
  else:
    return("DOWN")
