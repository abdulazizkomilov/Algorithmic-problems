tokens1 = ["4", "13", "5", "/", "+"]
# output: 6

tokens2 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# output: 22

tokens3 = ["2", "1", "+", "3", "*"]
# output: 9


def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = int(num1 / num2)
            stack.append(result)
    return stack[0]

print(evalRPN(tokens1))

print(evalRPN(tokens2))

print(evalRPN(tokens3))
