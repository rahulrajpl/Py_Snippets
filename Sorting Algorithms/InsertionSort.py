import random
import time

def insertion_sort(d):
    start_time = time.time()
    print("Before Sorting:", d)
    for i in range(1,len(d)):
        current_element = d[i]
        current_position = i
        while current_position > 0 and d[current_position-1] > current_element:
            d[current_position] = d[current_position-1]
            current_position -= 1
        d[current_position] = current_element





    #----------------------------
    # for i in range(1,len(d)):
    #     current_value = d[i]
    #     position = i
    #     while position > 0 and d[position-1]>current_value:
    #         d[position] = d[position-1]
    #         position = position - 1
    #     d[position] = current_value
    # ----------------------------
    end_time = time.time()
    print("After Sorting: ", d)
    print("Time taken for the execution: ", str(round(end_time - start_time, 3)), "Seconds")


if __name__ == "__main__":
    insertion_sort(random.sample(range(10),10))