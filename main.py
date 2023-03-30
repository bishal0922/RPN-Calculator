#!/usr/bin/python3

"""
Bishal Giri
1001934305
Lab 03
"""

OPERATORS = ['+', '-', '*', '/']

def main():
    #valid operators
    
    #open input.txt file
    input_file = open("INPUT.txt", "r")
    
    #read input.txt file
    lines = input_file.readlines()
    
    for line in lines:
        #pass it to our function
        print(RPN(line))
    
    input_file.close()   
    
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
        #if the element is a number
        else:
            #push it to the stack
            stack.append(int(i))
    
    #return the last element of the stack
    return stack.pop()
    
if __name__ == "__main__":
    main()