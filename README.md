# RPN - Reverse Polish Notation

Reverse Polish Notation (RPN) is a mathematical notation where the operator is placed after the operands. In other words, in RPN, expressions are written without parentheses and with the operator following the operands.

For example, the infix notation "3 + 4" would be written in RPN as "3 4 +". In this notation, the operator "+" follows the operands "3" and "4".

RPN is also known as postfix notation because the operator comes after the operands.

One of the advantages of RPN is that it eliminates the need for parentheses and operator precedence rules, as the order of evaluation is determined solely by the order of the operands and operators. This can simplify the implementation of mathematical expressions in computer programs.

One way to implement Reverse Polish Notation (RPN) is to use a stack data structure. The algorithm for evaluating an expression in RPN using a stack can be described as follows:

Initialize an empty stack.
Read the input expression from left to right.
For each symbol in the expression:
a. If the symbol is an operand, push it onto the stack.
b. If the symbol is an operator, pop the top two elements from the stack, apply the operator to them, and push the result back onto the stack.
After processing all the symbols, the result of the expression will be the only element left on the stack.

## Code:

<a href="main.py">main.py</a>