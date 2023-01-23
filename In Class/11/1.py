def linear_search (L,e):
    count = 0;
    for i in range(len(L)):
        count += 1
        if L[i] == e:
            return count
    return count

def linear_search_smarter (L,e):
    count = 0;
    for i in range(len(L)):
        count += 1
        if L[i] == e:
            return count
        elif L[i] > e:
            return count

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mylist.sort()

n = 12.5
print(linear_search(mylist,n))
print(linear_search_smarter(mylist,n))

