import time
import numpy as np
import sorting_and_searching
import matplotlib.pyplot as plt
import main

L = {"a","b","c","d","e","f","g","h","i","j","k","l","m"}

def display_comparison(L: list):
    len_list = []
    insertion_list = []
    selection_list = []
    bubble_list = []
    dot_sort_list = []

    for i in range(4):
        np.random.shuffle(L)
        L = L[0:i+1]
        len_list.append(i)

        #insertion sort
        time_start = time.time()
        sorting_and_searching.insertion_sort(L)
        end_time = time.time()
        insertion_list.append(end_time-time_start)

        #selection sort
        time_start = time.time()
        sorting_and_searching.selection_sort(L)
        end_time = time.time()
        selection_list.append(end_time-time_start)


        #bubble sort
        time_start = time.time()
        sorting_and_searching.bubble_sort(L)
        end_time = time.time()
        bubble_list.append(end_time-time_start)


        #dot_sort sort
        time_start = time.time()
        L.sort()
        end_time = time.time()
        dot_sort_list.append(end_time-time_start)

    plt.plot(np.array(len_list),np.array(insertion_list))
    plt.plot(np.array(len_list),np.array(selection_list))
    plt.plot(np.array(len_list),np.array(bubble_list))
    plt.plot(np.array(len_list),np.array(dot_sort_list))
    plt.show()

display_comparison(main.read_data())