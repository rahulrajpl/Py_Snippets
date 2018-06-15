import random
from bubblesort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort

elements = random.sample(range(10000),6000)
elements_1 = elements[:]
elements_2 = elements[:]
bubble_sort(elements) #Random Elements List
selection_sort(elements_1)
insertion_sort(elements_2)