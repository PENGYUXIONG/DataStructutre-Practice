class Node:
	def __init__(self, data):
		self.data = data
		self.color = 'red'
		self.parent = None
		self.count = 1
		self.left = self.right = None


class red_black_tree:
	def __init__(self):
		self.root = None

	def get_min_child(self, cur_node):
		while cur_node.left is not None:
			cur_node = cur_node.left
		return cur_node

	def get_uncle_node(self, cur_node):
		if cur_node.parent is None or cur_node.parent.parent is None:
			print('parent node or grandparent node not exist, uncle does not exist')
			return
		elif cur_node.parent.data < cur_node.parent.parent.data:
			return cur_node.parent.parent.right
		elif cur_node.parent.data > cur_node.parent.parent.data:
			return cur_node.parent.parent.left

	def insert(self, data, cur_node):
		new_node = Node(data)
		
		if self.root is None:
			self.root = new_node
			self.root.color = 'black'
			return
		while cur_node is not None:
			if data < cur_node.data:
				if cur_node.left is None:
					new_node.parent = cur_node
					cur_node.left = new_node
					cur_node = new_node
					break
				cur_node = cur_node.left
			elif data > cur_node.data:
				if cur_node.right is None:
					new_node.parent = cur_node
					cur_node.right = new_node
					cur_node = new_node
					break
				cur_node = cur_node.right
			elif data == cur_node.data:
				cur_node.count = cur_node.count + 1
				return
		
		# root is black, if the parent node exist and is red, the node should also have grandparent node
		if cur_node.parent and cur_node.parent.color == 'red':
			self.fix_red_black_tree(cur_node)

	def delete(self, data, cur_node):
		while cur_node is not None:
			if cur_node.data > data:
				cur_node = cur_node.left
			elif cur_node.data < data:
				cur_node = cur_node.right
			elif cur_node.data == data and cur_node.count > 1:
				cur_node.count = cur_node.count - 1
				return
			elif cur_node.data == data and cur_node.count == 1:
				break
		if not cur_node:
			print('no such node')
			return
		parent_node = cur_node.parent
		if cur_node.left is not None and cur_node.right is not None:
			child_node = self.get_min_child(cur_node.right)
			cur_node.data = child_node.data
			if child_node.parent.data > child_node.data:
				child_node.parent.left = self.delete_node(cur_node.data, child_node)
			elif child_node.parent.data <= child_node.data:
				child_node.parent.right = self.delete_node(cur_node.data, child_node)
		elif not parent_node:
			self.root = self.delete_node(data, cur_node)
		elif parent_node.data > cur_node.data:
			parent_node.left = self.delete_node(data, cur_node)
		elif parent_node.data < cur_node.data:
			parent_node.right = self.delete_node(data, cur_node)
	
	def get_sibling(self, cur_node):
		if not cur_node:
			print('node is none, error')
			return
		elif cur_node.data <= cur_node.parent.data:
			return cur_node.parent.right
		elif cur_node.data > cur_node.parent.data:
			return cur_node.parent.left

	def delete_node(self, data, cur_node):
		if not cur_node.parent:
			if cur_node.left is not None:
				cur_node.left.color = 'black'
				cur_node.left.parent = None
				return cur_node.left
			elif cur_node.right is not None:
				cur_node.right.color = 'black'
				cur_node.right.parent = None
				return cur_node.right
		elif cur_node.left is not None:
			if cur_node.left.color == 'red' or cur_node.color == 'red':
				cur_node.left.parent = cur_node.parent
				cur_node.left.color = 'black'
			elif cur_node.color == 'black' and cur_node.left.color == 'black':
				self.black_node_operation(cur_node)
				cur_node.left.parent = cur_node.parent
			return cur_node.left
		elif cur_node.right is not None:
			if cur_node.right.color == 'red' or cur_node.color == 'red':
				cur_node.right.parent = cur_node.parent
				cur_node.right.color = 'black'
			elif cur_node.color == 'black' and cur_node.right.color == 'black':
				self.black_node_operation(cur_node)
				cur_node.right.parent = cur_node.parent
			return cur_node.right
		else:
			if cur_node.color == 'black':
				self.black_node_operation(cur_node)

	def black_node_operation(self, cur_node):
		sibling_node = self.get_sibling(cur_node)
		parent_node = cur_node.parent
		grandparent_node = cur_node.parent.parent
		if sibling_node.color == 'black':
			if not sibling_node.left and not sibling_node.right:
				sibling_node.color = 'red'
				if parent_node is not self.root:
					self.black_node_operation(parent_node)
			elif sibling_node.left is not None and sibling_node.left.color == 'red':
				if not grandparent_node:
					if cur_node.data > parent_node.data:
						self.right_rotate(parent_node)
					else:
						parent_node.right = self.right_rotate(sibling_node)
						parent_node.right.parent = parent_node
						self.left_rotate(parent_node)
				elif parent_node.data < grandparent_node.data:
					# left left
					if cur_node.data > parent_node.data:
						grandparent_node.left = self.right_rotate(parent_node)
						grandparent_node.left.parent = grandparent_node
					# right left
					else:
						parent_node.right = self.right_rotate(sibling_node)
						parent_node.right.parent = parent_node
						grandparent_node.left = self.left_rotate(parent_node)
						grandparent_node.left.parent = grandparent_node
				else:
					# left left
					if cur_node.data > parent_node.data:
						grandparent_node.right = self.right_rotate(parent_node)
						grandparent_node.right.parent = grandparent_node
					# right left
					else:
						parent_node.right = self.right_rotate(sibling_node)
						parent_node.right.parent = parent_node
						grandparent_node.right = self.left_rotate(parent_node)
						grandparent_node.right.parent = grandparent_node
				parent_sibling = self.get_sibling(parent_node)
				parent_sibling.color = 'black'
					
			elif sibling_node.right is not None and sibling_node.right.color == 'red':
				if not grandparent_node:
					if cur_node.data > parent_node.data:
						parent_node.left = self.left_rotate(sibling_node)
						parent_node.left.parent = parent_node
						self.right_rotate(parent_node)
					else:
						self.left_rotate(parent_node)
				elif parent_node.data < grandparent_node.data:
					# left right
					if cur_node.data > parent_node.data:
						parent_node.left = self.left_rotate(sibling_node)
						parent_node.left.parent = parent_node
						grandparent_node.left = self.right_rotate(parent_node)
						grandparent_node.left.parent = grandparent_node
					# right right
					else:
						grandparent_node.left = self.left_rotate(parent_node)
						grandparent_node.left.parent = grandparent_node
				else:
					# left right
					if cur_node.data > parent_node.data:
						parent_node.left = self.left_rotate(sibling_node)
						parent_node.left.parent = parent_node
						grandparent_node.right = self.right_rotate(parent_node)
						grandparent_node.right.parent = grandparent_node
					# right right
					else:
						grandparent_node.right = self.left_rotate(parent_node)
						grandparent_node.right.parent = grandparent_node
				parent_sibling = self.get_sibling(parent_node)
				parent_sibling.color = black
			else:
				sibling_node.color = 'red'
				if parent_node is not self.root:
					self.black_node_operation(parent_node)
		else:
			if not grandparent_node:
				if cur_node.data > parent_node.data:
					self.right_rotate(parent_node)
				else:
					self.left_rotate(parent_node)
			elif parent_node.data < grandparent_node.data:
				# left case
				if cur_node.data > parent_node.data:
					grandparent_node.left = self.right_rotate(parent_node)
					grandparent_node.left.parent = grandparent_node
				# right case
				else:
					grandparent_node.left = self.left_rotate(parent_node)
					grandparent_node.right.parent = grandparent
			else:
				# left case
				if cur_node.data > parent_node.data:
					grandparent_node.right = self.right_rotate(parent_node)
					grandparent_node.right.parent = grandparent_node
				# right case
				else:
					grandparent_node.right = self.left_rotate(parent_node)
					grandparent_node.right.parent = grandparent_node
			parent_node.color, sibling_node.color = sibling_node.color, parent_node.color

	def fix_red_black_tree(self, cur_node):
		if cur_node.parent == self.root:
			return
		uncle_node = self.get_uncle_node(cur_node)
		if uncle_node and uncle_node.color == 'red':
			cur_node.parent.color = 'black'
			uncle_node.color = 'black'
			if cur_node.parent.parent != self.root:
				cur_node.parent.parent.color = 'red'
				self.fix_red_black_tree(cur_node.parent.parent)
		else:
			grandparent_node = cur_node.parent.parent
			parent_node = cur_node.parent
			ancestor_node = grandparent_node.parent
			# left
			if parent_node.data < grandparent_node.data:
				# left
				if cur_node.data < parent_node.data:
					if not ancestor_node:
						self.right_rotate(grandparent_node)
					elif ancestor_node.data > grandparent_node.data:
						ancestor_node.left = self.right_rotate(grandparent_node)
						ancestor_node.left.parent = ancestor_node
					elif ancestor_node.data < grandparent_node.data:
						ancestor_node.right = self.right_rotate(grandparent_node)
						ancestor_node.right.parent = ancestor_node
				# right					
				elif cur_node.data > parent_node.data:
					grandparent_node.left = self.left_rotate(parent_node)
					grandparent_node.left.parent = grandparent_node
					if not ancestor_node:
						self.right_rotate(grandparent_node)
					elif ancestor_node.data > grandparent_node.data:
						ancestor_node.left = self.right_rotate(grandparent_node)
						ancestor_node.left.parent = ancestor_node
					elif ancestor_node.data < grandparent_node.data:
						ancestor_node.right = self.right_rotate(grandparent_node)
						ancestor_node.right.parent = ancestor_node
			# right
			elif parent_node.data > grandparent_node.data:
				# left
				if cur_node.data < parent_node.data:
					grandparent_node.right = self.right_rotate(parent_node)
					grandparent_node.right.parent = grandparent_node
					if not ancestor_node:
						self.left_rotate(grandparent_node)
					elif ancestor_node.data > grandparent_node.data:
						ancestor_node.left =  self.left_rotate(grandparent_node)
						ancestor_node.left.parent = ancestor_node
					elif ancestor_node.data < grandparent_node.data:
						ancestor_node.right = self.left_rotate(grandparent_node)
						ancestor_node.right.parent = ancestor_node
				# right
				elif cur_node.data > parent_node.data:
					if not ancestor_node:
						self.left_rotate(grandparent_node)
					elif ancestor_node.data > grandparent_node.data:
						ancestor_node.left = self.left_rotate(grandparent_node)					
						ancestor_node.left.parent = ancestor_node
					elif ancestor_node.data < grandparent_node.data:
						ancestor_node.right = self.left_rotate(grandparent_node)
						ancestor_node.right.parent = ancestor_node
	def left_rotate(self, cur_node):
		if cur_node == self.root:
			self.root = cur_node.right
			self.root.parent = None

		new_top = cur_node.right
		old_left = new_top.left
		
		cur_node.right = old_left
		new_top.left = cur_node

		if old_left:
			old_left.parent = cur_node
		cur_node.parent = new_top		

		new_top.color, cur_node.color = cur_node.color, new_top.color

		return new_top

	def right_rotate(self, cur_node):
		if cur_node == self.root:
			self.root = cur_node.left
			self.root.parent = None
		
		new_top = cur_node.left
		old_right = new_top.right

		cur_node.left = old_right
		new_top.right = cur_node
		if old_right:	
			old_right.parent = cur_node
		cur_node.parent = new_top

		new_top.color, cur_node.color = cur_node.color, new_top.color		

		return new_top

	def inorder_traversal(self, cur_node, data_list = []):
		if cur_node is None:
			return
		else:
			if cur_node.left is not None and cur_node.left.parent is not cur_node:
				print('cur_node: ' + str(cur_node.data) + 'has wrong left child')
			if cur_node.right is not None and cur_node.right.parent is not cur_node:
				print('cur_node: ' + str(cur_node.data) + 'has wrong right child')
			self.inorder_traversal(cur_node.left, data_list)
			data_list.append(cur_node.data)
			self.inorder_traversal(cur_node.right, data_list)
		return data_list
