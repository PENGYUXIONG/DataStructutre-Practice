class Node:
	def __init__(self, data):
		self.data = data
		self.prev = self.next = None
class deque:
	def __init__(self, capacity):
		self.capacity = capacity
		self.front = self.rear = None
	def size(self):
		size = 0
		cur_node = self.front
		while cur_node is not None:
			size = size + 1
			cur_node = cur_node.next
		return size
	def insert_front(self, data):
		# deque is full condition
		if self.capacity == self.size():
			print('deque is full, insertion failed')
			return
		new_node = Node(data)
		# deque is empty condition
		if self.front == None:
			self.front = self.rear = new_node
		else:
			self.front.prev = new_node
			new_node.next = self.front
			self.front = new_node
	def insert_last(self, data):
		# if the deque is full
		if self.capacity == self.size():
			print('deque is full, insertion failed')
			return
		new_node = Node(data)
		# deque is empty condition
		if self.front == None:
			self.front = self.rear = new_node
		else:
			self.rear.next = new_node
			new_node.prev = self.rear
			self.rear = new_node
	def delete_front(self):
		# if the deque is empty
		if self.front == None:
			print('this is an empty queue, deletion failed')
		# if there is only one element in the queue
		elif self.front == self.rear:
			self.front = self.rear = None
		else:
			self.front = self.front.next
			self.front.prev = None
	def delete_last(self):
		# if the deque is empty
		if self.front == None:
			print('this is an empty queue, deletion failed')
		# if there is only one element
		elif self.front == self.rear:
			self.front = self.rear = None
		else:
			self.rear = self.rear.prev
			self.rear.next = None
	def get_front(self):
		if self.front is None:
			print('the deque is empty')
			return
		print(self.front.data)
	def get_rear(self):
		if self.front is None:
			print('the deque is empty')
			return
		print(self.rear.data)
	def erase(self):
		self.front = self.rear = None
	def display(self):
		data_list = []
		cur_node = self.front
		while cur_node is not None:
			data_list.append(cur_node.data)	
			cur_node = cur_node.next
		print(data_list)

new_deque = deque(5)
new_deque.display() 
new_deque.delete_front()
new_deque.delete_last()
new_deque.insert_last(-2)
new_deque.insert_front(0)
new_deque.insert_front(-1)
new_deque.insert_last(1)
new_deque.insert_last(2)
new_deque.display()
new_deque.delete_front()
new_deque.display()
new_deque.get_front()
new_deque.get_rear()
new_deque.erase()
new_deque.display()
