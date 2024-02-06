'''
Lecture Notes: Merge Sort
'''

def mergeSort(myList):
    n = len(myList)
    if n > 1:
        list1 = myList[:n//2]
        list2 = myList[n//2:]
        mergeSort(list1)
        mergeSort(list2)
        merge(list1, list2, myList)


def merge(list1, list2, myList):
    f1 = 0  #pointer1
    f2 = 0  #pointer2
    while f1 + f2 < len(myList):
        if f1 == len(list1) or list2[f2] < list1[f1]:
            myList[f1+f2] = list2[f2]
            f2 += 1
        else:
            myList[f1+f2] = list1[f1]
            f1 += 1           
    

