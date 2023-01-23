def square(num: int) -> int:
    assert  isinstance(num,int) or isinstance(num,float), "you didn't enter an integer"

    sq = num**2
    assert  sq == num**2, "something went wrong"
    return sq

print(square(4))

def precond(num: int):
    if num < 0:
        raise ValueError("please enter a positive number")
    if type(num) != int:
        raise ValueError("please enter an integer")

def mult_list(list1: list, list2: list) -> list:
    assert len(list1) == len(list2), "lists are not the same length"
    mult = []
    for a in range(len(list1)):
        try:
            mult.append(list1[a]*list2[a])
        except ZeroDivisionError:
            mult.append(float("NaN"))
        except TypeError:
            print("a value is not an int")

    return mult

print(mult_list([3,3],[2,2]))
print(mult_list([3,3],[2,0]))
print(mult_list([3,3],[2,2,2]))