'''Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place

'''

data_input = [3, 4, -1, 1]
data_input = [0,2,1,3]
mins,maxs,counts,sums=1,0,0,0
for data in data_input:
	if data < mins and data >0:
		mins = data

	if data > maxs:
		maxs = data

	if data>0:
		counts +=1
		sums +=data

if maxs == counts:
	maxs +=1

expected = ((mins + maxs)/2 )*(maxs+1-mins)
print(expected - sums)


