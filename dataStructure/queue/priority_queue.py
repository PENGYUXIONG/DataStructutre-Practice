class Node:
	def __init__(self, data, priority):
		self.data = data
		self.priority = priority
		self.next = None
class priority_queue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.front = self.rear = None
	def size(self):
		cur_node = self.front
		size = 0
		while cur_node is not None:
			size = size + 1
			cur_node = cur_node.next
		return size
	def insert(self, data, priority):
		# if the queue is full
		new_node = Node(data, priority)
		if self.size() == self.capacity:
			print('the queue is full, unable to insert!')
			return
		# if the queue is empty
		elif self.front is None:
			self.front = self.rear = new_node
			return
		else:
			cur_node = self.front
			# if did not reach the rear element and the priority is smaller than next element, we need to keep traverse
			while cur_node is not self.rear and cur_node.next.priority >= priority:
				cur_node = cur_node.next
			# if the new_node has least priority
			if cur_node is self.rear and cur_node.priority >= priority:
				cur_node.next = new_node
				self.rear = new_node
				return
			# if the new_node has most priority
			if cur_node is self.front and cur_node.priority < priority:
				new_node.next = self.front
				self.front = new_node
				return
			new_node.next = cur_node.next
			cur_node.next = new_node
	def getHighestPriority(self):
			if self.front is None:
				print('it is an empty queue')
				return
			print('priority: ' + str(self.front.priority), 'data: ' + str(self.front.data))
	def deleteHighestPriority(self):
			if self.front is None:
				print('this is an empty queue, unable to delete')
				return
			if self.front == self.rear:
				self.front = self.rear = None
				return
			self.front = self.front.next	
	def display(self):
		data_list = []
		cur_node = self.front
		while cur_node is not None:
			element = []
			element.append('priority: '+ str(cur_node.priority))
			element.append('data: ' + str(cur_node.data))
			data_list.append(element)
			cur_node = cur_node.next
		print(data_list)

new_queue = priority_queue(5)
new_queue.display()
new_queue.getHighestPriority()
new_queue.deleteHighestPriority()
new_queue.insert(2, 1)
new_queue.insert(3, 1)
new_queue.insert(4, 3)
new_queue.insert(3, 3)
new_queue.display()
new_queue.insert(2, -1)
new_queue.display()
new_queue.insert(10, 2)
new_queue.display()
new_queue.getHighestPriority()
new_queue.deleteHighestPriority()
new_queue.display()
