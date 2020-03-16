class State:
    edges = []

    label = None

    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label


class Fragment:

    start = None
    accept = None

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


def shunt(infix):
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
                postfix.append(OperatorStack.pop())

                OperatorStack.append(c)

            else:
                postfix.append(c)

    while OperatorStack:
        postfix.append(OperatorStack.pop())

    return ''.join(postfix)


def regex_compile(inflix):
    postfix = shunt(inflix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        c = postfix.pop()
        if c == '.':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            frag2.accept.edges.append(frag1.start)
            newFrag = Fragment(frag2.start, frag1.accept)

        elif c == '|':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            accept = State()
            Start = State(edges=[frag2.start, frag1.start])
            frag2.edges.append(accept)
            frag1.edges.append(accept)
            newFrag = Fragment(start, accept)

        elif c == '*':
            frag = nfa_stack.pop()
            accept = State()
            Start = State(edges[frag.start, accept])
            frag.accept.edges = ([frag.start, accept])
            newFrag = Fragment(start, accept)

        else:
            accept = State()
            Start = State(label=c, edges=[accept])
            newFrag = Fragment(Start, accept)

        nfa_stack.append(newFrag)

    return nfa_stack.pop()


def match(regex, s):

    nfa = regex_compile(regex)

    return nfa

    print(match("a.b|b*", "bbbbbbbbb"))
    
