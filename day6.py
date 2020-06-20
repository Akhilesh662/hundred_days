'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

'''

def check_recursive(n):
  return check_helper(n,len(n))

def check_helper(s,n):
  if n == 0 or n == 1:
    return 1

  count = 0
  if int(s[n-1])> 0:
    count = check_helper(s,n-1)
  if s[n-1] =='1' or s[n-2]=='2' or int(s[n-1])<7:
    count += check_helper(s,n-2)
  return count

dd = check_recursive("111")
print(dd)