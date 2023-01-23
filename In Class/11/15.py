import numpy as np
import matplotlib.pyplot as plt

list1 = [5, 4, 3, 2, 1]
list2 = [10, 9, 8, 7, 6]
ar = np.array([list1, list2])
print(ar)
line = np.linspace(-10, 10, 5)
print(line)

v = np.array([1, 2, 3])
u = np.array([4, 5, 6])
print(v * u)
print(np.sum(np.array([1, 2, 3]) * np.array([4, 5, 6])))

arr = np.array([0, -1, -2, -3, -4, -5, -6, -7, -8, -9])
mask = (arr % 2 == 0)
print(arr[mask])

my_arr = np.random.random(10)
mask_1 = my_arr > .5
# print(my_arr)
# print(my_arr[mask_1])
print(np.mean(my_arr[0:len(my_arr) // 2]), np.mean(my_arr[len(my_arr) // 2::]))

arr_2 = my_arr - np.mean(my_arr)
arr_3 = np.mean(arr_2 ** 2)
print(arr_3)
print(np.var(arr))

x = np.linspace(-5, 10, 100)
y = 1 / (x + 1)
plt.plot(x, y, linewidth=4,title="1/(x+1)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
