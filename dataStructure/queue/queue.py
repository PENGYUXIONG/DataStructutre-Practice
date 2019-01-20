class queue:
	def __init__(self, capacity):
		self.queue = []
		self.capacity = capacity
	def size(self):
		return len(self.queue)
	def enqueue(self, val):
		if self.size() == self.capacity:
			print("queue is full, cannot enqueue")
			return
		self.queue.append(val)
		return self.queue
	def dequeue(self):
		if self.size() == 0:
			print("queue is empty, cannot dequeue")
			return
		self.queue.pop(0)
		return self.queue
	def get_front(self):
		if self.size() == 0:
			print("queue is empty, cannot get front element")
			return
		return self.queue[0]
	def get_rear(self):
		if self.size() == 0:
			print("queue is empty, cannot get rear element")
			return

		return self.queue[self.size()-1]


new_queue = queue(2)
print(new_queue.queue)
new_queue.enqueue(9)
new_queue.enqueue(11)
new_queue.enqueue(13)
print(new_queue.queue)
new_queue.dequeue()
print(new_queue.queue)
print(new_queue.size())
print(new_queue.get_front())
print(new_queue.get_rear())
