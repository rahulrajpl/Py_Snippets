import random
import time

def selection_sort(d):

    start_time = time.time()  # Timer starts for calculating processing time
    print("Before Sorting:", d)
    d_count = len(d)
    i = 0
    while i < d_count:
        large = d[i]
        for j in range(1, d_count):
            if d[j] > large:
                large = d[j]
        d[d_count-1], d[d.index(large)] = d[d.index(large)], d[d_count-1]
        d_count = d_count - 1

    print("After Sorting: ",d)
    end_time = time.time()  # Timer stops for calculating processing time
    print("Time taken for the execution: ", str(round(end_time - start_time, 3)), "Seconds")


if __name__ == '__main__':
    selection_sort(random.sample(range(10000),10000)) #Random Elements List
