def fibonacci(n: int) -> int:
    fib_list = [0, 1]

    if n == 1: #don't be zero
        return 0
    elif n == 2:
        return 1
    else:
         for a in range(2, n):
                b = fib_list[-1] + fib_list[-2]
                print("this is b at " + str(a)+" is: " + str(b))
                fib_list.append(b)
                a = b

    return a


# print(fibonacci(5))

def root_guess(g: int, squared: int) -> int:

    while abs(g * g - squared) > .01:
        g = (g + squared/g) / 2
        print(g)
    return round(g)

print(root_guess(100,4))

def sum_digits (n: int) -> int:
    ssf = 0 #sum so far

    while n > 0:

        ssf += n % 10
        n = n // 10
    return ssf

print(sum_digits(6543))