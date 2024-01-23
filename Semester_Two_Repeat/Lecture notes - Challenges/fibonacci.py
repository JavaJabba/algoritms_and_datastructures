'''
Complexity Analysis Lecture

Variations of the Fibonacci Function to observe and understand complexity.
'''

# First iteration of the function. Binary Recursion. Complexity Omega(2n/2)
def fib1(n):
    if n <= 3:
        return 1
    return fib1(n-1) + fib1(n-2)

# Second iteration of the function. Linear Recursion. Complexity O(n)
def fib(n):
    (a,b) = _fib(n)
    return a

def _fib(n):
    if n == 1:
        return (1,0)
    elif n == 2:
        return (1,1)
    (a,b) = _fib(n-1)
    print (a,b)
    return (a + b, a)

# Example with Matrices. Linear Recursion. Complexity Goal: O(n log n)

def Fibonacci(n):
    matrix = [[1,1], [1,0]] #value of n=1 or n=2
    if n == 1 or n == 2:
        return matrix
    elif n > 2:
        ex = Fibonacci(n//2)
        ex = ex * ex
        if n % 2 == 1:
            newMatrix = []



    
    
    
    

#print(Fibonacci(2))  


def power2(x,n):
    print(str(n) + "\t1st")
    if n == 0:
        return 1
    elif n > 0:
        y = power2(x, n//2)
        print(str(n) + "\tn before check")
        y = y*y
        print(str(y) + "\ty before check")
        if n%2 == 1:
            print(str(n) + "\tn after check")
            y = y*x
            print(str(y) + "\ty after check")
        return y

power2(4,4)