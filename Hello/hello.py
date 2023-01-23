"""

This file will ask you to explore the basics of strings and functions in Python.

It presumes that you're familiar with Python's DocTest system; if not, see the arithemetic.py file.

It also presumes that your instructor has explained to you that "string" is the term for
the way that Python (or other computer software) records text information, and that
the quotation marks, either " style or ' style, are used to indicate the start and end
of the string. Note that, no matter which style of quotation you use, Python will try
to show you the result with the ' marks as long as that wouldn't create ambiguity with,
for example, the use of an apostrophe in the string itself.

>>> 'This is a Python string, entered with the apostrophes (often called single-quotes)'
'This is a Python string, entered with the apostrophes (often called single-quotes)'

>>> "This string was entered with regular (double) quotes, but the expected answer part will have single-quotes"
'This string was entered with regular (double) quotes, but the expected answer part will have single-quotes'

>>> "It's strange that Python has two kinds of quotes. Can you guess why?"
"It's strange that Python has two kinds of quotes. Can you guess why?"

>>> "If you want to see the string without the quotes, use the print function."
'If you want to see the string without the quotes, use the print function.'

>>> print("If you want to see the string without the quotes, use the print function.")
If you want to see the string without the quotes, use the print function.



Fix this example, and the function below, to give your preferred name:

>>> print(myPreferredName())
Jack Greff
>>> print(myPreferredPronouns())
He/Him/His

>>> print(Optional())
I'm from New York


Add a function myPreferredPronouns, to give a string showing your preferred pronouns, and add an example here:



Optionally, add a third function to tell us anything else you'd like us to know about you.

"""

def myPreferredName() -> str:
    return "Jack Greff"


def myPreferredPronouns() -> str:
    return "He/Him/His"

def Optional() -> str:
    return "I'm from New York"



#############################################################################################
# The following gets the DocTest system to check test cases in the documentation comments.  #
# In this course, you won't need to modify the stuff below, or even understand the details. #
#############################################################################################

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all "+str(result[1])+" tests"))
    else:
        print("Rats!")
