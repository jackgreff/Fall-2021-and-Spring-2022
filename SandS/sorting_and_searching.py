import main
import doctest


def selection_sort(
        list1: list) -> list:  # finds the minimum and puts it in front, then range moves to next term and restarts
    """
    sorts a list using selection sort
    :param list1: list to be sorted
    :return: sorted version of list

    :examples:

    >>> selection_sort([1,5,4.0,6.0,7,8,3,2,1]) #different types inside (float and int)
    [1, 1, 2, 3, 4.0, 5, 6.0, 7, 8]
    >>> selection_sort(main.read_data()) #when sort our titles
    ['20000 Leagues Under the Sea', 'Age of Discontuinity', 'Age of Wrath', 'Age of the Warrior', 'Aghal Paghal', 'Ahe Manohar Tari', "All the President's Men", 'Amulet of Samarkand', 'Analysis', 'Angels & Demons', 'Angels & Demons', 'Animal Farm', 'Apulki', 'Argumentative Indian', 'Arthashastra', 'Artist and the Mathematician', 'Asami Asami', 'Ashenden of The British Agent', 'Attorney', 'Ayn Rand Answers', 'Batatyachi Chal', 'Batman Earth One', 'Batman Handbook', 'Batman: The Long Halloween', 'Beautiful and the Damned', 'Beyond Degrees', 'Beyond the Three Seas', 'Birth of a Theorem', 'Bookless in Baghdad', 'Brethren', "Broca's Brain", 'Burning Bright', 'Case of the Lame Canary', 'Catch 22', 'Cathedral and the Bazaar', 'Char Shabda', 'Christmas Carol', 'City of Djinns', 'City of Joy', 'Clash of Civilizations and Remaking of the World Order', 'Code Book', 'Complete Mastermind', 'Complete Sherlock Holmes', 'Complete Sherlock Holmes', 'Computer Vision', 'Courtroom Genius', 'Crime and Punishment', 'Crisis on Infinite Earths', 'Data Analysis with Open Source Tools', 'Data Mining Handbook', 'Data Scientists at Work', 'Data Smart', 'Data Structures Using C & C++', 'Death of Superman', 'Deceiver', 'Design with OpAmps', "Devil's Advocate", 'Discovery of India', 'Doctor in the Nude', 'Doctor on the Brain', 'Dongri to Dubai', 'Down and Out in Paris & London', "Drunkard's Walk", 'Dylan on Dylan', 'Econometric Analysis', 'Electric Universe', 'Elements of Information Theory', 'Empire of the Mughal - Brothers at War', 'Empire of the Mughal - Raiders from the North', 'Empire of the Mughal - Ruler of the World', "Empire of the Mughal - The Serpent's Tooth", 'Empire of the Mughal - The Tainted Throne', 'Eyeless in Gaza', 'False Impressions', 'Farewell to Arms', 'Final Crisis', 'Flashpoint', 'Freakonomics', 'Free Will', 'Freedom at Midnight', 'From Beirut to Jerusalem', 'Fundamentals of Wavelets', "Girl who kicked the Hornet's Nest", 'Girl who played with Fire', 'Girl with the Dragon Tattoo', 'God Created the Integers', 'Grapes of Wrath', 'Great Indian Novel', 'Great War for Civilization', 'Gun Gayin Awadi', 'Hafasavnuk', 'Half A Life', 'Hidden Connections', 'History of England', 'History of Western Philosophy', 'History of the DC Universe', 'How to Think Like Sherlock Holmes', 'Hunchback of Notre Dame', 'Idea of Justice', 'Identity & Violence', 'Idiot', 'Image Processing & Mathematical Morphology', 'Image Processing with MATLAB', 'In a Free State', 'India from Midnight to Milennium', "India's Legal System", 'Information', 'Integration of the Indian States', 'Introduction to Algorithms', 'Jim Corbett Omnibus', 'Journal of Economics', 'Journal of a Novel', 'Judge', 'Jurassic Park', 'Justice', "Justice League: The Villain's Journey", 'Justice League: Throne of Atlantis', 'Karl Marx Biography', 'Killing Joke', 'Last Lecture', 'Last Mughal', 'Learning OpenCV', 'Let Us C', 'Life in Letters', 'Machine Learning for Hackers', 'Making Software', 'Manasa', 'Maqta-e-Ghalib', "Maugham's Collected Short Stories", 'Mein Kampf', 'Men of Mathematics', 'Moon and Sixpence', 'Moon is Down', 'More Tears to Cry', 'Mossad', "Murphy's Law", 'Nature of Statistical Learning Theory', 'Neural Networks', 'New Machiavelli', 'New Markets & Other Essays', 'Numbers Behind Numb3rs', 'O Jerusalem!', 'On Education', 'Once There Was a War', 'One', 'Orientalism', 'Outsider', 'Oxford book of Modern Science Writing', 'Pattern Classification', 'Phantom of Manhattan', 'Philosophy: Who Needs It', 'Physics & Philosophy', 'Pillars of the Earth', 'Pointers in C', 'Political Philosophers', 'Power Electronics - Mohan', 'Power Electronics - Rashid', 'Prince', 'Principles of Communication Systems', 'Prisoner of Birth', 'Python for Data Analysis', 'Radiowaril Bhashane & Shrutika', 'Raisin in the Sun', 'Rationality & Freedom', 'Return of the Primitive', 'Ropemaker', 'Rosy is My Relative', 'Russian Journal', 'Scoop!', 'Sea of Poppies', 'Selected Short Stories', 'Short History of the World', 'Signal and the Noise', 'Simpsons & Their Mathematical Secrets', 'Slaughterhouse Five', 'Social Choice & Welfare', 'Soft Computing & Intelligent Systems', "Statistical Decision Theory'", 'Statistical Learning Theory', 'Story of Philosophy', 'Structure & Interpretation of Computer Programs', 'Structure and Randomness', 'Superfreakonomics', 'Superman Earth One - 1', 'Superman Earth One - 2', "Surely You're Joking Mr Feynman", 'Tales of Beedle the Bard', 'Tales of Mystery and Imagination', 'Talking Straight', 'Tao of Physics', 'Textbook of Economic Theory', 'Theory of Everything', 'Think Complexity', 'To Sir With Love', 'Trembling of a Leaf', 'Trial', 'Uncommon Wisdom', 'Unpopular Essays', 'Urlasurla', 'Veil: Secret Wars of the CIA', 'Veteran', 'Vyakti ani Valli', 'We the Living', 'We the Nation', 'We the People', 'Wealth of Nations', 'Winter of Our Discontent', "World's Great Thinkers", "World's Greatest Short Stories", "World's Greatest Trials", 'Zen & The Art of Motorcycle Maintenance']

    #BELOW PRODUCES THE RIGHT ERRORS FROM USING ASSERT
    >>> selection_sort([1,1.0,"3",[1,2,3],False])#different types, assert error risen
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.selection_sort[2]>", line 1, in <module>
        selection_sort([1,1.0,"3"])#different types
      File "/homes/jgreff/cs105/SortingAndSearching/sorting_and_searching.py", line 41, in selection_sort
        assert the_type == type(a), f"you gave different types: base type: {the_type}, {a}: {type(a)}"
    AssertionError: you gave different types: base type: <class 'int'>, 3: <class 'str'>

    """
    assert type(list1) == list, "you did not enter a list, so it cannot be sorted"  # list must be a list

    # all types in list must be the same, except for ints and floats
    the_type = type(list1[0])
    assert the_type == str or the_type == int or the_type == float
    for a in list1:
        if (the_type == float or the_type == int) and type(a) == int or type(a) == float:
            pass_ = True  # we want to allow floats and ints together
        else:
            assert the_type == type(a), f"you gave different types: base type: {the_type}, {a}: {type(a)}"

    for i in range(len(list1)):  # going through the list i times and places the minimum in in the front

        # minimum index
        min = i  # location at minimum

        for a in range(i + 1, len(list1)):
            if list1[a] < list1[min]:
                min = a

        list1[i], list1[min] = list1[min], list1[i]  # swaps minimum and current term (list1 of i)
    return list1


