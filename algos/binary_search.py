def search_binary(sorted_list,word):
	''' should over ride __contain__ method if we require contain method'''


	low = 0
	high = len(sorted_list)


	while low < high:
		mid = (low + high)//2
		if sorted_list[mid] == word:
			return True
		elif word < sorted_list[mid]:
			# print("going left",mid)
			high = mid-1
		else:
			# print("going right",mid)
			low = mid+1
	return False

import time

def perfomance():
	n = 1024
	while n < 5e7:
		sorted_range= list(range(n))

		now = time.time()
		search_binary(sorted_range,-1)
		done = time.time()
		print(n,(done-now)*1000)
		n *=2
##Insert in bs : replace True with mid and False with negative


perfomance()
# using pthon in operator
# 1024 0.0
# 2048 0.0
# 4096 0.9968280792236328
# 8192 1.0104179382324219
# 16384 0.0
# 32768 0.9968280792236328
# 65536 3.9970874786376953
# 131072 5.982875823974609
# 262144 9.97161865234375
# 524288 15.958070755004883
# 1048576 26.928186416625977
# 2097152 40.89212417602539
# 4194304 57.872772216796875
# 8388608 112.73312568664551
# 16777216 453.8147449493408
# 33554432 1510.2603435516357

#using binary search
# 1024 0.0
# 2048 0.0
# 4096 0.0
# 8192 0.0
# 16384 0.0
# 32768 0.0
# 65536 0.0
# 131072 0.0
# 262144 0.0
# 524288 0.0
# 1048576 0.0
# 2097152 0.0
# 4194304 0.0
# 8388608 0.0
# 16777216 0.0
# 33554432 205.09004592895508
