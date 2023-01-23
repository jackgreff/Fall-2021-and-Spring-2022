def merge_sort(list):
    if len(list) > 1:#I use this so I don't have to do another elif with list lengths of 2,1, can be processed with main if statement
        list1 = list[0:len(list)//2]
        list2 = list[len(list)//2::]
    else:
        return list

    if len(list1) >= 1 and len(list2) >= 1:
        merge_list_1 = merge_sort(list1)
        merge_list_2 = merge_sort(list2)
        #sorts two lists
        combined = []
        while len(merge_list_1 + merge_list_2) != 0:
            if len(merge_list_1) == 0:
                combined = combined + merge_list_2
                break
            if len(merge_list_2) == 0:
                combined = combined + merge_list_1
                break

            if merge_list_1[0] < merge_list_2[0]:
                combined.append(merge_list_1[0])
                merge_list_1.remove(merge_list_1[0])
            else:
                combined.append(merge_list_2[0])
                merge_list_2.remove(merge_list_2[0])
        return combined
    elif len(list1) == 1 and len(list2) == 1:
        if list1[0] > list2[0]:
            return list2+list1
        else: #if equal either can be first
            return list1+list2
    elif len(list2) == 1 and len(list2) == 0:
        return list1
    elif len(list2) == 0 and len(list2) == 1:
        return list2
list1 = [12,2,10,4,8,5,7,1,3,6,9,11]

print(merge_sort(list1))