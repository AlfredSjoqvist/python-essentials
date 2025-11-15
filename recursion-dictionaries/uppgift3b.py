#import sys
#sys.setrecursionlimit(5000)


#def factorial(n=int):
#    if n == 1:
#        return 1
#    else:
#        return n * factorial(n-1)

def special_factorial(n=int, stop_condition=int):
    if n == 0:
        return 1
    if n == stop_condition:
        return stop_condition
    else:
        return n * special_factorial(n-1, stop_condition)


def choose(n=int, k=int):
    if n >= 0 and k >= 0:
        if n == k:
            return 1
        elif (n-k) > k:
            return special_factorial(n, n+1-k)//(special_factorial(k, 1))
        else:
            return special_factorial(n, k+1)//(special_factorial(n-k, 1))





print(choose(0, 0))
print(choose(1, 1))
#print(choose(1000, 1))
#print(choose(52, 5))
#print(choose(1000, 4))
#print(choose(1000, 800))

#print(special_factorial(5, 1))

#import math
#print(math.factorial(1000)//(math.factorial(800)*math.factorial(1000-800)))
