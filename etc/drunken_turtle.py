import turtle
import random

turtle.shape('turtle')
while True:
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(10,50))
    turtle.stamp()
