class Node:
	def __init__(self, data, priority):
		self.data = data
		self.prev = None
		self.next = None
		self.priority = priority

class Queue:
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

	def push(self, data, priority):
		# if the queue is full
		if self.size() == self.capacity:
			print('this queue is full')
			return 
		new_node = Node(data, priority)
		# if the queue is empty
		if self.front == None:
			self.front = self.rear = new_node
			return
		# if the new_node has lowest priority
		elif self.front.priority > priority:
			new_node.next = self.front
			self.front.prev = new_node
			self.front = new_node
		# if the new_node has highest priority
		elif self.rear.priority <= priority:
			self.rear.next = new_node
			new_node.prev = self.rear
			self.rear = new_node
		else:
			cur_node = self.front.next
			while cur_node is not self.rear and priority >= cur_node.priority:
				cur_node = cur_node.next
			temp_node = cur_node.prev
			temp_node.next = new_node
			new_node.prev = temp_node
			new_node.next = cur_node
			cur_node.prev = new_node
	
	def peek(self):
		# if the queue is empty
		if self.front is None:
			print('this is an empty queue')
			return
		print('data: ' + str(self.front.data) + 'priority: ' + str(self.front.priority))
	def pop(self):
		# if the queue is empty
		if self.front is None:
			print('this is an empty queue, pop failed')
			return
		# if the queue has only one element
		if self.front == self.rear:
			self.front = self.rear = None
			return
		self.front = self.front.next
		self.front.prev = None
	def display(self):
		data_list = []
		cur_node = self.front
		while cur_node is not None:
			element = []
			element.append(cur_node.priority)
			element.append(cur_node.data)
			data_list.append(element)
			cur_node = cur_node.next
		print(data_list)

new_queue = Queue(5)
new_queue.display()				
new_queue.peek()
new_queue.pop()
new_queue.push(1, 1)
new_queue.display()
new_queue.pop()
new_queue.display()
new_queue.push(1, 1)
new_queue.push(1, -1)
new_queue.push(-1, -1)
new_queue.display()
new_queue.peek()
new_queue.push(2,2)
new_queue.push(3,3)
new_queue.push(4,4)
