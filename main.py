import colorgram
import random
from turtle import Turtle, Screen

#Setting up the screen and setting the colormode to RGB
screen = Screen()
screen.colormode(255)

#Setting up the Turtle object, hiding it and using penup so that it does not leave trace lines
turtle = Turtle()
turtle.hideturtle()
turtle.penup()

#Declaring initial co-ordinated for turtle so turtle would start from there and setting its speed to fastest
pos_x = -295
pos_y = -250
turtle.teleport(pos_x, pos_y)
turtle.speed("fastest")

#Using colorgram library to extract colors from image.jpg
colors = colorgram.extract("image.jpg", 84)
color_list = []

#Converting the extracted colors to (R,G,B) form and appending that to color_list
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

for i in range(1, 101):                                     #Running for loop till 100
    color = random.choice(color_list)                       #Choosing a random color from our list
    turtle.dot(20, color)                                   #Turtle will draw a dot of size 20 using the extracted color
    turtle.fd(60)                                           #Turtle will move forward 60 paces to draw the next dot

    if i % 10 == 0:                                         #Once 10 dots are drawn
        turtle.setheading(90)                               #Turtle will change its heading to north
        turtle.fd(60)                                       #Turtle will go forward 60 paces
        pos_y += 60                                         #Position y will be incremented by 60
        turtle.teleport(pos_x, pos_y)                       #Turtle will teleport to its new coordinates
        turtle.setheading(0)                                #Turtle will set its heading towards right and start the for loop again

screen.exitonclick()                                        #Screen can exit only when the user presses "X"
