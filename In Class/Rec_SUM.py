def sum_digits (n: int, ssf: int) -> int:
    if n > 0:
        b = n % 10
        print(b)
        ssf = ssf + b
        b + sum_digits((n // 10,ssf))

    return ssf

#print("final sum: "+str(sum_digits(6789, 0)))

def root(squared: int) -> int:
    g = 1
    root_guess(((g + squared/g)/2), squared)
    return g

def root_guess(g: int, squared: int) -> int:

    if abs(g * g - squared) < .01:
        return g
    else:
        root_guess(((g + squared / g) / 2), squared)

#print(root(9))

a = "wrriognhgt"

print(a[1] + a[3] + a[5]+ a[7] + a[9])

print(a[0:int(len(a)/2)]+" "+a[int(len(a)/2)::])

input_a = input("input 1")
input_b = input("input 2")
print(input_a == input_b)
if(input_a < input_b):
    print(input_a+input_b)
else:
    print(input_b+input_a)

