from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 150

width = 10
height = 4

for i in range(0,height):
  for j in range(0,width):
    if j % 2.5 == 0:
      image(x + j * 60 , y + i * 60, "misc/YellowFlower.png")
    else:
      image(x + j * 60 , y + i * 60, "misc/Clover.png")
     
