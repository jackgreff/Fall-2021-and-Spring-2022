import string_similarity
import doctest


def correct_word(inp:str) -> str:
    """
    this function will give the closest word with the shortest euclidian hamming distance to an input, even if it is itself
    :param inp: word being corrected
    :return: closest word (euclidian hamming distance)

    :examples:

    >>> correct_word("Jonny") #not in dictionary
    'jinny'

    >>> correct_word("Johnny") #in dictionary
    'johnny'

#BELOW PRODUCES THE RIGHT ERRORS FROM USING ASSERT
    # >>> correct_word("Johnny F") #phrase, not word
    # 'johnny'
    #
    # >>> correct_word("Johnny!") #contains a special character
    # 'johnny'

    # >>> correct_word("1") #number. doesn't matter that it's in a string
    # Johnny
    """
    #precondition
    for a in inp:
        assert a != " ", f"{a}there should be no spaces"
        assert a != "!" and a != "_" and a != "(" and a != ")" and a != "*", "there should be no special characters" #could be others, chose most common ones
        assert isinstance(a,str), "every character should be an str"

    file = open('words.txt', "r")
    line = "temp line for return"
    closest_str = "" #clostest starts as nothing
    smallest_dist = 1000000000000  # need an infinitely large number

    for line in file: #for each line we'll find the distance between it and the input
        if line != "\n":
            diff = string_similarity.user_interface(inp,line[:-1]) #the euclidian hamming distance between input and line
            if diff < smallest_dist:
                # print(f"the new smallest difference between {inp} and {line[:-1]} is {diff}")

                #new clostest, replaces old ones
                smallest_dist = diff
                closest_str = line[:-1]#removes the /n


    file.close()
    return closest_str.lower()#post condition, always lowercase

doctest.testmod()


def record_data(inp:str) -> None:
    """
    adds input to the log
    :param inp: string added to log
    :return: nothing, just execute tasks
    """
    assert isinstance(inp,str), "you did not enter a string"
    #opens, adds, closes
    file = open('records.txt', "a")
    file.write(inp+"\n")
    file.close()

def add_word(inp:str,add:str) ->  None:
    """
    adds paramater 'inp' to the dictionary if user wants to
    :param inp: string added to dictionary
    :param add: string that will say whether to add or not
    :return: nothing, just execute tasks
    """
    assert isinstance(inp,str) and isinstance(add,str) , "you did not enter a string"
    add = input("do you want to add {inp} to the dictionary? (Y = yes, anything else = no)")
    if add.lower() == "y":
        # opens, adds, closes
        file = open('words.txt', "a")
        file.write(inp + "\n")
        file.close()

# auto_correct()