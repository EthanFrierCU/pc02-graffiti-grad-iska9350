#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Isha Kanu
September 09, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
#Red Hexagon shape
up()
goto(250,100)
down()
color("red")
begin_fill()
forward(50)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(50)
end_fill()

# Black Warning Sign
up()
goto(265,85)
down()
pensize(3)
color("yellow","black")
begin_fill()
right(135)
forward(75)
left(90)
forward(20)
left(90)
forward(75)
left(90)
forward(20)
up()
goto(275,5)
down()
circle(8)
end_fill()

# Devil Ears
up()
goto(30,200)
down()
color(int(255),int(0),int(0))
begin_fill()
pensize(4)
setheading(100)
forward(30)
setheading(225)
forward(20)
goto(30,200)
up()
goto(-45,220)
down()
setheading(140)
forward(30)
setheading(265)
forward(40)
goto(-45,220)
end_fill()

# X on face
color("black")
up()
goto(-110,220)
down()
pensize(10)
setheading(315)
forward(275)
up()
goto(100,220)
down()
setheading(225)
forward(275)

#Words
up()
goto(-300,-200)
down()
color('gold')
style = ('Courier', 30, 'italic')
write("# Mr. Steal Yo' Money!", font=style, align='left')

hideturtle()
done()