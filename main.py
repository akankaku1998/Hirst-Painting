import turtle as t
import colorgram
import random

dummy = t.Turtle()
dummy.speed("fastest")
dummy.hideturtle()
dummy.penup()
t.colormode(255)

#Extract colors from image
colors_list = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
  colors_list.append(color.rgb)

#Set heading of turtle to the left-most cornor
dummy.setheading(225)
dummy.forward(300)
dummy.setheading(0)

#Print dots
for dots in range(1, 101):
  dummy.dot(15, random.choice(colors_list))
  dummy.forward(45)

  if dots % 10 == 0:
    dummy.setheading(90)
    dummy.forward(45)
    dummy.setheading(180)
    dummy.forward(450)
    dummy.setheading(0)


screen = t.Screen()
screen.exitonclick()