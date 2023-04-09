#!/usr/bin/python3

"""
This is for the EXTRA CREDIT PORTION OF THE ASSIGNMENT
Added Modulo Operator! (%)
"""

OPERATORS = ['+', '-', '*', '/', "%"]

def main():
    #valid operators
    
    #open input.txt file
    input_file = open("input_RPN_EC.txt", "r")
    
    #read input.txt file
    lines = input_file.readlines()
    
    for line in lines:
        #pass it to our function
        print(RPN(line))
    
    input_file.close()   


def alg_To_RPN(line):
    order = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }
    
    output, stack = [], []

    #splitting the line to get a list of expressions
    line = line.split()

    for i in line:
        if i.isdigit():
            output.append(i)
        elif i in order.keys():
            while stack and stack[-1] ! 
    pass
    
def RPN(line):
    #split the line
    line = line.split()
    #create a stack
    stack = []
    
    #loop through the line
    for i in line:
        #if the element is an operator
        if i in OPERATORS:
            #pop the last two elements
            a = stack.pop()
            b = stack.pop()
            #perform the operation
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a / b)
            elif i == '%':
                stack.append(a % b)
        #if the element is a number
        else:
            #push it to the stack
            stack.append(int(i))
    
    #return the last element of the stack
    return stack.pop()
    
if __name__ == "__main__":
    main()


