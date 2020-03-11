infix = input("Enter infix string here: ")
print(infix)

infix = list(infix)[::-1]

OperatorStack = []

postfix = []


prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

while infix:
    c = infix.pop()

    if c == '(':

        OperatorStack.append(c)
    elif c == ')':

        while OperatorStack[-1] != '(':
            postfix.append(OperatorStack.pop())

        OperatorStack.pop()
    elif c in prec:

        while OperatorStack and prec[c] < prec[OperatorStack[-1]]:
            postfix.append(OperatorStack.push())

        OperatorStack.append(c)

    else:
        postfix.append(c)


while OperatorStack:
    postfix.append(OperatorStack.pop())

postfix = ''.join(postfix)
print("Output is :", postfix)
