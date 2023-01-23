import doctest

def keyboard_euclidean_distance(char1: str, char2: str) -> float:
    """
    this function finds the distance between letters on a keyboard
    :param char1: first letter compared (which one is first doesn't matter)
    :param char2: second letter compared
    :return: distance between letters

    :examples:
    >>> keyboard_euclidean_distance("q", "a") #char 2 is just char 1 shifted down 1
    1.0

    >>> keyboard_euclidean_distance("q", "w") #char 2 is just char 1 shifted 1 to the left
    1.0

    >>> keyboard_euclidean_distance("q", "s") #char 2 is just char 1 shifted down 1 and 1 to the right (root 1)
    1.4142135623730951

    >>> keyboard_euclidean_distance("q", "q") #same
    0.0

    >>> keyboard_euclidean_distance("", "") #empty
    0.0

    """
    keyboard_xy = {'q': (0, 0), 'w': (1, 0), 'e': (2, 0), 'r': (3, 0), 't': (4, 0), 'y': (5, 0), 'u': (6, 0), 'i': (7, 0), 'o': (8, 0), 'p': (9, 0),
                   'a': (0, 1), 's': (1, 1), 'd': (2, 1), 'f': (3, 1), 'g': (4, 1), 'h': (5, 1), 'j': (6, 1), 'k': (7, 1), 'l': (8, 1),
                   'z': (0, 2), 'x': (1, 2), 'c': (2, 2), 'v': (3, 2), 'b': (4, 2), 'n': (5, 2), 'm': (6, 2)}
    # Your code goes here
    if type(char1) == str and type(char2) == str and len(char1) <= 1 and len(char1) <= 1: #precondition
        if char1 != char2:
            if char1 == " " or char2 == " ": #spaces are considered 10
                return 10

            #distance formula:
            x = (keyboard_xy[char2][0] - keyboard_xy[char1][0])**2
            y = (keyboard_xy[char2][1] - keyboard_xy[char1][1])**2
            return (x+y)**(1/2)
        return 0.0

def euclidian_hamming_distance(str1: str, str2: str) -> float:
    """
    this function finds the distance between strings on a keyboard in a euclidian way
    :param str1: first string compared (which one is first doesn't matter)
    :param str2: second string compared
    :return: eucidlian hamming distance between char1 and char2

    :examples:
    >>> euclidian_hamming_distance("qwerty", "qwerty") #same
    0.0
    >>> euclidian_hamming_distance("qwerty", "QWERTY") #same, one capitalized
    0.0

    >>> euclidian_hamming_distance("qwerty", "wertyu") # shifted 1 to left
    6.0

    >>> euclidian_hamming_distance("qwerty", "asdfgh") #shifted 1 down
    6.0

    >>> euclidian_hamming_distance("qwerty", "sdfghj") #shifted 1 left AND down (6 times root 1)
    8.485281374238571

    >>> euclidian_hamming_distance("qwerty", "a") #different lengths
    51.0

    >>> euclidian_hamming_distance("", "") #empty
    0

    """
    # Your code goes here (don't forget the docstring above)
    if type(str1) == str and type(str2) == str: #precondition

        str1=str1.lower()
        str2=str2.lower()
        long = str2  # made it the default, will be corrected below if wrong
        short = str1
        if len(str1) > len(str2):  # if not the default stays
            long = str1
            short = str2

        # make strings the same size for comparison
        for a in range(0, (len(long) - len(short))):
            short = short + " "

        mismatch = 0
        #simple for loop to add all distances
        for a in range(0,len(long)):
            mismatch += keyboard_euclidean_distance(long[a],short[a])

        return mismatch




def hamming_distance(str1: str, str2: str) -> int:
    """
    this function finds the distance between strings on a keyboard in the hamming way
    :param str1: first string compared (which one is first doesn't matter)
    :param str2: second string compared
    :return: hamming distance between char1 and char2

    :examples:
    >>> hamming_distance("qwerty", "qwerty") #same
    0
    >>> hamming_distance("qwerty", "QWERTY") #same, one capitalized
    0

    >>> hamming_distance("qwerty", "wertyu") # entirely different
    6

    >>> hamming_distance("qwebbb", "qweaaa") #some same, some different
    3

    >>> hamming_distance("qwerty", "s") #different lengths
    6

    >>> hamming_distance("", "") #they are the same, so zero
    0

    """
    # Your code goes here (don't forget the docstring above)

    # chooses long one
    if type(str1) == str and type(str2) == str: #precondition

        str1=str1.lower()
        str2=str2.lower()
        long = str2  # made it the default, will be corrected below if wrong
        short = str1
        if len(str1) > len(str2):  # if not the default stays
            long = str1
            short = str2

        # make strings the same size for comparison
        for a in range(0, (len(long) - len(short))):
            short = short + " "

        mismatch = 0
        #for loop, if different lengths add 1
        for a in range(0,len(short)):
            if long[a] != short[a]:
                mismatch += 1

        return mismatch



def user_interface(word_1: str, word_2: str) -> None:
    """
    parent function that tells you euclidian hamming distance and hamming distance based off user input
    :return: lines telling you the distances

    """
    # Your code goes here


    while word_1 != "" and word_2 != "":
        # word_1 = input("what is your first word you want to check?")
        # word_2 = input("what is your first word you want to check?")

        #PRECONDITION
        for a in word_1:# will stop of if there is a number inside
            try:
                float(a)
                print(f"invalid input with '{a}'")
                word_1 = "" #makes one word empty, which wont pass through the if loop and then while loop
            except:
                needed_space = 0 # need to fill this space

        word_1=word_1.lower()
        word_2=word_2.lower()
        long = word_2  # made it the default, will be corrected below if wrong
        short = word_1
        if len(word_1) > len(word_2):  # if not the default stays
            long = word_1
            short = word_2

        # make strings the same size for comparison
        for a in range(0, (len(long) - len(short))):
            short = short + " "
        if word_1 != "" and word_2 != "":
            word_1 = word_1.lower()
            word_2 = word_2.lower()
            #
            # print(f"your normal hamming distance between {word_1} and {word_2} is {hamming_distance(long,short)}")
            #
            # print(f"your euclidian hamming distance between {word_1} and {word_2} is {euclidian_hamming_distance(long,short)}")

            # print(euclidian_hamming_distance(long,short))
        return euclidian_hamming_distance(long,short)
doctest.testmod()

# user_interface()

