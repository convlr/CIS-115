import turtle
import random

TURTLE_COLOR = ["red", "orange", "yellow", "green", "blue"]
BOX_WIDTH = 200
BOX_HEIGHT = 200
TURTLE_DIRECTION = random.randint(0, 359)
TURTLE_DISTANCE = random.randint(1, 100)

turtle.color("tan")
turtle.hideturtle()
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()

turtle.begin_fill()
for _ in range(4):
	turtle.left(90)
	turtle.forward(BOX_WIDTH)
turtle.end_fill()

turtle.home()
turtle.showturtle()
turtle.shape("turtle")

x, y = turtle.position()
newloop = 0

while newloop < 5:
	turtle.color(random.choice(TURTLE_COLOR))
	turtle.setheading(TURTLE_DIRECTION)
	turtle.forward(TURTLE_DISTANCE)
	newloop += 1
	if -100 <= x <= 100 and -100 <= y <= 100:
		turtle.write("Darn!")
		turtle.color(random.choice(TURTLE_COLOR))
		turtle.setheading(TURTLE_DIRECTION)
		turtle.forward(TURTLE_DISTANCE)
	else:
		turtle.write("Tiddles did not escape!")
#for i in range(5):
#
#	newposition = turtle.position()
#	turtle.color(random.choice(TURTLE_COLOR))
#	turtle.setheading(TURTLE_DIRECTION)
#	turtle.forward(TURTLE_DISTANCE)
#
#	x, y = newposition
#
#	if -100 <= x <= 100 and -100 <= y <= 100:
#		turtle.write("Darn!")
#        turtle.color(random.choice(TURTLE_COLOR))
#        turtle.setheading(TURTLE_DIRECTION)
#        turtle.forward(TURTLE_DISTANCE)
#
#	else:
turtle.done()