def insertion_sort(list1: list) -> list:  #
    """
    sorts a list using insertion sort
    :param list1: list to be sorted
    :return: sorted version of list

    :examples:

    >>> insertion_sort([1,5,4.0,6.0,7,8,3,2,1]) #different types inside (float and int)
    [1, 1, 2, 3, 4.0, 5, 6.0, 7, 8]
    >>> insertion_sort(main.read_data()) #when sort our titles
    ['20000 Leagues Under the Sea', 'Age of Discontuinity', 'Age of Wrath', 'Age of the Warrior', 'Aghal Paghal', 'Ahe Manohar Tari', "All the President's Men", 'Amulet of Samarkand', 'Analysis', 'Angels & Demons', 'Angels & Demons', 'Animal Farm', 'Apulki', 'Argumentative Indian', 'Arthashastra', 'Artist and the Mathematician', 'Asami Asami', 'Ashenden of The British Agent', 'Attorney', 'Ayn Rand Answers', 'Batatyachi Chal', 'Batman Earth One', 'Batman Handbook', 'Batman: The Long Halloween', 'Beautiful and the Damned', 'Beyond Degrees', 'Beyond the Three Seas', 'Birth of a Theorem', 'Bookless in Baghdad', 'Brethren', "Broca's Brain", 'Burning Bright', 'Case of the Lame Canary', 'Catch 22', 'Cathedral and the Bazaar', 'Char Shabda', 'Christmas Carol', 'City of Djinns', 'City of Joy', 'Clash of Civilizations and Remaking of the World Order', 'Code Book', 'Complete Mastermind', 'Complete Sherlock Holmes', 'Complete Sherlock Holmes', 'Computer Vision', 'Courtroom Genius', 'Crime and Punishment', 'Crisis on Infinite Earths', 'Data Analysis with Open Source Tools', 'Data Mining Handbook', 'Data Scientists at Work', 'Data Smart', 'Data Structures Using C & C++', 'Death of Superman', 'Deceiver', 'Design with OpAmps', "Devil's Advocate", 'Discovery of India', 'Doctor in the Nude', 'Doctor on the Brain', 'Dongri to Dubai', 'Down and Out in Paris & London', "Drunkard's Walk", 'Dylan on Dylan', 'Econometric Analysis', 'Electric Universe', 'Elements of Information Theory', 'Empire of the Mughal - Brothers at War', 'Empire of the Mughal - Raiders from the North', 'Empire of the Mughal - Ruler of the World', "Empire of the Mughal - The Serpent's Tooth", 'Empire of the Mughal - The Tainted Throne', 'Eyeless in Gaza', 'False Impressions', 'Farewell to Arms', 'Final Crisis', 'Flashpoint', 'Freakonomics', 'Free Will', 'Freedom at Midnight', 'From Beirut to Jerusalem', 'Fundamentals of Wavelets', "Girl who kicked the Hornet's Nest", 'Girl who played with Fire', 'Girl with the Dragon Tattoo', 'God Created the Integers', 'Grapes of Wrath', 'Great Indian Novel', 'Great War for Civilization', 'Gun Gayin Awadi', 'Hafasavnuk', 'Half A Life', 'Hidden Connections', 'History of England', 'History of Western Philosophy', 'History of the DC Universe', 'How to Think Like Sherlock Holmes', 'Hunchback of Notre Dame', 'Idea of Justice', 'Identity & Violence', 'Idiot', 'Image Processing & Mathematical Morphology', 'Image Processing with MATLAB', 'In a Free State', 'India from Midnight to Milennium', "India's Legal System", 'Information', 'Integration of the Indian States', 'Introduction to Algorithms', 'Jim Corbett Omnibus', 'Journal of Economics', 'Journal of a Novel', 'Judge', 'Jurassic Park', 'Justice', "Justice League: The Villain's Journey", 'Justice League: Throne of Atlantis', 'Karl Marx Biography', 'Killing Joke', 'Last Lecture', 'Last Mughal', 'Learning OpenCV', 'Let Us C', 'Life in Letters', 'Machine Learning for Hackers', 'Making Software', 'Manasa', 'Maqta-e-Ghalib', "Maugham's Collected Short Stories", 'Mein Kampf', 'Men of Mathematics', 'Moon and Sixpence', 'Moon is Down', 'More Tears to Cry', 'Mossad', "Murphy's Law", 'Nature of Statistical Learning Theory', 'Neural Networks', 'New Machiavelli', 'New Markets & Other Essays', 'Numbers Behind Numb3rs', 'O Jerusalem!', 'On Education', 'Once There Was a War', 'One', 'Orientalism', 'Outsider', 'Oxford book of Modern Science Writing', 'Pattern Classification', 'Phantom of Manhattan', 'Philosophy: Who Needs It', 'Physics & Philosophy', 'Pillars of the Earth', 'Pointers in C', 'Political Philosophers', 'Power Electronics - Mohan', 'Power Electronics - Rashid', 'Prince', 'Principles of Communication Systems', 'Prisoner of Birth', 'Python for Data Analysis', 'Radiowaril Bhashane & Shrutika', 'Raisin in the Sun', 'Rationality & Freedom', 'Return of the Primitive', 'Ropemaker', 'Rosy is My Relative', 'Russian Journal', 'Scoop!', 'Sea of Poppies', 'Selected Short Stories', 'Short History of the World', 'Signal and the Noise', 'Simpsons & Their Mathematical Secrets', 'Slaughterhouse Five', 'Social Choice & Welfare', 'Soft Computing & Intelligent Systems', "Statistical Decision Theory'", 'Statistical Learning Theory', 'Story of Philosophy', 'Structure & Interpretation of Computer Programs', 'Structure and Randomness', 'Superfreakonomics', 'Superman Earth One - 1', 'Superman Earth One - 2', "Surely You're Joking Mr Feynman", 'Tales of Beedle the Bard', 'Tales of Mystery and Imagination', 'Talking Straight', 'Tao of Physics', 'Textbook of Economic Theory', 'Theory of Everything', 'Think Complexity', 'To Sir With Love', 'Trembling of a Leaf', 'Trial', 'Uncommon Wisdom', 'Unpopular Essays', 'Urlasurla', 'Veil: Secret Wars of the CIA', 'Veteran', 'Vyakti ani Valli', 'We the Living', 'We the Nation', 'We the People', 'Wealth of Nations', 'Winter of Our Discontent', "World's Great Thinkers", "World's Greatest Short Stories", "World's Greatest Trials", 'Zen & The Art of Motorcycle Maintenance']

    #BELOW PRODUCES THE RIGHT ERRORS FROM USING ASSERT
    >>> insertion_sort([1,1.0,"3",[1,2,3],False])#can't handle list
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.insertion_sort[2]>", line 1, in <module>
        insertion_sort([1,1.0,"3",[1,2,3],False])#different types
      File "/homes/jgreff/cs105/SortingAndSearching/sorting_and_searching.py", line 109, in insertion_sort
        assert the_type == type(a), f"you gave different types: base type: {the_type}, {a}: {type(a)}"
    AssertionError: you gave different types: base type: <class 'int'>, 3: <class 'str'>
    """

    assert type(list1) == list, "you did not enter a list, so it cannot be sorted"  # list must be list

    # all types must be the same
    the_type = type(list1[0])  # all types must be the same as this one
    assert the_type == str or the_type == int or the_type == float  # can only handle str,int,float
    for a in list1:
        if (the_type == float or the_type == int) and (type(a) == int or type(a) == float):
            pass_ = True  # we want to allow floats and ints together
        else:
            assert the_type == type(a), f"you gave different types: base type: {the_type}, {a}: {type(a)}"

    for i in range(1, len(list1)):  # going through the list i times and places the minimum in sortlist
        position = i  # current position for while loop
        value = list1[i]  # current value for while loop
        # finds the position of value
        while position > 0 and value < list1[position - 1]:
            list1[position] = list1[position - 1]
            position = position - 1

        list1[position] = value  # makes the first one its bigger than into list[i]
    return list1


