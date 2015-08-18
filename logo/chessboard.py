from tealight.logo import move, turn

def drawgrid(gridlength):
  for i in range(0,4):
    move(gridlength)
    turn(90)
  
def drawsquares(squareslength):
  for i in range(0,5):
    turn(90)
    move(squareslength)
    turn(-90)
    move(100)
    turn(90)
    move(squareslength)
    turn(90)
    move(100)
    turn(180)

drawgrid(100)
drawsquares(10)