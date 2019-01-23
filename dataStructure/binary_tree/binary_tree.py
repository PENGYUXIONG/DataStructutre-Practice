class Node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

class Binary_Tree:
	def __init__(self):
		self.root = None
	def add_left(self, data, node):
		if self.root is None:
			print('it is an empty tree, define root first')
			return
		node.left = Node(data)
	def add_right(self, data, node):
		if self.root is None:
			print('it is an empty tree, define root first')
			return
		node.right = Node(data)
	def delete_left(self, node):
		if self.root is None:
			print('empty tree, unable to delete')
			return
		elif self.left == None:
			print('dont have a left child')
		node.left = None
	def delete_right(self, node):
		if self.root is None:
			print('empty tree, unable to delete')
			return
		elif self.right == None:
			print('dont have a right child')
		node.right = None

def in_order_traversal(root, data_list = []):
	if root:
		in_order_traversal(root.left)
		data_list.append(root.data)
		in_order_traversal(root.right)
	return data_list

def pre_order_traversal(root, data_list = []):
	if root:
		data_list.append(root.data)
		pre_order_traversal(root.left)
		pre_order_traversal(root.right)
	return data_list

def post_order_traversal(root, data_list = []):
	if root:
		post_order_traversal(root.left)
		post_order_traversal(root.right)
		data_list.append(root.data)
	return data_list

def breadth_first_traversal(root):
	if root:
		level = get_level(root)
		print_node(root, level)

def get_level(root, level = 0):
	if root is None:
		return level
	level = level + 1
	left = get_level(root.left, level)
	right = get_level(root.right, level)
	if left > right:
		return left
	return right

def print_node(root, level, level_list=[]):
	counter = 0
	while counter < level:
		counter = counter + 1
		level_list.append(get_node_in_level(root, counter, []))
	print(level_list)
	return level_list

def get_node_in_level(root, level, node_list= []):
	if level == 0:
		return node_list
	elif level == 1:
		node_list.append(root.data)
		return node_list
	else:
		get_node_in_level(root.left, level-1, node_list)
		get_node_in_level(root.right, level-1, node_list)
		return node_list

def get_ancestors(root, data, ancestors):
	if root is None:
		return False
	elif root.data == data:
		return True
	elif get_ancestors(root.left, data, ancestors) or get_ancestors(root.right, data, ancestors):
		ancestors.append(root.data)
		return True
	return False

def is_subtree(root, root2):
	if root is None and root2 is not None:
		return False
	elif root.data == root2.data:
		return is_identical(root, root2)
	else:
		is_subtree(root.left, root2)
		is_subtree(root.right, root2)

def is_identical(root, root2):
	if root == root2 == None:
		return True
	elif root is None or root2 is None:
		return True
	elif root.data == root2.data:
		return is_identical(root.left, root2.left) & is_identical(root.right, root2.right)
	return False

'''
build a perfect three layer tree
	1
      /  \
     2    3
    / \  / \
   4  5 6   7
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

'''
build a perfect two layer tree
	1
      /   \
     2     3
'''

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)


'''
build a full binary tree
	1
       / \
      3   3
'''

root3 = Node(1)
root3.left = Node(3)
root3.right = Node(3)


print(in_order_traversal(root))
print(pre_order_traversal(root))
print(post_order_traversal(root))

print(get_level(root))
breadth_first_traversal(root)
ancestors = []
print(get_ancestors(root, 7, ancestors))
print(ancestors)

print(is_subtree(root, root2))
print(is_subtree(root, root3))
print(is_subtree(root2, root3))
