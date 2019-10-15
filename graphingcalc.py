# This program makes a graphing calculator
# CS 2420 section2
# Fall, 2019

from graphics import *
from math import *

def main():
    points = []
    XLOW = -15
    YLOW = -15
    XHIGH = 15
    YHIGH = 15
    XINC = .01

    infix = input("Enter an equation")
    postfix = infixToPostfix(infix)

    x = XLOW
    while x<=XHIGH:
        y = evaluatePostfix(postfix, x) # Your function here!
        points.append( [x,y] )
        x += XINC


    win = GraphWin("My Circle", 500, 500)
    win.setCoords(XLOW, YLOW, XHIGH, YHIGH)
    for i in range(len(points)-1):
        l = Line(Point(points[i][0],points[i][1]), Point(points[i+1][0],points[i+1][1]))
        l.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

class Stack:
    def __init__ (self):
        self.mStack = []

    def push(self, item):
        self.mStack.append(item)

    def pop(self):
        return self.mStack.pop()

    def getStackLength(self):
        return len(self.mStack)

    def topOfStack(self):
        if len(self.mStack) > 0:
            return self.mStack[len(self.mStack)-1]

def infixToPostfix(infix):
    postfix = ""
    myStack = Stack()
    for c in infix:
        if c in "0123456789x":
            postfix += c
        elif c in ")":
            while myStack.topOfStack() != "(":
                stackItem = myStack.pop()
                postfix += stackItem
            myStack.pop()
            
        elif c in "+-":
            if myStack.getStackLength() > 0:
                if myStack.topOfStack() in "*/":
                    while myStack.topOfStack() != "(" and myStack.getStackLength() > 0:
                        stackItem = myStack.pop()
                        postfix += stackItem
            myStack.push(c)
            
        elif c in "*/":
            if myStack.getStackLength() > 0:
                while myStack.getStackLength() > 0 and myStack.topOfStack() in "*/":
                    stackItem = myStack.pop()
                    postfix += stackItem
            myStack.push(c)
            
        elif c in "(":
            myStack.push(c)

    while myStack.getStackLength() > 0:
        stackItem = myStack.pop()
        postfix += stackItem

    return postfix

def evaluatePostfix(postfix, x):
    myStack = Stack()
    
    for c in postfix:
        if c in "0123456789":
            myStack.push(c)
        elif c == "+":
            rhs = myStack.pop()
            lhs = myStack.pop()
            v = float(lhs) + float(rhs)
            myStack.push(v)
        elif c == "-":
            rhs = myStack.pop()
            lhs = myStack.pop()
            v = float(lhs) - float(rhs)
            myStack.push(v)
        elif c == "*":
            rhs = myStack.pop()
            lhs = myStack.pop()
            v = float(lhs) * float(rhs)
            myStack.push(v)
        elif c == "/":
            rhs = myStack.pop()
            lhs = myStack.pop()
            v = float(lhs) / float(rhs)
            myStack.push(v)
        elif c == "x":
            myStack.push(x)

    result = myStack.pop()
    return result


main()
