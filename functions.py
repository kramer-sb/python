# done in turtle

import turtle

turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def triangle(size):
  for i in range(3):
	turtle.forward(size)
	turtle.left(120)
	
triangle(175)
back(50)
triangle(150)
back(110)
triangle(55)
