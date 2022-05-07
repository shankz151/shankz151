from turtle import *
setup ()
chutiya = Turtle()
colors = ["red","blue","green","yellow","purple","orange",]
import random 
chutiya.up()
chutiya.goto(-200,0)
chutiya.down()
chutiya.width(5)

chutiya.speed(0)
for i in range(9001):
    colorchoice=random.choice(colors)
    chutiya.color(colorchoice)
    chutiya.forward(400)
    chutiya.right(181)

