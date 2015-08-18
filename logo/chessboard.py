from tealight.logo import move, turn

def drawgrid(gridlength):
  for i in range(0,4):
    move(gridlength)
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

drawgrid(100)
verticalsquares(10)

