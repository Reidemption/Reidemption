#infix to postfix algorith
#WILL BE ASKED HOW TO DO THIS ON FINAL
"""
infix 3*x
postfix 3x*

infix 3*4 + 5
postfix 34*5+

infix 3+4*5
postfix 345*+

infix (3+4)*5
postfix 34+5*

infix 3+4*5-6/7
#you need a stack
for char in infix:              *       /
    if digit:                   +       -
        char+postfix          stack   stack
    if operator:
        push on stack
#if operand isn't greater than the one on the top of the stack
#the operand is popped off the stack
postfix 345*+67/-

infix 3-(x+2*(4*x/7)-8)*9
postfix 3x24x
stack: - ( + * ( *

    postfix 3x24x*7
    stack - ( + * ( /
    when we get to the RIGHT PARAM, everything until the corresponding LEFT PARAM pops off

        postfix 3x24x*7/
        stack - ( + *

            postfix 3x24x*7/*+8-9
            stack - * 

                postfix 3x24x*7/*+8-9*-
                stack
"""


"""
Evaluate postfix
#uses a stack but puts the digits on the stack, not the operators

infix 3*x
postfix 3x*

we will loop through x(starting at -10, going to 10)
def EvaluatePostFix(postfix,x):
    #loop through every char in postfix
    if char is number:
        convert from string 3 to number 3 on the stack
        push whatever x is onto the stack
        first pop goes to the right, second to the left
        find the result and put it back into the stack
        then pop off the result and return in

infix 3*4 + 5
postfix 34*5+
3 push
stack: 3
4 push
stack: 3 4
pop 4
pop 3 
multiply 3*4
push result
stack: 12
5 push
stack: 12 5
pop 12
pop 5
add 12+5
push result (17)

"""

"""
postfix: 75+38*/
pop both 5 and 7
add both and then push the 12
pop 8 and 3 and multiply them
stack: 12 24
pop off the 12 and 24
.5 final answer
"""

def InfixtoPostfix(infix):
    stack = MyStack()
    postfix = ""
    for char in infix:
    #for c = infix:
        if char >= '0' and c<= '9':
            postfix += char
        elif char == 'x':
            postfix += char
        elif char in "+-":
            while not stack.empty() and stack.top() in "+-*/":
                postfix += stack.pop()
        elif char in "*/":
            while not stack.empty() and stack.top() in "*/":
                postfix += stack.pop()
        #add section for left PARAM
        elif char in ")":
            while not stack.empty() and stack.top():
            stack.push(char)
    #pop everything off the stack and move into postfix

def EvaluatePostFix(postfix, x):
    stack = MyStack()
    for char in postfix:
        if char >= '0' and c<= '9':
            stack.push(float(char))
        elif char == 'x':
            stack.push(x)
        elif c == '+':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs + rhs
            stack.push(result)
        elif c == '-':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs - rhs
            stack.push(result)
        elif c == '*':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs * rhs
            stack.push(result)
        elif c == '/':
            rhs = stack.pop()
            lhs = stack.pop()
            result = lhs / rhs
            stack.push(result)
    return stack.pop()
