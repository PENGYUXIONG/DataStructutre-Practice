class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linked_list_circular_queue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.front = self.rear = None
	def size(self):
		size = 0
		cur_node = self.front
		if cur_node is None:
			return size
		while cur_node.next is not self.front:
			size = size + 1
			cur_node = cur_node.next
		return size+1
	def enqueue(self, data):
		# empty condition 
		if self.front == None:
			new_node = Node(data)
			self.front = self.rear = new_node
			self.front.next = self.rear
		# full queue condition
		elif self.size() == self.capacity:
			print('the queue is full, queue failed')
		else:
			new_node = Node(data)
			new_node.next = self.front
			self.rear.next = new_node
			self.rear = new_node
	def dequeue(self):
		# empty condition
		if self.front == None:
			print('This is an empty queue, dequeue failed')
		# only one element exist in queue
		elif self.front == self.rear:
			self.front = self.rear = None
		else:
			self.front = self.front.next
			self.rear.next = self.front
	def display(self):
		# empty condition
		if self.front == None:
			print('This is an empty queue')
			return
		cur_node = self.front
		data_list = []
		while cur_node.next is not self.front:
			data_list.append(cur_node.data)
			cur_node = cur_node.next
		data_list.append(cur_node.data)
		print(data_list)

new_circular_queue = linked_list_circular_queue(5)
print(new_circular_queue.size())
new_circular_queue.display()
new_circular_queue.dequeue()
new_circular_queue.enqueue(1)
new_circular_queue.enqueue(2)
new_circular_queue.enqueue(3)
new_circular_queue.enqueue(4)
new_circular_queue.enqueue(5)
new_circular_queue.enqueue(0)
new_circular_queue.display()
new_circular_queue.dequeue()
new_circular_queue.display()
