from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
direction = -1
turn(1)
for i in range(0,4):
  while touch() == "fruit":
    move()
  turn(-1)
for i in range(0,7):
  for i in range(0,4):
    move()
  turn(direction)
  direction = -direction
  for i in range(0,30):
    move()
  turn(direction)
  
for i in range(0,3):
  move()
turn(direction)
  
  
  #direction = -direction
  #for i in range(0,30):
  #  move()
  #turn(1)
  #for i in range(0,4):
  #  move()
  #turn(1)
  #for i in range(0,30):
  #  move()
  #turn(-1)
#for i in range(0,4):
  #move()
#turn(-1)
#for i in range(0,30):
  #move()