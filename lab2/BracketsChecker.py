from stack import Stack 

def checkBraccets(inputString):
    stack = Stack()
    index = 0
    error = True
    while (index < len(inputString)) and error:
        symbol = inputString[index]

        if symbol == "(" or symbol == "{" or symbol == "[":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                error = False
            elif  symbol ==")" and stack.peek() == "(":
                stack.pop()
            elif  symbol =="}" and stack.peek() == "{":
                stack.pop()
            elif  symbol =="]" and stack.peek() == "[":
                stack.pop()
        index += 1
    if error and stack.isEmpty():
        return True
    else:
        return False


print(checkBraccets("(()()()())")) #true
print(checkBraccets("(((()()(0)))")) #false
print(checkBraccets("{[]{()()([])()()}}")) #true
print(checkBraccets("{()([)[[](])}()}")) #false   
