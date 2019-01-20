class circular_queue:
	def __init__(self, size):
		self.size = size
		self.queue = [None for i in range(size)]
		self.front = self.rear = -1

	def enqueue(self, val):
		# check if the queue is full
		if (self.rear + 1) % self.size == self.front:
			print('the queue is full\n')	
			return
		# check if the queue is empty
		elif(self.front == -1):
			self.front = self.rear = 0
			self.queue[0] = val
		else:
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = val
	
	def dequeue(self):
		# check if the queue is empty
		if self.front == -1:
			print('Empty queue, not able to dequeue\n')
			return self.queue
		# check if the queue has only one element
		elif (self.front == self.rear):
			self.queue[self.front] = None
			self.front = self.rear = -1
		else:
			self.queue[self.front] = None
			self.front = (self.front + 1) % self.size
	def display(self):
		# check if the queue is empty
		if (self.rear == -1):
			print('this is a empty queue')
		# check if the queue is full
		elif (self.rear + 1) % self.size == self.front:
			print(self.queue)
		elif self.rear >= self.front:
			print(self.queue[self.front: self.rear + 1])
		else:
			print(self.queue[self.rear: self.front+1])

new_circular_queue = circular_queue(2)
new_circular_queue.dequeue()
new_circular_queue.enqueue(21)
new_circular_queue.enqueue(22)
new_circular_queue.enqueue(23)
new_circular_queue.display()
new_circular_queue.dequeue()
new_circular_queue.display()
new_circular_queue.enqueue(12)
new_circular_queue.display()
new_circular_queue.dequeue()
new_circular_queue.display()
