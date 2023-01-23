def vcheck (string: str,num: int) -> None:
    if len(string) == 0:
        print(f"there are {num} vowels {string}")
        return
    if string[0] == "a" or string[0] == "e" or string[0] == "i" or string[0] == "o" or string[0] == "u":
        num += 1
    vcheck(string[1::],num)

# vcheck("mathamatica",0)


def typesum(x:int):
    count = 0
    while x < 100:
        inp = int(input("type a number: "))
        if inp == 0:
            break

        x += inp
        count += 1
        print(x)
    print(f"You entered {count} numbers")

# typesum(0)

def posneg():
    boolfor = True
    count = 0
    while boolfor == True:
        inp = input("type a number (or break if you want to stop): ")

        if (inp == "break"):
            break
        else:
            inp = float(inp)

        count += 1

        if inp < 0:
            print(f"{inp} that's negative")
        elif inp == 0:
            print(f"{inp} that's zero")
        elif inp > 0:
            print(f"{inp} that's positive")

        print(f"you entered {count} numbers")


#posneg()

n = 10
sum = 0
for i in range(0,n+1):
    if i**2 <= n:
        # print(i**2)
        sum += i**2
# print(f"the sum is {sum}")

def power(base: int, power:int) -> int:
    init_base = base
    for base in range (power):
        init_base = init_base*base
        power = power - 1
    # print(init_base)
#
# power(4,4)

def vowcount(string: str)-> int:
    string = "string"
    count = 0
    for a in range(len(string)):
        if a == 'a' or a == "e" or a == "i" or a == "o" or a == "u":
            count += 1
    print(f"count is {count}")

vowcount("aeiou")
