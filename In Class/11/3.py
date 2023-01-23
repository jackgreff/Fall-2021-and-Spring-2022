mylist = ["action", "western", "romance", "comedy", "horror", "scifi", "documentary", "animation"]


# semi close to bubble
def selection_sort(list1):  # finds the minimum and puts it in front, then range moves to next term and restarts
    for i in range(len(list1)):  # going through the list i times and places the minimum in in the front

        # minimum
        min = "zzz"
        for a in range(i, len(list1)):
            if list1[a] < min:
                min = list1[a]
            print(min)
        print("___")

        # adds minimum to list, removes it for next iteration
        list1.remove(min)
        list1.insert(i, min)
    return list1


def insertion_sort(list1):  #
    for i in range(len(list1)):  # going through the list i times and places the minimum in sortlist
        for a in range(i):  # for every value up until this point, because
            if list1[i] < list1[a]:
                print(f"{list1[i]} is less than {list1[a]}")
                my_value = list1[i]  # stores value, so still knows when removed
                list1.remove(list1[i])  # removes that value so it can be inserted
                list1.insert(a,my_value),  # inserts value to where is less than. Everything before it is sorted, so order will be right

        print(list1)

    return list1


def linear_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return i
    return -1


# print(insertion_sort(mylist))
def binary_search(sorted_list, item):
    left = sorted_list[0:(len(sorted_list) // 2)]
    right = sorted_list[len(sorted_list) // 2:]  # if odd right has extra
    order = 0
    in_list = False
    while True:
        print(order,left,right)
        if len(left) == 1 and left[0] == item:
            in_list = True
            break
        elif len(right) == 1 and right[0] == item:
            order += 1  # if its on the right there's one on the left, so add 1
            in_list = True
            break
        elif len(left) <= 1 and left[0] != item and len(right) <= 1 and right[0] != item:  # not in list
            break

        if item < right[0]:
            right = left[len(left) // 2::]  # if odd right has extra
            left = left[0:(len(left) // 2)]

        else:
            order += len(left)
            left = right[0:(len(right) // 2)]
            right = right[len(right) // 2::]  # if odd right has extra

    if in_list == True:
        return order
    else:
        return -1


# print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],23))
sortlista = [1, 3, 6, 9, 11, 12, 14, 17, 20, 25, 30, 37, 44, 45]
input = 37
theorder = binary_search(sortlista, input)
print(theorder)
print(f"{sortlista[theorder]} = {input} ")

merge1 = [1, 3, 4, 5, 11]
merge2 = [2, 5, 7, 8, 9, 10]


def sorts_2_lists(merge1, merge2):
    combined = []
    while len(merge1 + merge2) != 0:
        if len(merge1) == 0:
            combined = combined + merge2
            merge2.clear()
            break

        if len(merge2) == 0:
            combined = combined + merge1
            merge1.clear()
            break

        print(combined, merge1, merge2)
        if merge1[0] < merge2[0]:
            combined.append(merge1[0])
            merge1.remove(merge1[0])
        elif merge1[0] > merge2[0]:
            combined.append(merge2[0])
            merge2.remove(merge2[0])
        elif merge1[0] == merge2[
            0]:  # since they're identical it shouldn't matter which one is added (other will be next)
            combined.append(merge2[0])
            merge2.remove(merge2[0])
    return combined

print(sorts_2_lists(merge1,merge2))
# def selection_sort()

# print(selection_sort(mylist))
