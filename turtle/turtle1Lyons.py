import turtle
import time

# creating first object
turtle.speed(1)
turtle.hideturtle()
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.goto(50,50)
turtle.goto(0,0)
turtle.goto(50,-50)
turtle.goto(100,0)
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.goto(-50,50)
turtle.goto(0,0)
turtle.goto(-50,-50)
turtle.goto(-100,0)


time.sleep(2)
turtle.reset()



turtle.done()
