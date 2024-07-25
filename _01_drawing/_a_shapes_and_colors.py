import turtle
from turtle import Turtle

window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
swimmings: Turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
swimmings.shape('turtle')
# Set your turtle's speed using .speed(2)
swimmings.speed(5)
# Set your turtle's color using .color('green') and .pencolor('blue')
swimmings.color('blue')
# Move your turtle forward using .forward(100)
swimmings.forward(100)
# TEST    Did your turtle move forward?
# Move your turtle left or right using .left(90) or .right(90)
swimmings.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
for i in range(4):
    swimmings.forward(100)
    swimmings.left(90)
# TEST    Did your turtle draw a square?
# Move your turtle to a new place on the screen using .goto(x, y)
swimmings.goto(100, 0)
# x=0 and y=0 is the center of the screen
swimmings.begin_fill()
# Have your turtle draw a circle using .circle(radius, steps=30)
swimmings.circle(25, steps=30)
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
swimmings.end_fill()
# Draw 3 more shapes with different fill colors!
swimmings.color('green')
swimmings.begin_fill()
for i in range(4):
    swimmings.forward(180)
    swimmings.right(90)
swimmings.end_fill()
swimmings.color('purple')
swimmings.begin_fill()
swimmings.left(90)
swimmings.forward(200)
swimmings.left(45)
swimmings.left(100)
swimmings.forward(50)
swimmings.left(100)
swimmings.end_fill()

swimmings.color('red')
swimmings.begin_fill()
swimmings.forward(400)
swimmings.left(135)
swimmings.forward(400)
swimmings.left(90)
swimmings.forward(400)
swimmings.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
