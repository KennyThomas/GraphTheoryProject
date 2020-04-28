import argparse

class State:
  def __init__(self, label=None, edges=None):
    self.edges = edges if edges else []
    self.label = label


class Fragment:

    start = None #start state of the nfa fragment
    accept = None #accept state of te nfa fragment

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


def shunt(infix):   # Shunting algorithm  -- turns infix to postfix
    infix = list(infix)[::-1] # reverse the list

    OperatorStack  = [] # operator stack created

    postfix = [] # postfix stack created
    prec = {     #operator precedence
    '*': 100,
    '+': 95,
    '?': 90,
    '.': 80, 
    '|': 60,
    ')': 40, 
    '(': 20}

    while infix:   #loop through the input
        c = infix.pop()

        if c == '(':   #decide what to do depending on the character
            OperatorStack.append(c)
        elif c == ')':
            while OperatorStack [-1] != '(':
                postfix.append(OperatorStack.pop())
            OperatorStack .pop()
        elif c in prec:
            while OperatorStack  and prec[c] < prec[OperatorStack [-1]]:
                postfix.append(OperatorStack.pop())
            OperatorStack .append(c)
        else:
            postfix.append(c)
    while OperatorStack :
        postfix.append(OperatorStack.pop())

    return ''.join(postfix)


def compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1] # reverse the list

    nfa_stack = []   #nfa stack created

    while postfix:
        c = postfix.pop() # pop a character from postfix
        if c == '.':      #any character accepted
            frag1 = nfa_stack.pop()   #create two fragments
            frag2 = nfa_stack.pop()
            frag2.accept.edges.append(frag1.start)
            newfrag = Fragment(frag2.start, frag1.accept) #create new instance of fragment to represent the nfa
            nfa_stack.append(newfrag)




        elif c == '|':    # 0 or 1
            frag1 = nfa_stack.pop() #create two fragements as in can be 0 or 1 
            frag2 = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            frag1.accept.edges.append(accept)
            frag2.accept.edges.append(accept)
            newfrag = Fragment(start, accept) #create new instance of fragment to represent the nfa
            nfa_stack.append(newfrag)




        elif c == '*':    # 0 or more
            frag = nfa_stack.pop()  # one fragment it created
            accept = State()
            start = State(edges=[frag.start, accept])
            frag.accept.edges = ([frag.start, accept])
            newfrag = Fragment(start, accept) #create new instance of fragment to represent the nfa



        
        elif c == '+':  # 1 or more
            frag = nfa_stack.pop() # one fragment created
            frag.accept.edges.append(frag.start)
            newfrag = Fragment(frag.start, frag.accept) #create new instance of fragment to represent the nfa



        elif c == '?':  # 0 or 1
            frag = nfa_stack.pop() # one fragment created
            accept = State()
            start = State(edges=[frag.start, accept])
            frag.accept.edges = ([accept])
            newfrag = Fragment(start, accept) #create new instance of fragment to represent the nfa

         


              
        else:
            accept = State()
            initial = State(label=c, edges=[accept])
            newfrag = Fragment(initial, accept)
        nfa_stack.append(newfrag) #push the new nfa instance of fragment to represent te new nfa

    return nfa_stack.pop()


def followes(state, current):
    if state not in current:
        current.add(state)
        if state.label is None:
            for x in state.edges:
                followes(x, current)





def Menu(self):
    option = input("Enter 1 to continue , 2 to quit , or 3 to run tests  ")

    if option == "1":
        regex = input("Enter regular expression:  ") 
        s = input("Enter String to compare:  ")
        print("Result:")
        print("Your statement is :" , match(regex,s))
        Menu(self=Menu)
    
    elif option == "2":
        exit()

    elif option == "3":
        print("Running Tests please wait..........")
        tests = [
            ["b*","bbbbbbbbb",  True],
            ["b+" , "b" , True],
            ["b+" ,"  " , False],
            ["b?","b" , True],
            ["b.b|b","b",  True]
        ]
        
        for test in tests:
            assert match(test[0],test[1]) == test[2] , test[0] + (" should match " if test[2] else  " should not match ") + test[1]
            
        print("Tests finished with zero errors")
        print("")
        Menu(self=Menu)



def match(regex, s):  # match the regular expression with a string

    nfa = compile(regex)

    current = set()
    followes(nfa.start, current)
    previous = set()
    for c in s:    #loop through characters in s
        previous = current
        current = set()  #create new empty set

        for state in previous:
            if state.label is not None:
                if state.label == c:
                    followes(state.edges[0], current) #add the state at the end of te arrow to current

    return nfa.accept in current    #see if it matches the string 


parser = argparse.ArgumentParser(description='Enter a regular expression and  a String to compare' , prog='GraphTheoryProject')
parser.add_argument('-r', '--regex' , type=str  , metavar='' ,help='A regular expression')
parser.add_argument('-s', '--s', type=str, metavar='' , help='A string to match')
parser.add_argument('--version', '-v',  action='version', version='%(prog)s 2.0')
parser.add_argument('--SampleInput', '-si', help='Provides sample input',  action='version', version='Regular expression = b*  | String = bbbbbb  | Result = True')
parser.add_argument('--info' , '-i', action='version',version='*Thompsons Alogorithm* is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA) , This NFA can be used to match strings against the regular expression.'  ,  help='Information on project')
args = parser.parse_args()

if any(vars(args).values()):
    print("Result:")
    print("Your statement is :" , match(args.regex, args.s))




elif not any(vars(args).values()):
    Menu(self=Menu)

        





       