import doctest


def quadratic_function(x: float, b: float, c: float):
    return x**2 + b*x + c


def find_minimizer(left: float, right: float) -> float:
    """
    Finds the local minimum between "left" and "right" for a quadratic equation

    :param left: lowest value x for domain of function
    :param right: highest value x for domain of function
    :return: returns the minimum between left and right

    :examples:
    >>> round(find_minimizer(-15.0, 15.0),0) #general min of function (since its between the walls)
    -11.0
    >>> round(find_minimizer(-30,-15),0)#INT, lowest x point (testing below the min) , will go to wall closest to -11
    -15.0
    >>> round(find_minimizer(15.0,30.0),0)#lowest x point (testing above the min) , will go to wall closest to -11
    15.0

    #no need for more tests, will always be the side closest to -11
    """
    left = float(left) #allows ints to pass below statement
    right = float(right)

    if ((isinstance(left,int) and isinstance(right,int)) or (isinstance(left,float) and isinstance(right,float))): #precondition, can be negative or with decimal (just must be float or int)
        fxb = 22
        fxc = 8

        mid = (left + right)/2

        leftpoint = quadratic_function((left+mid)/2,fxb,fxc)
        rightpoint = quadratic_function((right+mid)/2,fxb,fxc)

        if abs(leftpoint - rightpoint) < .0001: ##checks if the points are close enough (ultimately rounded. it's so .0001 value doesn't matter)
            return mid

        if leftpoint < rightpoint:#moves left and right between the left half for next round
            return find_minimizer(left,mid)
        elif leftpoint > rightpoint:#moves left and right between the right half for next round
            return find_minimizer(mid,right)

def harder_function(x: float):
    return x**4 + abs(x) + 2**x

def h_find_minimizer(left: float, right: float) -> float:
    """
    Finds the minimum (not locally) of harder_function.

    :return: returns the minimum between left and right

    :examples:
    >>> round(h_find_minimizer(-25.0,25.0)) #minimum, left and right chosen knowing minimum
    0

    >>> round(h_find_minimizer(-25,25)) #minimum, left and right chosen knowing minimum
    0

    """
    left = float(left) #allows ints to pass below statement
    right = float(right)

    if isinstance(left,float) and isinstance(right,float): #precondition, can be negative or with decimal (just must be float or int)

        mid = (left + right)/2

        leftpoint = harder_function((left+mid)/2)
        rightpoint = harder_function((right+mid)/2)


        if abs(leftpoint - rightpoint) < .0001: #checks if the points are close enough (ultimately rounded. it's so .0001 value doesn't matter)
            return mid

        if leftpoint < rightpoint: #moves left and right between the left half for next round
            return h_find_minimizer(left,mid)
        elif leftpoint > rightpoint:#moves left and right between the right half for next round
            return h_find_minimizer(mid,right)



# Uncomment the next line to run the tests

doctest.testmod()


