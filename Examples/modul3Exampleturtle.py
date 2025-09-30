import turtle

# Named constants
SCREEN_WIDTH = 600 # screen width
SCREEN_HEIGHT = 600 # screen height
TARGET_LLEFT_X = 100 # targets lower-left x
TARGET_LLEFT_Y = 250 # targets lower-left y
TARGET_WIDTH = 25 # width of the target
FORCE_FACTOR = 30 # arbitrary
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# setup turtle
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# draw target
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# center the turtle
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# get angle and force from the user
angle = float(input("Enter the projectile angle: "))
force = float(input("Enter the launch force(1-10): "))

# calculate the distance
distance = force * FORCE_FACTOR

# set the heading
turtle.setheading(angle)

# launch the projectile
turtle.pendown()
turtle.forward(distance)

# did we hit the target?
if (TARGET_LLEFT_X <=turtle.xcor() <=(TARGET_LLEFT_X + TARGET_WIDTH) and
   TARGET_LLEFT_Y <=turtle.ycor() <=(TARGET_LLEFT_Y + TARGET_WIDTH)):
	print("yes")
else:
	print("no")


turtle.done()
