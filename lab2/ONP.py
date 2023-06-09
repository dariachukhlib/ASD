from stack import Stack 

def evaluatePostfixExpression(expression):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '^': lambda x, y: x ** y}
    stack = Stack()
    for symbol in expression.split():
        if symbol.isdigit():
            stack.push(float(symbol))
        elif symbol in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[symbol](operand1, operand2)
                stack.push(result)
        elif symbol == '=' and stack.size()==1:
             return stack.peek()
    return  "Error!!! Check your expression"
    
s1 = "2 5 2 + *  = "
print(evaluatePostfixExpression(s1))



