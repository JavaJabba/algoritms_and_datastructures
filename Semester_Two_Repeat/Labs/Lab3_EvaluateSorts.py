'''
Lab 3: Evaluating Sorting Algorithms.

Test Functions
'''
import time

# 1. Evaluating a single algorithm on one list
def testonealg(inlist, sortfunc):
    start_time = time.perf_counter()
    sortfunc(inlist)
    end_time = time.perf_counter()
    checksorted(inlist, sortfunc)
    return end_time - start_time

def checksorted(inlist):
    return