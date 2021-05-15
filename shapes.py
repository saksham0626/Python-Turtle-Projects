# Shapes

import turtle
import time
t = turtle.Turtle()


#star
#t.speed(6)
t.color("red", "blue")
t.begin_fill()
for i in range(8):
    t.forward(200)
    t.left(135)
t.end_fill()
time.sleep(2)
t.clear()


#square
t.color("green", "yellow")
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()
time.sleep(2)
t.clear()



# double square
t.color("pink", "green")
t.begin_fill()
for i in range(4):
    t.forward(90)
    t.right(90)
t.penup()
t.forward(150)
t.pendown()

for i in range(4):
    t.backward(90)
    t.right(90)
t.end_fill()
time.sleep(2)


