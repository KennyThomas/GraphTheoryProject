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

    OperatorStack  = []

    postfix = []
    prec = {
    '*': 100, 
    '.': 80, 
    '|': 60,
    '+': 50,
    '?': 45,
    ')': 40, 
    '(': 20}

    while infix:
        c = infix.pop()

        if c == '(':
            OperatorStack .append(c)
        elif c == ')':
            while OperatorStack [-1] != '(':
                postfix.append(OperatorStack .pop())
            OperatorStack .pop()
        elif c in prec:
            while OperatorStack  and prec[c] < prec[OperatorStack [-1]]:
                postfix.append(OperatorStack .pop())
            OperatorStack .append(c)
        else:
            postfix.append(c)
    while OperatorStack :
        postfix.append(OperatorStack .pop())

    return ''.join(postfix)


def compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        c = postfix.pop()
        if c == '.':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            frag2.accept.edges.append(frag1.start)
            newfrag = Fragment(frag2.start, frag1.accept)
            nfa_stack.append(newfrag)
        elif c == '|':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            frag1.accept.edges.append(accept)
            frag2.accept.edges.append(accept)
            newfrag = Fragment(start, accept)
            nfa_stack.append(newfrag)
        elif c == '*':
            frag = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag.start, accept])
            frag.accept.edge = ([frag.start, accept])
            newfrag = Fragment(start, accept)
        
        elif c == '+':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            frag2.accept.edges.append(frag1.start)
            newfrag = Fragment(frag2.start, frag1.accept)
            nfa_stack.append(newfrag)
        
        elif c == '?':
            frag = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag.start, accept])
            frag.accept.edge = ([frag.start, accept])
            newfrag = Fragment(start, accept)

        else:
            accept = State()
            initial = State(label=c, edges=[accept])
            newfrag = Fragment(initial, accept)
        nfa_stack.append(newfrag)

    return nfa_stack.pop()


def followes(state, current):
    if state not in current:
        current.add(state)
        if state.label is None:
            for x in state.edges:
                followes(x, current)


def match(regex, s):

    nfa = compile(regex)

    current = set()
    followes(nfa.start, current)
    previous = set()
    for c in s:
        previous = current
        current = set()

        for state in previous:
            if state.label is not None:
                if state.label == c:
                    followes(state.edges[0], current)

    return nfa.accept in current



regex = input("Enter regular expression:  ")
s = input("Enter String to compare:  ")

print("Your statement is :" , match(regex, s))