def linear_search(list1: list, e) -> int:  # no type hint for e since it can be almost any variable
    """
    Searches for the index of an item 'e' in list 'List1'
    :param list1: list to be searched
    :param list1: list to be searched
    :return: index of e in list 1 (or -1 if it is not in the list

    :examples:

    >>> linear_search(insertion_sort(main.read_data()),'Age of Discontuinity') #finds position in titles
    1

    >>> linear_search(insertion_sort(main.read_data()),'Trial') #finds position in titles
    195
    >>> linear_search([1.0,2,3,4,5,6],7) #not in list
    -1
    """
    assert type(list1) == list, "you did not enter a list, so it cannot be sorted"
    # we can have different types in list, so rest is not necessary

    for i in range(len(list1)):  # checks every term
        if list1[i] == e:
            return i
    return -1


def binary_search(sorted_list: list, item) -> list:  # item can be any variable, no hint
    """
    Searches for the index of an item 'e' in list 'List1'
    :param sorted_list: a sorted list that is searched
    :param item: item searched for
    :return: index of item in sorted_list (or -1 if it is not in the list)

    :examples:

    >>> binary_search(insertion_sort(main.read_data()),'Age of Discontuinity')
    1

    >>> linear_search(insertion_sort(main.read_data()),'Trial')
    195
    >>> linear_search([1.0,2,3,4,5,6],7) #not in list
    -1
    >>> linear_search([1,1.0,"3",[1,2,3],False],False)
    4
    """
    list1 = sorted_list
    assert type(list1) == list, "you did not enter a list, so it cannot be sorted"  # must be list

    the_type = type(list1[0])  # initial type, all should be the same for comparison
    assert the_type == str or the_type == int or the_type == float, "The types you entered aren't supported"
    for a in range(1, len(list1)):  # every term in the list must be the same
        if (the_type == float or the_type == int) and (
                type(a) == int or type(a) == float):  # allows ints and floats together
            pass_ = True  # meaningless variable, allows for else statement
        else:
            assert the_type == type(
                list1[a]), f"you gave different types: base type: {the_type}, {list1[a]}: {type(list1[a])}"
        assert list1[a] > list1[a - 1] or list1[a] == list1[
            a - 1], f"The list is not sorted. {list1[a]} is smaller than {list1[a - 1]}"

    list1 = sorted_list
    the_type = type(list1[0])  # the type that all should be
    assert the_type == str or the_type == int or the_type == float
    for a in range(1, len(list1)):
        if (the_type == float or the_type == int) and type(a) == int or type(a) == float:
            pass_ = True  # we want to allow floats and ints together
        else:
            assert the_type == type(
                list1[a]), f"you gave different types: base type: {the_type}, {list1[a]}: {type(list1[a])}"
        assert list1[a] > list1[a - 1] or list1[a] == list1[
            a - 1], f"The list is not sorted. {list1[a]} is smaller than {list1[a - 1]}"  # make sure the term before it is equal or less than current, else not sorted

    # divides list into two terms to see where the searched for term lands, updates during while loop and hones in on value
    left = sorted_list[0:(len(sorted_list) // 2)]
    right = sorted_list[len(sorted_list) // 2:]  # if odd right has extra

    order = 0
    in_list = False  # default is item is not in list, will be triggered if true
    while True:
        # print(order, left, right)

        # checks if its been divided into one term
        if len(left) == 1 and left[0] == item:
            in_list = True
            break
        elif len(right) == 1 and right[0] == item:
            order += 1  # if its on the right there's one on the left, so add 1
            in_list = True
            break
        elif len(left) <= 1 and left[0] != item and len(right) <= 1 and right[0] != item:  # not in list
            break

        # chooses one half to hone in on, repeats loop
        if item < right[0]:
            right = left[len(left) // 2::]  # if odd right has extra
            left = left[0:(len(left) // 2)]

        else:
            order += len(
                left)  # we add the length of the left if we are on the right, this way we added lengths that we have passed when getting closer to value
            left = right[0:(len(right) // 2)]
            right = right[len(right) // 2::]  # if odd right has extra

    if in_list == True:
        return order
    else:
        return -1


def bubble_sort(L: list) -> list:
    assert isinstance(L, list), "please enter a list"

    while True:
        order = True
        for a in range(1, len(L)):
            if L[a - 1] > L[a]:
                L[a - 1], L[a] = L[a], L[a - 1]
                order = False
        if order == True:
            return L



doctest.testmod()
