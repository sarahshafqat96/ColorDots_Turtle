from turtle import Turtle, Screen
import random

screen = Screen()                                       #Creating a screen object

turtle = Turtle()                                       #Creating a turtle object
turtle.hideturtle()                                     #Hide the turtle
turtle.speed("fastest")                                 #Turtle's speed should be fastest

colors = ["red", "blue", "green", "orange", "purple", "black", "yellow", "pink", "teal", "plum"]

for i in range(100):                                    #Starting a for loop
    turtle.circle(100)                                  #Turtle will make a circle of radius 100
    turtle.color(random.choice(colors))                 #The circle will be of a random color from  the colors list declared above
    current_heading = turtle.heading()                  #Current heading variable will store turtle's heading as of now
    new_heading = current_heading + 10                  #Add 10 to that heading
    turtle.setheading(new_heading)                      #Set turtle's new heading to that heading
    turtle.circle(100)                                  #Turtle will draw a new circle at that heading

screen.exitonclick()                                    #Screen will exit when user presses "X"
