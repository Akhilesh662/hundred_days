'''

from MIT Algo lecture 20
1 ) define subproblems
2 ) guess part of solution
3 ) relate sub problem solution
4 ) recurse and memoize  OR build a table bottom up (for loop )
5 ) solve the original problem




'''
def febv2(n):
    for i in range(1,n+1):
        if i < 2:
            l1= l2 = 1
        else:
            l1,l2 = l2, l1+l2
        return l2

memo = {}
def feb(n):
    if n in memo:
        return memo[n]
    if n < 2:
        f =1
    else:
        f = feb(n-1) + feb(n-2)
    memo[n] = f
    return f

