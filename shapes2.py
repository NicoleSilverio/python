from turtle import *
import math

# Name your Turtle.
tommy = Turtle()

# Set Up your screen and starting position.
tommy.penup()
setup(500,300)
x_pos = 1
y_pos = 70
tommy.setposition(x_pos, y_pos)
person = input('enter number of sides: ')
color = input('enter color: ')
steps= input('how many steps?:')


### Write your code below:
def shape(steps, angle, speed):
    tommy.pendown()
    tommy.pencolor(color)
    tommy.speed(speed)

    tommy.begin_fill()
    tommy.fillcolor(color)
    for b in range(int(person)):
        tommy.forward(int(steps))
        tommy.right(angle)
    tommy.end_fill()


shape(steps, 360/int(person), 208)







# Close window on click.
exitonclick()
