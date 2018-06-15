import sys
import random
import time
sys.setrecursionlimit(1500)


def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, p)
        quick_sort2(A, p+1, hi)

def get_pivot(A, low, hi):
    mid = (low + hi) // 2
    s = sorted([A[low], A[mid], A[hi]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    return hi




def partition(A, low, hi):
    pivot_index = get_pivot(A, low, hi)
    pivot_value = A[pivot_index]
    A[pivot_index], A[low] = A[low], A[pivot_index]
    border = low

    for i in range(low, hi+1):
        if A[i] < pivot_value:
            border += 1
            A[i], A[border] = A[border], A[i]
        A[low], A[border] = A[border], A[low]
    return border
#-----------------------------------------------
#Special implementation with minimum lines of code!!
# Function may be studies for minimalised implementatin
# Credits to Original fuction written by a random Youtube user.
def mindblowing_quicksort(d):
    if len(d) < 2:
        return d
    lesser = mindblowing_quicksort([x for x in d[1:] if x <= d[0]])
    bigger = mindblowing_quicksort([x for x in d[1:] if x > d[0]])
    return lesser+[d[0]]+bigger
#-----------------------------------------------

if __name__ == '__main__':

    d = random.sample(range(100000),100000)
    d2 = d[:]
    #print("Before Sorting: ", d)
    #quick_sort(d)
    start_time = time.time()
    mindblowing_quicksort(d)
    #print("After Quick sort ", mindblowing_quicksort(d))
    end_time = time.time()

    print("Time take for the execution: ", str(round(end_time - start_time, 3)), "Seconds")

    start_time = time.time()
    quick_sort(d2)
    end_time = time.time()

    print("Time take for the execution: ", str(round(end_time - start_time, 3)), "Seconds")
