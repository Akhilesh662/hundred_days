'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

'''

# used ap scheduler 

import time

def test():
	print("I am called")


def scheduler(f,n):
	print("i am waiting",time.time())
	time.sleep(n/1000)
	print("i am calling",time.time())
	res = f()
	return res

scheduler(test,2000)

