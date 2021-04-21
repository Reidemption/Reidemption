from graphics import *

class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        if self.stack == []:
            return True
        return False
        
    def pop(self):
        if self.empty() == True:
            return False
        return self.stack.pop()

    def push(self, x):
        self.stack.append(x)

    def top(self):
        if self.empty() != True:
            x = self.stack[-1]
            return x
        return False


def InfixtoPostfix(infix):
    stack = Stack()
    postfix = ""
    for char in infix:
        if char >= '0' and char <= '9':
            postfix += char
        elif char == 'x':
            postfix += char
        else:
            if char in "(":
                stack.push(char)
            elif char in ")":
                operator = stack.pop()
                while operator != "(":
                    postfix += operator
                    operator = stack.pop()
            else:
                if char in "+-":
                    while not stack.empty() and stack.top() in "+-*/":
                        postfix += stack.pop()
                    stack.push(char)
                elif char in "*/":
                    while not stack.empty() and stack.top() in "*/":
                        postfix += stack.pop()
                    stack.push(char)

    #pop everything off the stack and move into postfix
    while not stack.empty():
        postfix += stack.pop()
    return postfix


def EvaluatePostFix(postfix, x):
    stack = Stack()
    for char in postfix:
        if char >= '0' and char <= '9':
            stack.push(float(char))
        elif char == 'x':
            stack.push(x)
        elif char == '+':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs + rhs
            stack.push(result)
        elif char == '-':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs - rhs
            stack.push(result)
        elif char == '*':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs * rhs
            stack.push(result)
        elif char == '/':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs / rhs
            stack.push(result)
    return stack.pop()

def PrintDirections():
    print("IMPORTANT: DO NOT INCLUDE SPACES")
    print("Enter any formula of single digit integers. Feel free to include 'x' as a variable")

def main():
    #Let user enter function
    PrintDirections()
    infix = input("Enter your function: ")
    infix.strip()
    postfix = InfixtoPostfix(infix)

    #Generate points to draw
    points = []
    xlow = -10
    ylow = -10
    xhigh = 10
    yhigh = 10
    xincrement = .1
    x = xlow
    epsilon = 0.0001
    while x < xhigh + epsilon:
        y = EvaluatePostFix(postfix, x)
        # y = x*x
        points.append([x,y])
        x += xincrement

    #Draw said points

    win = GraphWin("My Function", 500, 500)
    win.setCoords(xlow,ylow, xhigh,yhigh)
    #lx = Line(Point((-500,0),(500,0))
    #ly = Line(Point(0,500),(0,-500))

    #lx.draw(win)
    #ly.draw(win)
    for i in range(len(points)-1):
        #c = Circle(Point(points[i][0],points[i][1]), .1)
        #c.draw(win)
        l = Line(Point(points[i][0], points[i][1]),
                Point(points[i+1][0], points[i+1][1]))

        l.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()