import doctest


def sum_of_4(num):

    """" find the sum of 4 numbers

     :param num: First Number
     :type num: int

     >>> sum_of_4(4444)
     16

     """
    num_1 = num//1000
    num = num - num_1 * 1000

    num_2 = num//100
    num = num - num_2 * 100

    num_3 = num//10
    num = num - num_3 * 10
    return num + num_1 + num_2 + num_3

doctest.testmod()
# print(sum_of_4(1111))


def power(x:int, n: int) -> int:
    product = 1
    if n == 1:
        return x
    elif n == 0:
        return 1
    elif n < 0:
        return 1/power(x, -n)
    else:
        return x * power(x, n-1)


print(power(3, -2))

