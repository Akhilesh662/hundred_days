'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
	2,4,6,2,5
2
4
6
2
5


'''
# Python 3 program to implement above approach
maxLen = 10

# variable to store states of dp
dp = [0 for i in range(maxLen)]

# variable to check if a given state
# has been solved
v = [0 for i in range(maxLen)]

# Function to find the maximum sum subsequence
# such that no two elements are adjacent


def maxSum(arr, i, n):

    # Base case
    if (i >= n):
        return 0

    # To check if a state has
    # been solved
    if (v[i]):
        return dp[i]
    v[i] = 1

    # Required recurrence relation
    step1 = maxSum(arr, i + 1, n)
    step2 = maxSum(arr, i + 2, n)
    current = arr[i]

    dp[i] = max(step1, current + step2)

    # Returning the value
    return dp[i]


arr = [2, 4, 6, 2, 5]

n = len(arr)
print(maxSum(arr, 0, n))
print(dp)
