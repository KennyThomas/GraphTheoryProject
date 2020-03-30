# `Graph Theory Project`
Execute regular expressions on strings using an algorithm known as Thompson’s construction

## `Deployment`
Open up the folder in the directory of the .py file.<br>
Run Python GraphTheoryProject.py<br>
Enter in a regular expression for example " a.b|b* " <br>
Next enter in a string to compare for example "bbbbbb"<br>
Result will either be true or false


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
   Regular expression cheat sheet https://www.debuggex.com/cheatsheet/regex/python <br>
   Python https://www.python.org/<br>
   
   


## `Author`
Thomas Kenny
