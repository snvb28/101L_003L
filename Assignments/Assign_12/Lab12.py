########################################################################
##
## CS 101 Lab
## Program #12
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating a program that draws select shapes using classes.
##
## ALGORITHM:
##      1. Import the turtle module.
##      2. Create super class named 'Point' with __init__, draw, and draw_action methods.
##      3. Create 'Box' subclass with __init__ and draw_action methods.
##      4. Create 'Box_Filled' subclass with __init__ and draw_action methods.
##      5. Create 'Circle' subclass with __init__ and draw_action methods.
##      6. Create 'Circle_Filled' subclass with __init__ and draw_action methods.
##
## ERROR HANDLING:
##          No error handling present.
##
## OTHER COMMENTS:
##          Main function created to display shapes for result images.
##
########################################################################

import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()


class Box(Point):

    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)


class Box_Filled(Box):

    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()


class Circle(Point):

    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)


class Circle_Filled(Circle):

    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


def main():
    b = Box_Filled(-200, 70, 100, 200, 'red', 'blue')
    b.draw()
    c = Circle_Filled(200, -70, 100, 'blue', 'red')
    c.draw()

main()
   