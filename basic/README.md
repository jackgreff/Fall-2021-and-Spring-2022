<h1 style="text-align: center;">Welcome to Java</h1>
<h3 style="text-align: center;">Haverford CS 106 - Introduction to Data Structures</h3>
<h3 style="text-align: center;">Lab 0 (one week)</h3>


# Overview 

This lab is designed to ease you into Java syntax by having you
implement a series of simple functions. The goal is for you to get some practice with loops, enums, classes, and writing well-commented code.


# A Basic Class

In order to make any Java program, you need to make a class. As you saw
in the Hello World Tutorial, the most basic class you can make has only
the single `public static void main` method.

In this lab, we'll practice Java syntax by making some `public` `static`
methods. Some of these may be familiar to you from CS 105. However, you
must solve these **without** recursion!

You should test the methods by calling the methods from the `main`
method. Be sure to write clear and complete comments for all the
methods.


1.  Make a method `power(x,exp)` that takes a given number `x` and
    returns the number raised to a given power `exp`. Think carefully
    about the data type of the parameters. You may assume that
    `exp`$\geq 0$ and that `exp` is an integer.

2.  Make a method `GCD` that takes two positive integers and returns the
    greatest common denominator using this algorithm from Euclid:

    > Given two positive integers, keep replacing whichever number is
    > larger by the remainder of the larger divided by the smaller. When
    > you get a remainder of zero, the other number is the GCD.

3.  Make a method `isPrime` that takes a nonnegative integer and returns
    `true` if it's prime and `false` otherwise.

4.  Make a method `round` that takes a double floating point number and
    returns the number rounded to the nearest integer. You may *not* use
    a library to do this for you: you should only use basic arithmetic
    operations and the usual program statements.

5.  Create a public `enum` called `Standing` with following constants:
    `FIRST_YEAR, SOPHOMORE, JUNIOR, SENIOR`. For consistency with the
    autograder, ensure that this `enum` is a member of the `Main` class.

    Make a method `classYear` that takes a `Standing` and returns the
    information about the class year as a String. The returned String
    should be in format `Class of 20XX`. For example,
    `classYear(Standing.SOPHOMORE)` should return `"Class of 2023"`.  


# Lab 0 Rules

Here are some things to note before you carry out this lab:

-   Do **not** use recursion! Doing so will result in penalization.

-   Do **not** create additional classes - *for this lab*, you should
    only work with `Main.java`.

-   Think carefully about the data types you are using (e.g. `int`,
    `double`, etc). Do not make assumptions unless specified in the
    instructions.



# General Style & Coding Tips

Below are some helpful general tips and style guidelines for all labs:

-   Remember to use Javadoc style conventions while commenting.
    > For reference on Javadoc style, check out [this resource](https://www.tutorialspoint.com/java/java_documentation.htm). Don't worry about tags, just look at the examples at the top. \
    > Plus, use [this code example](https://pythontutor.com/java.html#code=/**%0A%20*%20Java%20program%20that%20computes%20the%20sum%20of%20the%20first%20n%20numbers%0A%20*%20%40author%20Jeova%20Farias%0A%20*%20%40version%20January%2013,%202022%0A%20*/%0Apublic%20class%20Main%20%7B%0A%20%20%20%20public%20static%20void%20main%28String%5B%5D%20args%29%20%7B%0A%20%20%20%20%20%20%20%20int%20n%20%3D%2010%3B%0A%20%20%20%20%20%20%20%20int%20result%20%3D%20sumIntegers%28n%29%3B%0A%20%20%20%20%20%20%20%20System.out.println%28result%29%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20/**%0A%20%20%20%20%20*%20Returns%20the%20sum%20of%20the%20first%20n%20integers%0A%20%20%20%20%20*%20%40param%20n%20positive%20integer%20n%0A%20%20%20%20%20*%20%40return%20sum%20of%20the%20first%20n%20integers%0A%20%20%20%20%20*/%0A%20%20%20%20public%20static%20int%20sumIntegers%28int%20n%29%7B%0A%20%20%20%20%20%20%20%20int%20total%20%3D%200%3B%20//%20Set%20up%20a%20variable%20for%20the%20total%0A%20%20%20%20%20%20%20%20for%20%28int%20i%20%3D%200%3B%20i%20%3C%3D%20n%3B%20i%2B%2B%29%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20total%20%2B%3D%20i%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20return%20total%3B%0A%20%20%20%20%7D%0A%7D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=java&rawInputLstJSON=%5B%5D&textReferences=false)
     from class as a reference for what your style should look like.

-   Write your variables in camelCase, and be sure to indent properly.

-   Don't forget to add comments! Include...
    > - A document header (name, date, program description)
    > - Comments at the top of each function describing what the
    >   function does
    > - Comments within the functions as needed, to describe 
    >   non-obvious steps \

-   When working on larger programs, test as you go! That is, write
    a little bit of code, then make sure it works before building on it.

-   Focus on correctness rather than efficiency.

