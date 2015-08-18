from tealight.logo import move, turn

gridsize = 160
squaresize = 20

def drawgrid(gridsize):
  for i in range(0,4):
    move(gridsize)
    turn(90)
  
def vertical_lines(squaresize):
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
    
def horizontal_lines(squaresize):
  for i in range(0,4):
    move(squaresize)
    turn(90)
    move(gridsize)
    turn(-90)
    move(squaresize)
    turn(-90)
    move(gridsize)
    turn(90)
    
def fillingvertically():
  turn(90)
  move(1)
  turn(-90)
  move(squaresize)
  turn(90)
  move(1)
  turn(90)
  move(squaresize)
  
  

drawgrid(gridsize)
vertical_lines(squaresize)

turn(-90)
move(gridsize)
turn(90)

horizontal_lines(squaresize)
turn(180)
move(gridsize)
turn(180)

