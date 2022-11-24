import turtle
import time

screen = turtle.Screen()
t = turtle.Pen()
t.pensize(20)
t.pencolor("green")
t.ht()
screen.bgpic("images\cat.gif")

# time.sleep(5)
t.st()
# change screen background color
# screen.bgcolor("orange")
t.shape("turtle")

t.goto(0, 0)
time.sleep(3)
# t.speed("slowest")
t.speed(1)
t.forward(100)


time.sleep(2)

# t.clear()
t.reset()

# input()
# alternative:
screen.exitonclick()
