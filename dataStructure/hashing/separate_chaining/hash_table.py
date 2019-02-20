# implement with table doubling method to handle hash table size
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class hash_table:
	def __init__(self, size):
		self.table_size = size
		self.slots = [None] * size
	def size(self):
		size = 0
		for i in self.slots:
			while i is not None:
				size += 1
				i = i.next
		return size
	def isFull(self):
		if self.size() == self.table_size:
			return True
		return False
	def isEmpty(self):
		if self.size() == 0:
			return True
		return False
	def customize_hash(self, data):
		return data % self.table_size
	def insert(self, data):
		if self.isFull():
			print('full slot, unable to insert, need new table')
			new_table = hash_table(self.table_size * 2)
			for x in self.slots:
				while x is not None:
					new_table.insert(x.data)
					x = x.next
			new_table.insert(data)
			return new_table
		key = self.customize_hash(data)
		new_node = Node(data)
		if not self.slots[key]:
			self.slots[key] = new_node
		else:
			cur_node = self.slots[key]
			while cur_node.next is not None:
				if cur_node.data == data:
					return
				cur_node = cur_node.next
			cur_node.next = new_node
	def delete(self, data):
		if self.isEmpty():
			print('empty slot unable to delete')
			return
		if self.size() < 0.25 * self.table_size:
			print('too many slots, need smaller table')
			new_table = hash_table(self.table_size/2)
			for x in self.slots:
				while x is not None:
					new_table.insert(x.data)
					x = x.next
			new_table.delete(data)
			return new_table
		key = self.customize_hash(data)
		cur_node = self.slots[key]
		if cur_node is None:
			print('key does not exist, cannot delete')
		else:
			if cur_node.next is None:
				if cur_node.data == data:
					self.slots[key] = None
				else:
					print('key does not exist, cannot delete')
				return
			while cur_node.next is not None:
				if cur_node.next.data == data:
					cur_node.next = cur_node.next.next
					return
				cur_node = cur_node.next
			print('key does not exist, cannot delete')
	def display(self):
		for node in self.slots:
			slot = []
			while node is not None:
				slot.append(node.data)
				node = node.next
			print(slot)						
new_table = hash_table(8)
new_table.insert(1)
new_table.insert(2)
new_table.insert(-1)
new_table.insert(9)
new_table.insert(0)
new_table.insert(11)
new_table.insert(1)
new_table.insert(-2)
new_table.insert(20)
new_table = new_table.insert(23)
new_table.display()
new_table.delete(-1)
new_table.delete(2)
new_table.delete(0)
new_table.delete(9)
new_table.delete(11)
new_table.delete(-2)
new_table = new_table.delete(23)
new_table.display()

