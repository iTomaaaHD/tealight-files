from tealight.logo import move, turn

def drawgrid(gridlength):
  for i in range(0,4):
    move(gridlength)
    turn(90)
    move(gridlength)
  
def drawsquares(squareslength):
  move(10)
  turn(-90)
  move(100)

drawgrid(100)