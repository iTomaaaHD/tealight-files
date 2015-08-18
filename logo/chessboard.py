from tealight.logo import move, turn

gridsize = 100
squaresize = 10

def drawgrid(gridsize):
  for i in range(0,4):
    move(gridsize)
    turn(90)
  
def verticalsquares(squaresize):
  for i in range(0,5):
    turn(90)
    move(squaresize)
    turn(-90)
    move(100)
    turn(90)
    move(squaresize)
    turn(90)
    move(100)
    turn(180)
    
def horizontalsquares(squaresize):
  move(squaresize)
  turn(90)
  move(gridsize)
  turn(-90)
  move(squaresize)
  turn(-90)
  move(gridsize)
  

drawgrid(gridsize)
verticalsquares(squaresize)
horizontalsquares(squaresize)

