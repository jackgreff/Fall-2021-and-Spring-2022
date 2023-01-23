<h1 style="text-align: center;">Lab 1: ProPublica Investigates Computational Recidivism, Part 1</h1>
<h3 style="text-align: center;">Haverford CS 106 - Introduction to Data Structures</h3>
<h3 style="text-align: center;">Due: 2/10/22</h3>


# Overview

In this lab, you will design a class to encapsulate one entry from the
COMPAS scores dataset, as well as write a handful of methods to prepare
for reading and processing the COMPAS dataset next lab.

COMPAS is an algorithm designed by Northpointe that tries to predict the
likelihood that a criminal defendant will reoffend in the future, or in
other words, their likelihood of recidivism. [Propublica's analysis of
COMPAS](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) found that it's predictions were not only unreliable, but also
consistently discriminated against black defendants. The data you will be working was
with complied by Propublica, a nonprofit investigative journalism organization. It's base is the anonymous records of 7,000
people arrested in Broward County, Florida, in 2013 and 2014. Propublica
then ran the original entries through COMPAS to obtain the predicted
recidivism scores, and they also recorded if the defendants were later
arrested for committing another crime (within two years). All of this
was compiled to make up the dataset provided.

Labs 1 and 2 are also meant to emphasize the importance of ethics and
evaluation in computing. As you move forward in computer science, it is
crucial that you recognize your responsibility to think critically
about design decisions you make while coding, because they often directly
affect people. Risk assessment tools like COMPAS are often misused by
judges to determine a defendant's sentence.

This lab is the foundation for Lab 2, where you will later replicate the
Propublica's calculations in the *Prediction Fails Differently for Black
Defendants* chart using ArrayLists.

# Designing the Defendant Class

## Understanding the Data

When designing any class, we first need to understand the
details of the data that we will store and what types of queries we may
want to make about that data.

To understand the data and the larger context, look at these sources in
order:

1.  ProPublica's introductory video: <https://youtu.be/17eDz5HA_qI>

2.  Article: ["Machine Bias\" by Propublica](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)

3.  Handout "Lab 1: Understanding Propublica.pdf\"

4.  Video: ["Context of Risk Assessment
    Tools\"](http://sorelle.friedler.net/riskassessmentsintro.mp4)

5.  Look at the CSV data in "compas-scores.csv\". (You won't use this file in your code this week)

## Creating a `Defendant` Class Representing a Single Row

### 1.  Create the class

- Create a file `Defendant.java` in the `src` folder of this project. There you will write the
  `Defendant` class.
- Think about what a single row in the CSV represents. Create a class that
  holds information about a single row. Be sure to name it meaningfully
  based on your understanding of what the single row represents.

- Using javadoc style, write a comment to describe the class - what it
  represents, what contents it holds, etc.

### 2.  Fields and methods

- Add necessary fields to represent the information about what the class
  represents based on the CSV - think about its columns! Think carefully
  about what the most appropriate data type of these fields should be; __ you
  should include enums__ as a possibility but make sure they are an
  appropriate data type - e.g. you should not make everything be `enum` or
  `String`.

- After you have created the fields, add any necessary getter and setter
  methods to the class.

### 3.  Constructor

- We now need to make the class accept data from outside to initialize the
  fields you created earlier. Make a constructor that takes in an array of Strings
  (e.g. `String[] data`) and initializes the fields of your class. Think strategically
  about how you can convert that array of Strings into the types you need in each field.


# Getting Ready to Replicate the Analysis: Writing Methods

The goal of these two labs is to get ready to replicate ProPublica's analysis
shown in the table *Prediction Fails Differently for Black Defendants*.
In the next lab, you'll do the actual replication. To prepare the necessary classes
appropriately and understand the analysis you'll be working
towards, make sure you have read the article ["Machine
Bias\"](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
by ProPublica and the handout "Lab 1: Understanding Propublica.pdf".

> In order to do this, we need to determine if the person represented by
the row fits the description in the table. For example, to see if
someone is part of the 25.3% in the table, we need to check:
> 1.  if the person is white (or Caucasian)
> 2.  if the person did not re-offend (i.e., was not labeled as being
      >    rearrested within 2 years)
> 3.  if the person was labelled "high risk\"

### 1. Boolean Methods

* More generally, we need to check the person's race (white or Black),
  whether they re-offended, and whether they were labelled "low risk\" or
  "high risk\" of recidivism. __Make these methods__ that return `true` or
  `false` depending on whether a person fits this criteria: `isWhite()`,
  `isBlack()`, `hasReoffended()`, `isLowRisk()`, and `isHighRisk()`.

### 2. `toString()` Method
* If you try to print an object, Java will output the memory address of
  the object. However, this doesn't tell us much and makes it difficult to
  see what the object is like. To make meaningful print statements,
  __override the `toString()` method__ to show some of the fields. You can do
  this by simply creating a method in the class with the precise
  signature: `public String toString()`


# Example Output

The following is an example of a call to your program, and what it could output. Your printed statement does not have to match this exactly, in fact, feel free
to improve on the formatting!

~~~java
String[] data = {"Male", "African-American", "Possession of Cannabis", "8", "High", "0"}
Defendant d = new Defendant(data)
System.out.println(d)
~~~
Output:
```
An African-American male defendant was charged with possession of cannabis. He was assigned a high risk score of 8 and did not later reoffend. 
```


# General Style & Coding Tips

Below are some helpful general tips and style guidelines for all labs:

-   Remember to use Javadoc style conventions while commenting.
    > For reference on Javadoc style, check out [this resource](https://www.tutorialspoint.com/java/java_documentation.htm). Don't worry about tags, just look at the examples at the top. \
    Plus, use [this code example](https://pythontutor.com/java.html#code=/**%0A%20*%20Java%20program%20that%20computes%20the%20sum%20of%20the%20first%20n%20numbers%0A%20*%20%40author%20Jeova%20Farias%0A%20*%20%40version%20January%2013,%202022%0A%20*/%0Apublic%20class%20Main%20%7B%0A%20%20%20%20public%20static%20void%20main%28String%5B%5D%20args%29%20%7B%0A%20%20%20%20%20%20%20%20int%20n%20%3D%2010%3B%0A%20%20%20%20%20%20%20%20int%20result%20%3D%20sumIntegers%28n%29%3B%0A%20%20%20%20%20%20%20%20System.out.println%28result%29%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20/**%0A%20%20%20%20%20*%20Returns%20the%20sum%20of%20the%20first%20n%20integers%0A%20%20%20%20%20*%20%40param%20n%20positive%20integer%20n%0A%20%20%20%20%20*%20%40return%20sum%20of%20the%20first%20n%20integers%0A%20%20%20%20%20*/%0A%20%20%20%20public%20static%20int%20sumIntegers%28int%20n%29%7B%0A%20%20%20%20%20%20%20%20int%20total%20%3D%200%3B%20//%20Set%20up%20a%20variable%20for%20the%20total%0A%20%20%20%20%20%20%20%20for%20%28int%20i%20%3D%200%3B%20i%20%3C%3D%20n%3B%20i%2B%2B%29%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20total%20%2B%3D%20i%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20return%20total%3B%0A%20%20%20%20%7D%0A%7D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=java&rawInputLstJSON=%5B%5D&textReferences=false)
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

