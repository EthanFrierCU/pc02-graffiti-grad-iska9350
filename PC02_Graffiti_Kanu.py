"""
Code Review of Isha Kanu PC02
https://github.com/ATLS1300/pc02-graffiti-grad-iska9350/blob/master/PC02_Graffiti_Kanu.py
Author: Ethan Frier
ATLS 1300-5650
10.05.20
A turtle drawing over Jeff Bezos' face - creates a red stop sign with exclimation point, draws devil horns on his head and an X over his face. He is Mr. Steal Yo Money

Summary review:
This project is a great example turtle graffiti. Isha fulfilled all the requirements of the assignment and used their turtle efficiently to draw comprehensive graphics, and some classic school notebook style doodles on his face.
In order to improve upon this project, I added a for loop to draw the stop sign, and added two turtles named warning and bezos for graphics and doodling respectively. I also reorganized the variables and made edits to the order and categorization of the turtle drawing commands. 
I really liked the drawing here, and especially thought that Isha used the basic turtle commands extremely successfully to make both overlaid graphics and drawings relational to the image. My edits were mostly organizational, in order to strengthen the backend so that Isha or other collaborators can continue to build on their creation. 
"""

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Isha Kanu
September 09, 2020
'''

from turtle import *                # import turtle

colormode(255)                      # set colormode to 0-255

# variables
w = 750                             # width of panel
h = 750                             # height of panel
octogon = 50                        # length of octogon sides
style = ('Courier', 30, 'italic')   # triple to store font information used in write() in the draw text block

# create a panel of size w,h with a color background behind gif of Bezos
panel = Screen()                    # create a panel to draw on. 
panel.setup(width=w, height=h)      # set panel size to w and h variables
panel.bgcolor("lightsteelblue1")    # set panel background color to light steel blue
image = "Bezos.gif"                 # import bezos.gif
panel.bgpic(image)

# create two turtles - one for graphics and one for bezos
warning = Turtle()                  # added this turtle to draw the graphics and text
bezos = Turtle()                    # added this turtle to draw on Jeff's face
warning.up()                        # moved pen up commands so that every block ends and begins with turtles up
bezos.up()

# warning turtle settings for stop sign
warning.goto(250,100)               # goto local origin for octogon
warning.color("red")
warning.down()
warning.begin_fill()

# for loop draws octogon 
for side in range(8):               # range is 9 to leave turtle at the proper orientation for next step
    warning.forward(octogon)        # draw forward by octogon size variable
    warning.right(45)               # turn right 45 degrees
warning.end_fill()
warning.up()

# warning turtle settings for exclamation point
warning.goto(265,85)                # goto local origin for exclamation point rectangle
warning.pensize(3)                  
warning.color("yellow","black")     # set the stroke to yellow and fill to black

# draw rectangle
warning.down()                      # moved to before begin_fill
warning.begin_fill()
warning.forward(20)                  
warning.right(90)
warning.forward(75)
warning.right(90)
warning.forward(20)
warning.right(90)
warning.forward(75)
warning.right(90)
warning.up()

# draw circle
warning.goto(275,-15)               # goto local origin for exclamation point circle - adjusted
warning.down()
warning.circle(8)                   
warning.end_fill()                  # end the shape and fill both rectange and circle
warning.up()

# bezos turtle settings for devil horns
bezos.goto(30,200)                  # goto local origin for first devil horn
bezos.pensize(4)
bezos.color(255,0,0)                # removed redundant int() data type constructor

# draw right horn
bezos.down()                        # moved to before begin_fill
bezos.begin_fill()
bezos.setheading(100)
bezos.forward(30)
bezos.setheading(225)
bezos.forward(20)
bezos.goto(30,200)
bezos.up()

#draw left horn
bezos.goto(-45,220)                 # goto local origin for second devil horn
bezos.down()
bezos.setheading(140)
bezos.forward(30)
bezos.setheading(265)
bezos.forward(40)
bezos.goto(-45,220)
bezos.end_fill()
bezos.up()                          # moved to after end_fill


# bezos turtle settings for X
bezos.goto(-110,220)                # goto local origin for X
bezos.color("black")                # moved to settings block
bezos.pensize(10)                   # moved to settings block

# draw X
bezos.down()
bezos.setheading(315)
bezos.forward(275)
bezos.up()
bezos.goto(100,220)
bezos.down()
bezos.setheading(225)
bezos.forward(275)
bezos.hideturtle()                  # hide bezos trutle, thanks for your service

# warning turtle draw text
warning.up()
warning.goto(-300,-200)             # goto local origin for text
warning.color('gold')               # moved to before pen down
warning.down()
warning.write("# Mr. Steal Yo' Money!", font=style, align='left')
warning.hideturtle()                # hide warning turtle

done()
