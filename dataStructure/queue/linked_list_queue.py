class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linked_list_queue:
	def __init__(self, capacity):
		self.front = self.rear = None
		self.capacity = capacity
	def size(self):
		size = 0
		cur_node = self.front
		while cur_node is not None:
			size = size + 1
			cur_node = cur_node.next
		return size
	def enqueue(self, data):
		# empty queue condition
		if self.front == None:
			self.front = self.rear = Node(data)
		# full queue condition
		elif self.size() == self.capacity:
			print('this is full queue, enqueue failed!')
		else:
			new_node = Node(data)
			self.rear.next = new_node
			self.rear = new_node
	def dequeue(self):
		# empty queue condition 
		if self.front == None:
			print('this is an empty queue, dequeue failed')
		# if there is ony one element inside the queue
		elif self.front == self.rear:
			self.front = self.rear = None
		else:
			self.front = self.front.next
	
	def display(self):
		# empty condition
		if self.front == None:
			print('this is an empty queue')
		else:
			data_list = []
			cur_node = self.front
			while cur_node is not None:
				data_list.append(cur_node.data)
				cur_node = cur_node.next
			print(data_list)

new_queue = linked_list_queue(5)
print(new_queue.size())
new_queue.dequeue()
new_queue.enqueue(1)
new_queue.display()
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
new_queue.enqueue(5)
new_queue.enqueue(6)
new_queue.display()
new_queue.dequeue()
new_queue.display()
