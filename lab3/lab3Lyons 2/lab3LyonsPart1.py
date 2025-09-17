# =================================================================
# AUTHOR: Brantley Lyons
# DATE: 9/17/25
# PROGRAM: Programming Lab 3, Part 1
# PURPOSE: Draw a square in the center of the screen using the
#          turtle module.
# =================================================================
import turtle  # we need to input turtle first

# show the turtle
turtle.showturtle()

turtle.penup()       # pick the turtle up (don't draw)

turtle.forward(100)  # move forward to where we want to start

turtle.pendown()     # put the turtle down (draw)

# draw a square in the center of the screen
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)  # changed to 200
turtle.right(90)
turtle.forward(200)
turtle.right(90)  # need to specify the angle
turtle.forward(100)

# Prevent the turtle from automatically closing after finishing
turtle.done()
