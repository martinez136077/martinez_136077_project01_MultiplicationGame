# martinez_136077_project01_MultiplicationGame
# This program helps children 
# multiply numbers by two

from graphics import *

def main():
    win = GraphWin("Multiplication Game", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Draw the interface
    Text(Point(1,3), "   Enter number to multiply by 2:").draw(win)
    Text(Point(1,1), "Total:").draw(win)
    inputText = Entry(Point(2.25,3), 5)
    inputText.setText("0")
    inputText.draw(win)
    outputText = Text(Point(2.25,1),"")
    outputText.draw(win)
    button = Text(Point(1.5,2.0),"Multiply")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # convert input
    fortwo = int(inputText.getText())
    total = fortwo * 2

    # display output and change button
    outputText.setText(round(total,2))
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()
    
main()
