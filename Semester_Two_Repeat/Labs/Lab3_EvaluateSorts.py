'''
Lab 3: Evaluating Sorting Algorithms.

Test Functions
'''
import time, random
import Lab1_Sorting

# 1. Evaluating a single algorithm on one list.
def testonealg(inlist, sortfunc):
    start_time = time.perf_counter()
    sortfunc(inlist)
    end_time = time.perf_counter()
    checksorted(inlist, sortfunc)
    return end_time - start_time

# Check if the list is sorted, if not send error.
def checksorted(inlist, sortfunc):
    i = 0
    for i in range(len(inlist)):
        if inlist[i] > inlist[i+1]:
            return "List not sorted using, "+ sortfunc.__name__ + "\nIndex: " + i+1 + "Value: " + inlist[i+1] + "is smaller than the previous index: " + i + "Value: " + inlist[i]
        i += 1
    return "List sorted using, "+ sortfunc.__name__ + "\n" + inlist 
        
# 2. Generate a random list with n integers and k duplicates.        
def randomList(n, k):
    i = 0
    list = []
    for i in range(n-k):
        list.append(random.randint(1, 99))
        i += 1
    j = 0
    for j in range(k):
        duplicate = list[random.randint(0, n-k)]
        list.append(duplicate)
        duplicate = 0
        j += 1
    random.shuffle(list)
    return list

# 3. Evaluating multiple lists.
def evaluate(n, k, num, f):
    i=0
    lists = []
    for i in range(num):
        newlist = randomList(n, k)
        random.shuffle(newlist)
        lists.append(newlist)
        i += 1
    print("Evaluating Function: " + f.__name__ + " on " + str(num) + " lists.")

evaluate(10, 2, 5, Lab1_Sorting.bubbleSort)