'''
draw spiral using recursion concept
'''

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, linelen):
	if linelen > 0:
		myTurtle.forward(linelen)
		myTurtle.right(90)
		drawSpiral(myTurtle, linelen-5)

drawSpiral(myTurtle, 100)
myWin.exitonclick()



