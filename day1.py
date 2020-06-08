'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

'''
from itertools import combinations

def add_to_k(list,k):
	return any(sum(i) == k for i in combinations(list,2))

print(add_to_k([10, 15, 3, 7],20))

