import auto_correct
import string_similarity


def user_interface() -> None:
    """
    runs code that corrects word, adds inputs to a log, and gives option to add new word to dictionary
    :return: returns nothing, executes tasks only

    """
    inp = "tempvar"
    while inp != "":
        inp = input("what word do you want to correct?")
        if inp == "":#needed so if the first input is empty it will stop
            break
        #PRECONDITION IN correct_word
        cor = auto_correct.correct_word(inp)
        #cor condition for below needs to be lowercase, which is a post condition for correct_word
        if cor.lower() == inp.lower():
            print(f"Input word: {inp}, word is correct.")
            auto_correct.record_data(f"Input word: {inp}, word is correct.") #records data
        else:
            print(f"Input word: {inp}, Corrected word: {cor}.")
            auto_correct.record_data(f"Input word: {inp}, Corrected word: {cor}.") #records data
            auto_correct.add_word() #will ask if wants to add to dictionary

if __name__ == '__main__':
    user_interface()




