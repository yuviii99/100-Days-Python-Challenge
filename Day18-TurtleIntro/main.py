import turtle as t
import random

# Colorgram package is used to extract colors from hirst painting to build our new one!
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst_painting.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

color_list = [(211, 154, 97), (52, 107, 132), (176, 78, 34), (238, 246, 243),
              (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157), (229, 197, 128), (231, 238, 242),
              (190, 88, 109), (55, 38, 19), (11, 51, 65), (44, 168, 125), (197, 122, 141), (50, 125, 120),
              (167, 21, 29), (225, 94, 80), (244, 162, 160), (4, 28, 26), (38, 32, 34), (80, 148, 170), (162, 26, 21),
              (236, 165, 170), (98, 125, 160), (167, 207, 192), (22, 79, 91), (162, 203, 212)]

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


s = t.Screen()
s.exitonclick()
