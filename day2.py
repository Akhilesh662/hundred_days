'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

'''

from functools import reduce

def product_array(given_array):
	result = []
	for i in range(len(given_array)):
		left, right = given_array[0:i], given_array[i+1:]
		result.append(reduce(lambda x,y: x*y,left+right))
	return result

print(product_array([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
print(product_array([3,2,1])) #[2, 3, 6]
