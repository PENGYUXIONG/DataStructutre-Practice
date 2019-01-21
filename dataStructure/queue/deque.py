class Deque:
	def __init__(self, capacity):
		self.deque = [None] * capacity
		self.capacity = capacity
		self.front = -1
		self.rear = 0
		self.size = 0
	def insert_front(self, data):
		# if the deque is full
		if self.size == self.capacity:
			print('the deque is full, unable to insert')
			return
		# if the deque is empty
		if self.front == -1:
			self.front = self.rear = 0
			self.deque[self.front] = data
			self.size = 1
			return
		self.front = (self.front-1+self.capacity) % self.capacity
		self.deque[self.front] = data
		self.size = self.size + 1
	def insert_last(self, data):
		# if the deque is full
		if self.size == self.capacity:
			print('the deque is full, unable to insert')
			return
		# if the deque is empty
		if self.front == -1:
			self.front = self.rear = 0
			self.deque[self.front] = data
			self.size = 1
			return
		self.rear = (self.rear+1) % self.capacity
		self.deque[self.rear] = data
		self.size = self.size + 1
	def delete_front(self):
		# if the deque is empty
		if self.front == -1:
			print('the deque is empty, unable to delete')
			return
		self.deque[self.front] = None
		# if the deque has only one item
		if self.rear == self.front:
			self.front = self.rear = -1
			self.size = 0
		self.front = (self.front+1)%self.capacity
		self.size = self.size - 1
	def delete_last(self):
		# if the deque is empty
		if self.front == -1:
			print('the deque is empty, unable to delete')
			return
		self.deque[self.rear] = None
		# if the deque has only one element
		if self.rear == self.front:
			self.front = self.rear = -1
			self.size = 0
		self.rear = (self.rear-1+self.capacity) % self.capacity
	def get_front(self):
		if self.front == -1:
			print('this deque is empty')
			return
		print(self.deque[self.front])
	def get_last(self):
		if self.front == -1:
			print('this deque is empty')
			return
		print(self.deque[self.rear])

new_deque = Deque(5)
print(new_deque.deque)
new_deque.delete_front()
new_deque.delete_last()
new_deque.insert_front(1)
new_deque.insert_last(2)
new_deque.insert_front(0)
new_deque.insert_front(-1)
new_deque.insert_last(3)
new_deque.insert_last(2)
print(new_deque.deque)
new_deque.delete_last()
new_deque.delete_front()
print(new_deque.deque)
new_deque.get_front()
new_deque.get_last()
