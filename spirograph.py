import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(0,360,5):
  tim.speed("fastest")
  tim.pencolor(random_color())
  tim.circle(100)
  tim.left(5)

