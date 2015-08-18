from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

turn(1)
for i in range(0,4):
  while touch() =="fruit":
    move()
  turn(-1)

for i in range(0,4):
  move()
turn(-1)
for i in range(0,30):
  move()
turn(1)
for i in range(0,4):
  move()
turn(1)
for i in range(0,30):
  move()
turn(-1)