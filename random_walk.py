from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
n=int(input("enter how many steps:"))
directions=[0,90,180,270]
for i in range(n):
  tim.pensize(15)
  tim.color(random.choice(colours))
  tim.forward(30)
  tim.speed("fast")
  tim.setheading(random.choice(directions))

screen.exitonclick()
  
