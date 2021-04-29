import turtle
import random
import time
screen=turtle.Screen()
trtl=turtle.Turtle()
screen.setup(420,320)
screen.title('Diverging Turtle made by Saksham Aggarwal')
screen.bgcolor('yellow')
trtl.shape('turtle')
trtl.color('darkgoldenrod','black')
s=10
trtl.penup()
trtl.setpos(30,30)
for i in range(120):
        s=s+1
        trtl.stamp()
        trtl.forward(s)
        trtl.right(25)
        time.sleep(0.10)      #activated with a break of a 1/10th of a second
        
trtl.write('Like, Share, Subscribe',font=("Arial", 40, "normal"))
