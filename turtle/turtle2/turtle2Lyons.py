# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 9/30/25
# PROGRAM: Turtle 2
# PURPOSE: The goal of this lab is to get used to conditionals
#		   and the random module
# =================================================================

import turtle
import random

WIDTH_BOX = 200
HEIGHT_BOX = 200
TURTLE_DIRECTION = random.randint(0, 359)
TURTLE_DISTANCE = random.randint(1, 200)

# Making turtles breakout box
turtle.color("tan")
turtle.hideturtle()
turtle.begin_fill()
turtle.teleport(100, -100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

# Setting turtle
turtle.showturtle()
turtle.home()
turtle.shape("turtle")
turtle.color("green")
turtle.left(TURTLE_DIRECTION)
turtle.forward(TURTLE_DISTANCE)

# Check position
x, y = turtle.position()

if -100 <=x <=100 and -100 <= y <= 100:
	print("Darn!")
else:
	print("Tiddles escaped!")

turtle.done()
