import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)
my_screen = Screen()
# Color list extracted from hirst.jpg
clrlst = [(191, 165, 116), (139, 166, 189),
          (59, 101, 137), (138, 90, 53), (13, 23, 53), (221, 206, 125), (60, 23, 12), (181, 146, 165), (178, 152, 47),
          (142, 176, 150), (74, 116, 82), (61, 15, 26), (124, 80, 101), (16, 38, 25), (127, 32, 18), (25, 52, 124),
          (178, 188, 215), (110, 34, 48), (162, 106, 135), (98, 149, 102), (96, 122, 172), (209, 180, 195),
          (171, 106, 95), (172, 205, 181), (77, 148, 163), (26, 89, 64)]

aseem = Turtle()
aseem.speed(0)

y = 0
aseem.penup()
aseem.hideturtle()
aseem.setpos(-150, y)   #So that the dots start from the left corner
for i in range(10):
    aseem.setpos(-150, y)   #So that the dots start from the left corner
    for j in range(10):
        aseem.pendown()
        aseem.dot(20, random.choice(clrlst))    #Randomly choosing a color from the list
        aseem.penup()   #So that the turtle doesn't draw a line while moving
        aseem.forward(40)   #Moving the turtle forward
    y = y + 40

my_screen.exitonclick()
