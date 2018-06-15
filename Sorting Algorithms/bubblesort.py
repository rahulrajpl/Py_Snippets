import random
import time


def bubble_sort(d):
    start_time = time.time()  # Timer starts for calculating processing time
    print("Before sorting:", d)
    d_count = len(d)
    i = 0
    while i < d_count:
        for j in range(1, d_count):
            if d[i] > d[j]:
                d[i], d[j] = d[j], d[i]
            i = i+1
        i = 0
        d_count = d_count - 1
    print("After sorting:", d)
    end_time = time.time()  # Timer stops for calculating processing time
    print("Time taken for the Bubble Sort execution: ", str(round(end_time - start_time, 3)), "Seconds")


if __name__ == '__main__':
    bubble_sort(random.sample(range(10000),4000)) #Random Elements List

