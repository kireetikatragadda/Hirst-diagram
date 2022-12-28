import turtle as turtle_module
import random

turtle_module.colormode(255 )



tim = turtle_module.Turtle()
tim.setheading(225)

tim.penup()
tim.forward(250)
tim.pendown()
tim.setheading(0)

color_list = [(238, 234, 228), (238, 231, 236), (232, 234, 240), (229, 239, 234), (202, 160, 103), (208, 165, 22), (122, 183, 206), (154, 57, 94), (222, 205, 111), (147, 29, 51), (11, 20, 47), (18, 106, 158), (47, 14, 25), (186, 156, 172), (52, 19, 15), (48, 120, 69), (167, 67, 45), (9, 29, 21), (65, 164, 94), (110, 180, 161), (148, 30, 24), (210, 178, 200), (191, 101, 96), (161, 206, 211), (178, 100, 117), (32, 40, 102), (238, 200, 7), (12, 105, 52), (162, 207, 198), (220, 177, 171)]




def move():
    for i in range(10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

def turn_left():
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.pendown()

def turn_right():
    tim.right(90)
    tim.penup()
    tim.forward(50)
    tim.right(90)
    tim.forward(50)
    tim.pendown()

for i in range(5):
    move()
    turn_left()
    move()
    turn_right()

screen = turtle_module.Screen()
screen.exitonclick()