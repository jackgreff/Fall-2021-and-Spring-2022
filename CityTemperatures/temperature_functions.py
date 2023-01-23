import doctest

def city_temperature_month(state: str, city: str, month: int) -> None:
    """
    Given a city, state, and month, this function will print every recorded temperature at each available year
    :param state: state selected
    :param city: city selected
    :param month: the month selected
    :return: several print statements saying each year and temperature

    :examples:

    >>> city_temperature_month('New York','Albany', 2) #complete data (every year)
    Average temperatures in Albany, New York, in February:
    -Year: 1995: 23.85
    -Year: 1996: 25.63
    -Year: 1997: 30.31
    -Year: 1998: 31.46
    -Year: 1999: 28.25
    -Year: 2000: 28.47
    -Year: 2001: 27.73
    -Year: 2002: 32.15
    -Year: 2003: 21.62
    -Year: 2004: 25.30
    -Year: 2005: 26.85
    -Year: 2006: 28.42
    -Year: 2007: 20.11
    -Year: 2008: 27.03
    -Year: 2009: 27.76
    -Year: 2010: 27.95
    -Year: 2011: 24.17
    -Year: 2012: 32.52
    -Year: 2013: 26.90
    -Year: 2014: 23.19
    -Year: 2015: 13.57
    -Year: 2016: 31.13
    -Year: 2017: 34.02
    -Year: 2018: 32.96
    -Year: 2019: 27.91
    -Year: 2020: 31.83

    >>> city_temperature_month('Pennsylvania','Harrisburg', 2) #incomplete data (not every year)
    Average temperatures in Harrisburg, Pennsylvania, in February:
    -Year: 1995: 28.99
    -Year: 1996: 31.89
    -Year: 1997: 38.30
    -Year: 1998: 39.77
    -Year: 1999: 35.92
    -Year: 2000: 34.41
    -Year: 2001: 34.58
    -Year: 2002: 37.74
    -Year: 2003: 27.59
    -Year: 2004: 31.03
    -Year: 2005: 33.75
    -Year: 2006: 33.56
    -Year: 2007: 25.73
    -Year: 2008: 32.51
    -Year: 2009: 34.01
    -Year: 2010: 30.90

    >>> city_temperature_month('Pennsylvania','Harrisberg', 2) #intionally spelled wrong
    No temperatures recorded for that year (it's possible you spelled the the city or state as well)

    """
    #preconditions
    assert isinstance(state,str) and isinstance(city,str) and isinstance(month,int)
    assert 12 >= month > 0, "there are 12 months. Enter between 1 and 12 "

    #month converter
    to_month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

    file = open('temperature_cities.csv', "r")
    header = file.readline()#reads header so it won't be run when going through data
    header_list = header[:-1].split(',')
    count = 0 #count is used so that the header won't be printed if there is nothing below it and will print that nothing comes up

    for line in file:
        line_list = line[:-1].split(',') #get a list of the header, used for printing years
        line_state = line_list[0] #state is first one. This and line_city aren't necessarily needed for below if statement, but it helps for reading
        line_city = line_list[1] #city is second one

        if line_city == city and line_state == state and line_list[2] == str(month):
            if count == 0:
                print(f"Average temperatures in {city}, {state}, in {to_month[month]}:")

            for a in range(3,len(line_list)):
                if line_list[a] != "":
                    print(f"-Year: {header_list[a]}: {line_list[a]}")
            count += 1;

    if count == 0: #if nothing matches
        print("No temperatures recorded for that year (it's possible you spelled the the city or state as well)")

# city_temperature_month('New York','Albany', 2)
# city_temperature_month('Pennsylvania','Harrisburg', 2)

