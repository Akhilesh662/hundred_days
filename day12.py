'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
'''



def is_reached(i,n):
    return i== n


n_ways = 0
def climbup(i,n):
    global n_ways
    if i > n:
        return False

    if is_reached(i,n):
        n_ways = n_ways+1
        return True
    climbup(i+1,n)
    climbup(i+2,n)
    return n_ways


for i in range(1,10):
    print(i,climbup(0,i))
    n_ways = 0



## found pattern of fibonacci 
## better ways is solve using fib n-1, fib n-2
