#code for import colors from image using colorgram
# import colorgram
#
# colors = colorgram.extract("hirst_painting.jpg", 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as t
from random import choice

color_list = [(153, 91, 49), (209, 156, 107), (42, 111, 146), (60, 116, 75), (199, 157, 31), (240, 58, 34),
              (131, 170, 183), (248, 211, 75), (155, 7, 26), (145, 64, 87), (146, 219, 161), (29, 178, 108),
              (188, 132, 139), (253, 232, 0), (125, 181, 123), (23, 55, 82), (222, 49, 52), (193, 234, 198),
              (46, 151, 194), (17, 90, 59), (250, 147, 138), (3, 78, 45), (250, 146, 159), (218, 231, 237),
              (192, 26, 13), (245, 229, 232), (3, 82, 118), (81, 71, 41), (46, 62, 86)]

screen = t.Screen()
pen = t.Turtle()
screen.colormode(255)


def random_color():
    color = choice(color_list)
    return color


def h_painting():
    pen.hideturtle()
    pen.up()
    pen.setpos(-200, -200)
    pen.speed(0)
    for _ in range(10):
        for _ in range(10):
            pen.dot(20, random_color())
            pen.up()
            pen.setx(pen.xcor()+50)
        pen.up()
        pen.setx(-200)
        pen.sety(pen.ycor()+50)


def h_painting_v2():
    pen.hideturtle()
    pen.up()
    pen.speed(0)
    pen.seth(225)
    pen.fd(350)
    pen.seth(0)
    for i in range(1, 101):
        pen.dot(20, random_color())
        pen.fd(50)
        if i % 10 == 0:
            pen.seth(90)
            pen.fd(50)
            pen.seth(180)
            pen.fd(500)
            pen.seth(0)


h_painting_v2()
screen.exitonclick()




