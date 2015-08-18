from tealight.logo import move, turn

gridsize = 160
squaresize = 20

def drawgrid(gridsize):
  for i in range(0,4):
    move(gridsize)
    turn(90)
  
def verticalsquares(squaresize):
  for i in range(0,4):
    turn(90)
    move(squaresize)
    turn(-90)
    move(gridsize)
    turn(90)
    move(squaresize)
    turn(90)
    move(gridsize)
    turn(180)
    
def horizontalsquares(squaresize):
  for i in range(0,4):
    move(squaresize)
    turn(90)
    move(gridsize)
    turn(-90)
    move(squaresize)
    turn(-90)
    move(gridsize)
    turn(90)
  

drawgrid(gridsize)
verticalsquares(squaresize)

turn(-90)
move(gridsize)
turn(90)

horizontalsquares(squaresize)

