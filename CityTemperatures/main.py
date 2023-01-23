import temperature_functions
import doctest

def user_interface():
    """
    Asks and gives several ways to view the weather in the U.S.
    :return: several print statements telling weather data
    """

    #there is no preconditon to pass user_iterface. It will stop though if input is empty though
    inp = "something"
    while inp != "":
        #informing the user, asks which one they want
        print("Which do you want?")
        print("(1) The temperature every year for a certain city, state and month")
        print("(2) The temperature every month for a certain city, state and year")
        print("(3) The warmest and coldest temperature for a given year and month")
        inp = input("Enter the applicable number")

        try: #won't pass if it can't be converted to number
            inp = int(inp)

            #asks parameters and gives results
            if inp == 1:
                state = input("What state do you want?")
                city = input("What city do you want?")
                month = int(input("What month do you want(enter number)?"))
                temperature_functions.city_temperature_month(state,city,month)
            elif inp == 2:
                state = input("What state do you want?")
                city = input("What city do you want?")
                year = int(input("Which year do you want"))
                temperature_functions.city_temperature_year(state,city,year)
            elif inp == 3:
                month = int(input("Which month do you want(enter number)?"))
                year = int(input("Which year do you want"))
                temperature_functions.hottest_coldest_cities(month,year)
            else: #not 1,2, or 3 will print this
                print("invalid input. Not 1, 2, or 3")
        except:#error caused will be if something entered cannot be converted to an int
            if inp != "": #if you dont enter anything, function wont print anything
                print("invalid input. You didn't enter a number")

if __name__ == '__main__':
    user_interface()