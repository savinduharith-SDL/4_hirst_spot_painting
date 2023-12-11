import turtle

import colorgram
import turtle as t
from random import choice

#Initialize objs
screen = t.Screen()
pointer = t.Turtle()

#Initialize vars
t.setworldcoordinates(-1, -1, 20, 20)
t.colormode(255)
pointer.penup()

#Get colors from the img
colors = colorgram.extract('hirst_painting.jpg', 30)
color_palette = []
for color in colors:
    rgb = color.rgb
    color_palette.append((rgb.r, rgb.g, rgb.b))

#Drawing a new hirst
for j in range(10):
    for i in range(10):
        pointer.dot(20,choice(color_palette))
        pointer.forward(2)
    pointer.home()
    pointer.left(90)
    for forward_points in range(j+1):
        pointer.forward(2)
    pointer.right(90)
pointer.home()
#Exit logic
screen.exitonclick()