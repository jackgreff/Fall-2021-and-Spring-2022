import sorting_and_searching
import doctest


def read_data() -> list:
    """
    Reads books.csv and puts the titles into a clean list (not sorted though)
    :return: clean list of titles

    :examples:

    >>> read_data()
    ['Fundamentals of Wavelets', 'Data Smart', 'God Created the Integers', 'Superfreakonomics', 'Orientalism', 'Nature of Statistical Learning Theory', 'Integration of the Indian States', "Drunkard's Walk", 'Image Processing & Mathematical Morphology', 'How to Think Like Sherlock Holmes', 'Data Scientists at Work', 'Slaughterhouse Five', 'Birth of a Theorem', 'Structure & Interpretation of Computer Programs', 'Age of Wrath', 'Trial', "Statistical Decision Theory'", 'Data Mining Handbook', 'New Machiavelli', 'Physics & Philosophy', 'Making Software', 'Analysis', 'Machine Learning for Hackers', 'Signal and the Noise', 'Python for Data Analysis', 'Introduction to Algorithms', 'Beautiful and the Damned', 'Outsider', 'Complete Sherlock Holmes', 'Complete Sherlock Holmes', 'Wealth of Nations', 'Pillars of the Earth', 'Mein Kampf', 'Tao of Physics', "Surely You're Joking Mr Feynman", 'Farewell to Arms', 'Veteran', 'False Impressions', 'Last Lecture', 'Return of the Primitive', 'Jurassic Park', 'Russian Journal', 'Tales of Mystery and Imagination', 'Freakonomics', 'Hidden Connections', 'Story of Philosophy', 'Asami Asami', 'Journal of a Novel', 'Once There Was a War', 'Moon is Down', 'Brethren', 'In a Free State', 'Catch 22', 'Complete Mastermind', 'Dylan on Dylan', 'Soft Computing & Intelligent Systems', 'Textbook of Economic Theory', 'Econometric Analysis', 'Learning OpenCV', 'Data Structures Using C & C++', 'Computer Vision', 'Principles of Communication Systems', 'Let Us C', 'Amulet of Samarkand', 'Crime and Punishment', 'Angels & Demons', 'Argumentative Indian', 'Sea of Poppies', 'Idea of Justice', 'Raisin in the Sun', "All the President's Men", 'Prisoner of Birth', 'Scoop!', 'Ahe Manohar Tari', 'Last Mughal', 'Social Choice & Welfare', 'Radiowaril Bhashane & Shrutika', 'Gun Gayin Awadi', 'Aghal Paghal', 'Maqta-e-Ghalib', 'Beyond Degrees', 'Manasa', 'India from Midnight to Milennium', "World's Greatest Trials", 'Great Indian Novel', 'O Jerusalem!', 'City of Joy', 'Freedom at Midnight', 'Winter of Our Discontent', 'On Education', 'Free Will', 'Bookless in Baghdad', 'Case of the Lame Canary', 'Theory of Everything', 'New Markets & Other Essays', 'Electric Universe', 'Hunchback of Notre Dame', 'Burning Bright', 'Age of Discontuinity', 'Doctor in the Nude', 'Down and Out in Paris & London', 'Identity & Violence', 'Beyond the Three Seas', "World's Greatest Short Stories", 'Talking Straight', "Maugham's Collected Short Stories", 'Phantom of Manhattan', 'Ashenden of The British Agent', 'Zen & The Art of Motorcycle Maintenance', 'Great War for Civilization', 'We the Living', 'Artist and the Mathematician', 'History of Western Philosophy', 'Selected Short Stories', 'Rationality & Freedom', 'Clash of Civilizations and Remaking of the World Order', 'Uncommon Wisdom', 'One', 'Karl Marx Biography', 'To Sir With Love', 'Half A Life', 'Discovery of India', 'Apulki', 'Unpopular Essays', 'Deceiver', 'Veil: Secret Wars of the CIA', 'Char Shabda', 'Rosy is My Relative', 'Moon and Sixpence', 'Political Philosophers', 'Short History of the World', 'Trembling of a Leaf', 'Doctor on the Brain', 'Simpsons & Their Mathematical Secrets', 'Pattern Classification', 'From Beirut to Jerusalem', 'Code Book', 'Age of the Warrior', 'Final Crisis', 'Killing Joke', 'Flashpoint', 'Batman Earth One', 'Crisis on Infinite Earths', 'Numbers Behind Numb3rs', 'Superman Earth One - 1', 'Superman Earth One - 2', 'Justice League: Throne of Atlantis', "Justice League: The Villain's Journey", 'Death of Superman', 'History of the DC Universe', 'Batman: The Long Halloween', 'Life in Letters', 'Information', 'Journal of Economics', 'Elements of Information Theory', 'Power Electronics - Rashid', 'Power Electronics - Mohan', 'Neural Networks', 'Grapes of Wrath', 'Vyakti ani Valli', 'Statistical Learning Theory', 'Empire of the Mughal - The Tainted Throne', 'Empire of the Mughal - Brothers at War', 'Empire of the Mughal - Ruler of the World', "Empire of the Mughal - The Serpent's Tooth", 'Empire of the Mughal - Raiders from the North', 'Mossad', 'Jim Corbett Omnibus', '20000 Leagues Under the Sea', 'Batatyachi Chal', 'Hafasavnuk', 'Urlasurla', 'Pointers in C', 'Cathedral and the Bazaar', 'Design with OpAmps', 'Think Complexity', "Devil's Advocate", 'Ayn Rand Answers', 'Philosophy: Who Needs It', "World's Great Thinkers", 'Data Analysis with Open Source Tools', "Broca's Brain", 'Men of Mathematics', 'Oxford book of Modern Science Writing', 'Justice', 'Arthashastra', 'We the People', 'We the Nation', 'Courtroom Genius', 'Dongri to Dubai', 'History of England', 'City of Djinns', "India's Legal System", 'More Tears to Cry', 'Ropemaker', 'Angels & Demons', 'Judge', 'Attorney', 'Prince', 'Eyeless in Gaza', 'Tales of Beedle the Bard', 'Girl with the Dragon Tattoo', "Girl who kicked the Hornet's Nest", 'Girl who played with Fire', 'Batman Handbook', "Murphy's Law", 'Structure and Randomness', 'Image Processing with MATLAB', 'Animal Farm', 'Idiot', 'Christmas Carol']

    """
    database = open("books.csv", "r")
    header = database.readline()
    database_list = []
    for line in database:
        line_list = line[:-1].split(',')  # get a list of the header, used for printing years
        title = line_list[0]
        up_title = ""  # to get out semicolons
        for a in title:
            if a != '''"''':  # removes quatation marks (can't combine with below becuause then loop breaks if there is a qutation mark
                if a != ";":  # stops everything after the colon, so the and stuff like that aren't included in new title
                    up_title = up_title + a
                else:
                    break
                # up_title = up_title + a if you don't want that then comment out the amove if/else statement and include this line

        database_list.append(up_title)
    return database_list


# print(read_data())
# print(sorting_and_searching.insertion_sort(read_data()))


def user_interface():
    """
    interface that asks the user for a book and gives index of book
    """
    sorted_data = sorting_and_searching.selection_sort(read_data())  # sorts data
    # sorted_data = sorting_and_searching.insertion_sort(read_data())  # sorts data

    while True:
        book = input("What book are you searching for?")
        if book != "":
            location = sorting_and_searching.binary_search(sorted_data, book)
            # location = sorting_and_searching.linear_search(sorted_data, book)
            if location == -1:
                print("your book is not in the database (check capitalization). Try again")
            else:
                print(f"you file is number {location} in the database")
        else:
            break

doctest.testmod()
# print(sorting_and_searching.bubble_sort(read_data()))

if __name__ == '__main__':
    user_interface()

