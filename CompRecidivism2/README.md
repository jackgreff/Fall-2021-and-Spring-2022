<h1 style="text-align: center;">Lab 2: ProPublica, Part 2</h1>
<h3 style="text-align: center;">Haverford CS 106 - Introduction to Data Structures</h3>
<h3 style="text-align: center;">Due: Thursday, Feb. 17th at 11:59pm </h3>


# Overview

There are two main components to this lab:

1. Creating a class that encapsulates the entirety of the COMPAS recidivism scores dataset using 
ArrayLists and your class from Lab 1.
2. Writing methods to analyze the data from your ArrayList of Defendants and replicate the table
in *Prediction Fails Differently for Black Defendants* from the ProPublica article.

For a more detailed overview of the dataset and Propublica's articles,
see Lab 1's Overview and "Lab 1: Understanding Propublica".

**OBS 1**: This lab requires you to use your `Defendant` class from lab 1. If you were unable 
to finish that class, or would like a correct version, reach out to your TAs or the instructor,
and they will help you!

**OBS 2**: This lab requires the use of ArrayLists in Java. You can 
find a quick tutorial on it [here](https://www.w3schools.com/java/java_arraylist.asp).

**OBS 3**: Make sure to read the file "Lab1_Understanding Propublica.pdf" from Lab 1 to understand the statics
you will be computing in this lab.

# Classes to be Implemented

In Lab 1, you created a ``Defendant`` class to store a single row of the dataset. In this lab, 
you will create a class to store the full dataset and compute some statistics on it called 
``DefendantsData``, and a ``Main`` class to run both classes. 

You are provided with a class ``PropublicaDataTable`` that you **don't need to alter**. You'll use it to 
print your final table in the right format. Also, don't forget to add the `Defendant` class
you created in Lab 1 to this project (you can simply add a new class file in it and copy/past the contents of Defendant.java in it).

## 1. `DefendantsData` class

> _Task_: Create a class called `DefendantsData`
that will represent the entire data set (not just one
row).
### 1.1. Fields
Make a field in your dataset class that holds
an ArrayList, and make sure the datatype of the ArrayList is the object
type you created in the last lab. Also make fields for the statistics required to compute 
the final table in our analysis (see "Lab1_Understanding Propublica.pdf" for more details).

### 1.2. Constructor

Should receive an ArrayList of the rows (which are `String[]`) of the COMPAS.csv and use it to 
initialize the ArrayList of defendants.

### 1.3. Methods
You should add two methods to this class:
1. `readData()`: It reads the ArrayList of defendants and computes the required statistics from the data.
2. `printTable()`: It uses those statistics to print the table via an object of the class `PropublicaDataTable` 
(provided to you in this Lab).

These methods should be called in the Main file via an instance of the `DefendantsData` class. You don't need to create 
getters and setters for this class.

## 2. ``Main`` Class
> _Task_: Create a `main` method that reads the CSV file, instantiate a `DefendantsData` class and runs the analysis.

In this main class you are only required to write its main method. It should read the "compas-scores.csv" file into an ArrayList
of `String[]` (more on it in the following section) and use it to create an instance of `DefendantsData`. Then you should use that instance to run your analysis.
### About the OpenCSV library

OpenCSV is a library that allows you to read in data. You can read in
data from "compas-scores.csv" using the below code. You'll also need to
add the appropriate imports (which IntelliJ ). We will use OpenCSV's `CSVReaderHeaderAware` for this lab.
Because we are using `HeaderAware` reader, it understands that the first
row is the "header" and does not include it in the data. The following code demonstrates how you should use 
it to read the data from "compas-scores.csv":

```Java
CSVReaderHeaderAware reader = new CSVReaderHeaderAware(new FileReader("compas-scores.csv"));
ArrayList<String[]> myEntries = new ArrayList<String[]>(reader.readAll());
reader.close();
```

This will give you an ArrayList (called `myEntries`), where each index is a
String array holding the row data. The indices in the String array
correspond to the column indices. For example, the following is a
visualiazation `myEntries`:

```
{"Male", "Other", "F", ...},                 // row 1
{"Male", "African-American", "F", ...},      // row 2
.
.
.
```
# Output
Now that you have the data read into your data structure, we can
reproduce the analysis ProPublica shows in their chart "Prediction Fails
Differently for Black Defendants." Therefore, when you run your code, output should be:

```aidl
                                                ┌─────────────────────┬──────────────────────────┐
                                                │        White        │     African-American     │
┌───────────────────────────────────────────────┼─────────────────────┼──────────────────────────┤
│    Didn't Re-Offend, but Labeled High Risk    │        23.5%        │           44.8%          │
├───────────────────────────────────────────────┼─────────────────────┼──────────────────────────┤
│    Did    Re-Offend, but Labeled Low  Risk    │        47.7%        │           28.0%          │
└───────────────────────────────────────────────┴─────────────────────┴──────────────────────────┘
```
**OBS**.: As mentioned in the "Lab1_Understanding Propublica.pdf" file, in order for this analysis to be the same as in the article make the method ``isHighRisk()`` from the
defendant to return ``true`` in the case the defendant is deemed **either** medium or high risk.

# Notes for Lab 2

- Mind the difference between `==` and `.equals()` when dealing with strings. If you aren't 
  sure, discuss with a peer or a TA/instructor!
- Don't forget to add try-catch statements wherever you find necessary. That will be taken into account during grading.

# General Style & Coding Tips

Below are some helpful general tips and style guidelines for all labs (they will be taken into account during grading):

-   Remember to use Javadoc style conventions while commenting.
    > For reference on Javadoc style, check out [this resource](https://www.tutorialspoint.com/java/java_documentation.htm). 
    > Don't worry about tags, just look at the examples at the top. Plus, use [this code example](https://pythontutor.com/java.html#code=/**%0A%20*%20Java%20program%20that%20computes%20the%20sum%20of%20the%20first%20n%20numbers%0A%20*%20%40author%20Jeova%20Farias%0A%20*%20%40version%20January%2013,%202022%0A%20*/%0Apublic%20class%20Main%20%7B%0A%20%20%20%20public%20static%20void%20main%28String%5B%5D%20args%29%20%7B%0A%20%20%20%20%20%20%20%20int%20n%20%3D%2010%3B%0A%20%20%20%20%20%20%20%20int%20result%20%3D%20sumIntegers%28n%29%3B%0A%20%20%20%20%20%20%20%20System.out.println%28result%29%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20/**%0A%20%20%20%20%20*%20Returns%20the%20sum%20of%20the%20first%20n%20integers%0A%20%20%20%20%20*%20%40param%20n%20positive%20integer%20n%0A%20%20%20%20%20*%20%40return%20sum%20of%20the%20first%20n%20integers%0A%20%20%20%20%20*/%0A%20%20%20%20public%20static%20int%20sumIntegers%28int%20n%29%7B%0A%20%20%20%20%20%20%20%20int%20total%20%3D%200%3B%20//%20Set%20up%20a%20variable%20for%20the%20total%0A%20%20%20%20%20%20%20%20for%20%28int%20i%20%3D%200%3B%20i%20%3C%3D%20n%3B%20i%2B%2B%29%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20total%20%2B%3D%20i%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20return%20total%3B%0A%20%20%20%20%7D%0A%7D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=java&rawInputLstJSON=%5B%5D&textReferences=false)
    from class as a reference for what your style should look like.

-   Write your variables in CamelCase, and be sure to indent properly.

-   Don't forget to add comments! Include...
    > - A document header (name, date, program description)
    > - Comments at the top of each function describing what the
        >   function does
    > - Comments within the functions as needed, to describe
        >   non-obvious steps

-   When working on larger programs, test as you go! That is, write
    a little of code, then make sure it works before building on it.

-   Focus on correctness rather than efficiency.



