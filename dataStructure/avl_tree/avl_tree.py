class Node:
	def __init__(self, data):
		self.data = data
		self.height = 0
		self.left = self.right = None
		self.num = 1

class AVL_Tree:
	def __init__(self):
		self.root = None
	
	def insert(self, data, cur_node):
		new_node = Node(data)
		if self.root is None:
			self.root = new_node
			return
		elif cur_node is None:
			return new_node
		elif cur_node.data < data:
			cur_node.right = self.insert(data, cur_node.right)
		elif cur_node.data > data:
			cur_node.left = self.insert(data, cur_node.left)
		elif cur_node.data == data:
			# if duplicate node, just increase counter by one
			cur_node.num = cur_node.num + 1
			return cur_node
		# set level for each node
		cur_node.height = self.get_level(cur_node)

		return self.fix_avl_tree(cur_node, data)

	def get_min_node(self, cur_node):
		while cur_node.left is not None:
			cur_node = cur_node.left
		return cur_node

	def delete(self, data, cur_node):
		if self.root is None:
			print('the avl tree is empty, unable to delete')
			return
		elif self.root.left is None and self.root.right is None:
			if self.root.num > 1:
				self.root.num = self.root.num - 1
			else:
				self.root = None
			return
		elif cur_node.data < data:
			cur_node.right = self.delete(data, cur_node.right)
			return cur_node
		elif cur_node.data > data:
			cur_node.left = self.delete(data, cur_node.left)
			return cur_node
		elif cur_node.data == data:
			if cur_node.num > 1:
				cur_node.num = cur_node.num - 1
				return cur_node
			else:
				if cur_node.right is not None:
					temp = self.get_min_node(cur_node.right)
					cur_node.data = temp.data
					cur_node.num = temp.num
					cur_node.right = self.delete(temp.data, cur_node.right)
				elif cur_node.left is not None:
					return cur_node.left
	
	def fix_avl_tree(self, cur_node, data):
		# check if the tree follows the AVL balance
		balance = self.get_balance(cur_node)
		# check tree's type
		# left left type or left type
		if balance > 1 and data < cur_node.left.data:
			return self.right_rotation(cur_node)

		# left right type
		if balance > 1 and data > cur_node.left.data:
			cur_node.left = self.left_rotation(cur_node.left)
			return self.right_rotation(cur_node)

		# right right type or right type
		if balance < -1 and data > cur_node.right.data:
			return self.left_rotation(cur_node)
		# right left type
		if balance < -1 and data < cur_node.right.data:
			cur_node.right = self.right_rotation(cur_node.right)
			return self.left_rotation(cur_node)
		return cur_node
	
	def left_rotation(self, cur_node):
		if cur_node is self.root:
				self.root = cur_node.right

		new_top = cur_node.right
		old_left = new_top.left
		cur_node.right = old_left
		new_top.left = cur_node
		new_top.height = self.get_level(new_top)
		cur_node.height = self.get_level(cur_node)
		
		return new_top

	def right_rotation(self, cur_node):
		if cur_node is self.root:
			self.root = cur_node.left

		new_top = cur_node.left
		old_right = new_top.right
		cur_node.left = old_right
		new_top.right = cur_node

		new_top.height = self.get_level(new_top)
		cur_node.height = self.get_level(cur_node)

		return new_top

	def get_level(self, cur_node):
		if not cur_node:
			return -1
		level =  max(self.get_level(cur_node.left), self.get_level(cur_node.right)) + 1
		return level
	
	def get_balance(self, cur_node):
		if not cur_node:
			return 0
		balance = self.get_level(cur_node.left) - self.get_level(cur_node.right)
		return balance

	def inorder_traversal(self, cur_node, data_list = []):
		if self.root is None:
			print('empty tree, unable to traversal')
			return
		elif cur_node is None:
			return data_list
		else:
			self.inorder_traversal(cur_node.left, data_list)
			data_list.append(cur_node.data)
			self.inorder_traversal(cur_node.right, data_list)
		return data_list
