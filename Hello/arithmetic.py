"""
It is important to test computer software before relying on it for anything important,
and to demonstrate the basic usage of a software component that we're going to use.

The DocTest system of the Python language lets you combine both of these activities
by providing one set of examples that serve as "documentation" for the software,
and then DocTest tests this documentation to confirm that it really does what is expected.

To make this system work, we'll start our python program with a multi-line entry that
begins with three quotation marks (as on the very first line above), and ends with
the same mark (we won't include it in this paragraph, because that would end the
multi-line entry here, and we want to demonstrate some more). This multi-line entry
contains a set of documenting examples, each with a specific format.

Each example begins with a line beginning with ">>> " (don't type the quotes,
but the space is important); on that first line of the example, after the ">>> ",
we show one way to _use_ a software component (below, we use + to find 2+2).
After the line showing the use, we write one or more lines giving the answer we expect
(4, in the case of 2+2), and then a blank line to indicate the end of the example.

Putting that all together, to demonstrate the use of "+" in Python, we could write this:

>>> 2+2
4

The first line, ">>> 2+2", is an example of how we could use the + symbol, for example, to add 2 and 2.
The second line, "4", has the example we expect.
The blank line after that indicates that there isn't any more to the answer, after the 4
(without that blank line, the DocTest system would think that 2+2 should produce 4 and then
all of this text).

We could similarly demonstrate multiplication, like this:

>>> 2*2
4

The DocTest system will notice that that's another documenting example, since it is inside
this initial entry surrounded by triple-quotes, and begins with ">>> ".

However, our demonstration of + and * isn't very good. So far, they seem to do the same thing!
A good set of documentation examples will illustrate a variety of uses of different software tools,
including showing how they differ. So, for + and *, we might show some more, as we do below
(after the DocTest self-quiz, which is marked with the lines of #### marks so you can find it).


First, though, some important details about DocTest:

 1. To actually perform the test, and check the documenting examples, we include some
    specific lines after the initial triple-quoted entry, and then just run the file as a
    Python program (e.g., by hitting the "run" button if we're using an integrated
    development environment such as PyCharm). At that point, the DocTest system will print
    out messages about any situtations in which the actual result doesn't match the expected
    answer we gave.

    You can see these specific DocTest lines at the end of this file, if you like; they're
    after the lines starting with "#" marks, down at the end of the file. But, you can also
    just ignore those lines, since they're already part of the file, and you shouldn't ever
    need to modify them in this course.

 2. The "expected answer" part must be written in the way Python will show it for us, which
    is usually the simplest way we could have entered the value into a Python program.
    You'll learn more about entering things into Python later, but, for now, just note that
    if you do something silly like writing one-half as "0.50000" rather than "0.5", DocTest
    will treat that as an incorrect example.

 3. The examples can be intermixed with text, as needed, to document/demonstrate the
    software. Anything that isn't between the ">>> " mark and the next blank line will be
    ignored during the testing. But, if you don't have a blank line after the test,
    sometimes the next bit of documentation can be mistaken for the test.



That's all the details you'll need to know about DocTest, for now. Here's a little quiz,
to see if you've mastered the details above, and then we'll get back to a better set of
documenting examples for + and *, just to make a few points about writing documentation.


######## The self-quiz on DocTest begins here. #########

These documenting examples of + and * contain several errors.
Try to guess how many errors there are, and run the program to check your guess.
Then, try to correct all the errors, and run the program again to see if you did.

Let's add 3 and 5, and see what we get:

>>> 3+5
8

Now, let's add one quarter (0.25) to three and a quarter, and see if we get three and a half:

>>> 0.25+3.25
3.5

Finally, let's check to 1+2 and 2+1:

>>> 1+2
3

>>> 2+1
3

########  The self-quiz on DocTest ends here.  #########


Now, back to writing our full set of documenting examples. This probably won't tell
you much about adding and multiplying, since you hopefully already know about them,
but it will illustrate some points about sets of examples. Remember that the point
of these examples is to illustrate whatever points you think are important about the
software you're demonstrating, and that you should demonstrate them for someone who
might not already know about the software.

A complete set of examples that gives a good illustration of the relevant features is
sometimes referred to as an "example sweep". So, let's try to provide an example sweep
that illustrates some important (if, hopefully familiar) ideas about + and *.



Note that addition and multiplication often give different results:

>>> 3+4
7

>>> 3*4
12


And, addition and multiplication are both "commutative"; in other words,
switching the left and right doesn't matter, and the examples below give
the same answers as the examples above.

>>> 4+3
7

>>> 4*3
12


Also, for big positive numbers, multiplication produces bigger results than addition:

>>> 17*11
187

>>> 17+11
28


We can add or multiply more than two numbers, of course:

>>> 2*3*4
24

>>> 2+3+4
9


And, the two operations can be combined on one line, in which case
the products (results of *) are added, rather than multiplying the sums:

>>> 2*3+4*5
26

Note that 26 this is the sum 2*3 and 4*5, not the product of 2, the sum of 3 and 4, and 5:

>>> 6+20
26

>>> 2+7+5
14

"""

# If we had written some Python software ourselves, it would usually go here.


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
