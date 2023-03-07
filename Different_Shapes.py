import turtle as t
import random
tim = t.Turtle()

sides=3
istrue=True
colors=["midnight blue","red","yellow","medium violet red","pale violet red"]
while(istrue):
  tim.color(random.choice(colors))
  for i in range(int(sides)):
    angle=360/sides
    
    tim.forward(100)
    tim.left(angle)
  if(sides==9):
    istrue=False
  sides=sides+1

