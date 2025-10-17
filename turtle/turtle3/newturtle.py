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
	turtle.pencolor("brown")
	turtle.left(90)
	turtle.forward(BOX_WIDTH)
turtle.end_fill()

turtle.penup()
turtle.home()
turtle.showturtle()
turtle.shape("turtle")
turtle.pendown()

x, y = turtle.pos()

for i in TURTLE_COLOR:
	turtle.color(i)
	turtle.setheading(random.randrange(TURTLE_DIRECTION))
	turtle.forward(random.randrange(TURTLE_DISTANCE))

	x, y = turtle.pos()

	if -100 <= x <= 100 and -100 <= y <= 100:	
		turtle.write("Darn!")
	else:
		turtle.write("Tiddles escaped!")	

turtle.done()
