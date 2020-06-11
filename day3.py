'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

#https://www.youtube.com/watch?v=suj1ro8TIVY helpful
'''
class Node:
    def __init__(self, val, left=None, right=None):
    	self.val = val
    	self.left = left
    	self.right = right


def serialize(root):
	if root == None:
		return 'X'
	
	x = "Node('"+root.val +"'"
	if root.left is not None:
		left_serial = serialize(root.left)
		x +=",left="
		x += left_serial 
	
	if root.right is not None:
		right_serial = serialize(root.right)
		x +=",right="
		x += right_serial
	x+=')'	
	return x

def deserialize(str):
	'''str look like proper python code format there is no need to write custom deserialize'''
	return eval(str)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'

