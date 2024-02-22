'''
Lab 3: Evaluating Sorting Algorithms.

Test Functions
'''
import time, random
import Lab1_Sorting, Lab2_Quicksort

# 1. Evaluating a single algorithm on one list.
def testonealg(inlist, sortfunc):
    start_time = time.perf_counter()
    sortfunc(inlist)
    end_time = time.perf_counter()
    checksorted(inlist, sortfunc)
    runtime = end_time - start_time
    return round(runtime, 6)

# Check if the list is sorted, if not send error.
def checksorted(inlist, sortfunc):
    i = 0
    for i in range(len(inlist)-1):
        if inlist[i] > inlist[i+1]:
            return "List not sorted using, "+ sortfunc.__name__ + "\nIndex: " + str(i+1) + ", Value: " + str(inlist[i+1]) + " is smaller than the previous index: " + str(i) + ", Value: " + str(inlist[i])
        i += 1
        
# 2. Generate a random list with n integers and k duplicates.        
def randomList(n, k):
    i = 0
    list = []
    for i in range(n-k):
        list.append(random.randint(1, 99))
        i += 1
    j = 0
    for j in range(k):
        duplicate = list.append(list[random.randint(0, (n-k)-1)])
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
    print("lists:")
    printMatrix(lists)
    j = 0
    while j < num:
        print("\nList " + str(j+1) + ":")
        print(testonealg(lists[j], f))
        j += 1
    
# 4. Evaluating different algorithms.
def evaluateAll(n, k, num, funcs):
    i=0
    lists = []
    for i in range(num):
        newlist = randomList(n, k)
        random.shuffle(newlist)
        lists.append(newlist)
        i += 1
    print("lists:")
    printMatrix(lists)
    j = 0
    totalRuntime = 0
    for j in range(len(funcs)-1):
        listsCopy = lists
        print("\nEvaluating Function: " + funcs[j].__name__ + " on " + str(num) + " lists.")
        k = 0
        while k < num:
            runtime = testonealg(listsCopy[k], funcs[j])
            totalRuntime = totalRuntime + runtime
            k += 1
        avgRuntime = totalRuntime/num
        print("Average Runtime of " + funcs[j].__name__ + " is: " + str(avgRuntime) + " seconds.\n")
        j += 1

# Helper method to read list of list easily.
def printMatrix(lists):
    i=0
    for i in range(len(lists)):
        print(lists[i])
        i += 1


#scale evaluator
def evaluateScale():
    parameters = [(100, 20),
                  (1000, 200),
                  (10000, 2000),
                  (100000, 20000)]
    functions = [Lab2_Quicksort.quicksort, Lab2_Quicksort.mergeSort, Lab1_Sorting.heapSort, Lab1_Sorting.insertionSort]
    for (n,k) in parameters:
        evaluateAll(n,k,20,functions)