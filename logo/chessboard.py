from tealight.logo import move, turn

def draw(gridlength):
  move(gridlength)
  turn(90)
  move(gridlength)

draw(200)