def city_temperature_year(state: str, city: str, year: int) -> None:
    """
    Given a city, state, and year, this function will print every recorded temperature each month
    :param state: state selected
    :param city: city selected
    :param year: the year selected
    :return: several print statements saying each month and temperature

    :examples:

    >>> city_temperature_year('New York','Albany', 2020) #incomplete data (not every month)
    Average temperatures in Albany, New York, in 2020:
    -Month: January: 32.25
    -Month: February: 31.83
    -Month: March: 42.22
    -Month: April: 46.78
    -Month: May: 50.45

    >>> city_temperature_year('New York','Albany', 2015) #complete data (every month)
    Average temperatures in Albany, New York, in 2015:
    -Month: January: 20.30
    -Month: February: 13.57
    -Month: March: 30.30
    -Month: April: 48.12
    -Month: May: 66.42
    -Month: June: 66.67
    -Month: July: 72.69
    -Month: August: 72.55
    -Month: September: 67.80
    -Month: October: 50.31
    -Month: November: 45.84
    -Month: December: 42.01

    >>> city_temperature_year('Arizona','Yuma', 2016) #no data available
    No temperatures recorded for that year(it's possible you spelled the the city or state as well)

    >>> city_temperature_year('New York','Albeny', 2015) #spelling mistake
    No temperatures recorded for that year(it's possible you spelled the the city or state as well)
    """
    assert isinstance(state,str) and isinstance(city,str) and isinstance(year,int)
    assert 2020 >= year >= 1995, "there is data for 2020 and 1995 only" #if it's not a state or city, it will be covered below

    to_month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

    file = open('temperature_cities.csv', "r")
    header = file.readline()
    header_list = header[:-1].split(',')#extacts header so its not with data

    #find the order of the year wanted in header
    order_year = 0
    for a in range(len(header_list)):
        if header_list[a] == str(year):
            order_year = a

    count = 0#counts how many months are collected
    for line in file:
        line_list = line[:-1].split(',')#list of line
        line_state = line_list[0]
        line_city = line_list[1]

        if line_city == city and line_state == state and line_list[order_year] != "":#If matches input
            # print(f"Month: {line_list[order_year]}")
            if count == 0:#first time will print
                print(f"Average temperatures in {city}, {state}, in {year}:")

            if line_list[order_year] != "":#if there is data for the month

                print(f"-Month: {to_month[int(line_list[2])]}: {line_list[order_year]}")
                count += 1
    file.close()
    if count == 0:#if nothing is found
        print("No temperatures recorded for that year(it's possible you spelled the the city or state as well)")



# city_temperature_year("Arizona","Tucson",2019)
# city_temperature_year('New York','Albany', 2020)

def hottest_coldest_cities(month: int, year: int) -> None:
    """
    Given a month and year, this function will print the warmest and coldest place
    :param month: month selected
    :param year: year selected
    :return: several print statements saying the coldest and warmest year

    :examples:

    >>> hottest_coldest_cities(8,1995)#example, likely almost full data
    The hottest city in August of 1995 is Yuma in Arizona with 96.15 degrees.
    The coldest city in August of 1995 is Juneau in Alaska with 54.32 degrees.

    #there will always be at least one month. We know off a previous example that not every place has May 2020
    >>> hottest_coldest_cities(5,2020)#example, likely missing data
    The hottest city in May of 2020 is Phoenix in Arizona with 88.16 degrees.
    The coldest city in May of 2020 is Sault Ste Marie in Michigan with 39.26 degrees.

    >>> hottest_coldest_cities(5,2021) #no data
    there is no information with the parameters entered. Try again

    """
    assert isinstance(month,int) and isinstance(year,int)
    assert 12 >= month > 0, "there are 12 months. Enter between 1 and 12 "
    # the right range of years will be corrected below (no need for precondition

    to_month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    #same as above. File opens and reads header, creates list
    file = open('temperature_cities.csv', "r")
    header = file.readline()
    header_list = header[:-1].split(',')

    order_year = "not a number"
    for a in range(len(header_list)):
        if header_list[a] == str(year):
            order_year = a

    coldest_temp = 10000
    coldest_city = ""
    coldest_state = ""

    hottest_temp = 0
    hottest_city = ""
    hottest_state = ""

    for line in file:
        #creates line and finds month and city
        line_list = line[:-1].split(',')
        line_month = line_list[2]
        line_city = line_list[1]

        if line_month == str(month) and type(order_year) == int: #if passes input
            if line_list[order_year] != "": #need another if statement if order_year isn't an int, won't get here if false
                if float(line_list[order_year]) > hottest_temp:
                    hottest_temp = float(line_list[order_year])
                    hottest_city = line_list[1]
                    hottest_state = line_list[0]

                if float(line_list[order_year]) < coldest_temp:
                    coldest_temp = float(line_list[order_year])
                    coldest_city = line_list[1]
                    coldest_state = line_list[0]
    file.close()

    #print statements
    if coldest_city == "" or hottest_city == "": #if no da   ta is overwritten
        print("there is no information with the parameters entered. Try again")
    else:
        print(f"The hottest city in {to_month[month]} of {year} is {hottest_city} in {hottest_state} with {hottest_temp} degrees.")
        print(f"The coldest city in {to_month[month]} of {year} is {coldest_city} in {coldest_state} with {coldest_temp} degrees.")

doctest.testmod()


# hottest_coldest_cities(8,1995)




