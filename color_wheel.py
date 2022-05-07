from turtle import *
setup ()
tl = Turtle()
colors = ["red","blue","green","yellow","purple","orange",]
import random 
tl.up()
tl.goto(-200,0)
tl.down()
tl.width(5)

tl.speed(0)
for i in range(9001):
    colorchoice=random.choice(colors)
    tl.color(colorchoice)
    tl.forward(400)
    tl.right(181)

