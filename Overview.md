# `Graph Theory Project Overview`
Explanation of Project work for the Graph Theory Project

## `Introduction`
For this project we were tasked with writing a program in python to execute regular expressions on strings using an algorithm known as Thompson's Contruction.
Using this algorithm we build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.
In my repository it includes on python file called GraphTheoryProject.py this includes the code for the main project. There is also another file that takes in a two txt files and compares them using the algorithm. These are located in the folder called PythonFiles. There is Research document included in the Repository, this shows the research I did for the project. In the main python file there is a command line included if you require help with the project, I will go into detail about this command line further on. There is also various tests I used in the main project file. I will explain these tests in the "Test" section.

## `Run`

### Download Project
* To run this code first you need to download it.<br> 
* To do this create a folder on your computer. 
* Go to the command line and cd into the folder just created for example "cd Desktop/FolderName". 
* Once this is done use the command "Git clone url" the url should be given on the frontpage of the repository. 
* If this is done succesfully the project should be downloaded in the file you just created.
* To Run the Python file you need to have Python 3 installed on your machine. <br>
  If you don't have Python installed follow the steps shown here.

### Installing Python
 
* To install Python navigate to the page https://www.python.org/ .<br>
* Once on this page go to the download section. <br>
* Choose version e.g Windows, Linux <br>
* Once the installer is downloaded run and wait for it to be installed. <br>

### Running the Programme
* Once Pyton is installed cd into Python files.<br>
* Run the command Python GraphTheoryProject.py .This will run the programme.<br>
* Next you should see an option to continue or quit. <br>
* Type 1 to continue or 2 to quit.<br>
* Enter in a Regular expression e.g "b?" <br>
* Next, enter in a string to compare eg "b" <br>
* Result should be as shown <br>
![Sample Input](Images/Input.PNG)


If you want to use the commands line use the following Python GraphTheoryProject.py --help  . <br>
This will display help if you require. As shown here.<br>
<br>
![Command Line](Images/CommandLinePNG.PNG)

## `Test`
* In the menu you will see an option to run tests.
* Type 3 to run the test.
* If there is an error in the test it will display saying which test had the error.
* If all tests pass you will see a message saying "Tests finished with zero erros"
* You will then return to the menu <br>
  These tests were made using Python assert. <br>
  Assert is used for debugging that tests a condition , if the condition is true the project continues as normal <br>
  If the the value is false it ouputs the error.<br>
  These are the following tests included with the project
  ```python 
     tests = [
            ["b*","bbbbbbbbb",  True],
            ["b+" , "b" , True],
            ["b+" ,"  " , False],
            ["b?","b" , True],
            ["b.b|b","b",  True]
        ]
        ```
  
  
  
## `Algorithm`
### Shunting-yard Algorithm
  This algorithm is used for changing the expression from infix to postfix notation. (Also known as Reverse Polish Notation)
  Invented by Edsger Dijkstra <br>
  This is achieved by doing the following steps
* Firstly we take in a regular expression
* We then put it into a list and using the following code [::-1] we reverse the list
* Once the list if reversed we pass it through a while loop to decide what do with, taking in account of the precedence.

```python
infix = list(infix)[::-1] 

    OperatorStack  = [] 

    postfix = [] 
    prec = {     #operator precedence
    '*': 100,
    '+': 95,
    '?': 90,
    '.': 80, 
    '|': 60,
    ')': 40, 
    '(': 20}
   ``` 
    
    
* In the project we create a Operator Stack.
* Depending on the characters we add or pop from the stack until we are left with the expression in postfix notation.

We use the following code to achive this


 ```python
 while infix:   
        c = infix.pop()
        if c == '(':   
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
```
### Thompson's Contruction Algorithm









## `References`
   GMIT lecture videos <br>
   These videos were used to help construct the project.
 
   Regular expression cheat sheet https://www.debuggex.com/cheatsheet/regex/python <br>
   I used this cheat sheet to understand the values of special characters like the ? and + <br>
   
   Python https://www.python.org/<br>
   Python was the language we were required to make the project with
   
   


## `Author`
Thomas Kenny

