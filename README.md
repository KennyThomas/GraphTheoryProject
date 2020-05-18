# `Graph Theory Project`
Execute regular expressions on strings using an algorithm known as Thompson’s construction

## `Deployment`
* Open up the folder in the directory of the .py file.
* Run Python GraphTheoryProject.py.
* You will be given an option of using command line arguements e.g --help
* These options are shown in the overview.md file
* These arguements will offer help if the user requires it.<br>
 Or 
* Continue with the project
* You will enter the menu and can choose to run tests to see if it works.
* If you choose to continue follow the following steps.
* Enter in a regular expression for example " a.b|b* " 
* Next enter in a string to compare for example "bbbbbb"
* Result will either be true or false.


## `How it works`
We first take in a regular expression and a string from the user<br>
Using the shunting algorithm we take in a regular expression and convert from infix to postfix.<br>
We create a list out of these characters and reverse the order<br>
Next we will pop characters of this list and create nfa fragments<br>
these fragments will have an accept state and start state
we will add these fragments to a stack
If the following characters "." , "?" , "|" , "+" , "*"*
are contained in the regular expression we will treat it differently as you can see in the code <br>
these characted will have different meanings for examples the "?" will mean 0 or 1 <br>
Once we have our nfa fragments created we can match these with our regular expression <br>
Our output will be displayed either true or false


## `References`
   GMIT lecture videos <br>
   These videos were used to help construct the project.
 
   Regular expression cheat sheet https://www.debuggex.com/cheatsheet/regex/python <br>
   I used this cheat sheet to understand the values of special characters like the ? and + <br>
   
   Argparse https://docs.python.org/3/howto/argparse.html<br>
   I used this tutorial to understand how to implement command line arguements <br> 
   
   Python https://www.python.org/<br>
   Python was the language we were required to make the project with
   
   


## `Author`
Thomas Kenny
