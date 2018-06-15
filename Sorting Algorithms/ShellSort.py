import random
import time

def shell_sort(d):
    start_time = time.time()
    print("Before Sorting:", d)

    sublistcount = len(d) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(d, startposition, sublistcount)
        print("After increment of size", sublistcount, "the List is", d)
        sublistcount = sublistcount //2

    end_time = time.time()
    print("After Sorting: ", d)
    print("Time taken for the execution: ", str(round(end_time - start_time, 3)), "Seconds")

def gap_insertion_sort(d, start, gap):
    for i in range(start+gap, len(d), gap):
        current_value = d[i]
        current_position = i

        while (current_position>gap) and d[current_position-gap] > current_value:
            d[current_position] = d[current_position-gap]
            current_position = current_position - gap

        d[current_position] = current_value

if __name__ == "__main__":
    shell_sort(random.sample(range(100),11))
