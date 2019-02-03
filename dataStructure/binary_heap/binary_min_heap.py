import heapq

class binary_min_heap:
	def __init__(self):
		self.heap = []
	def insert(self, data):
		heapq.heappush(self.heap, data)
	def parent(self, i):
		return (i-1)//2
	def left_child(self, i):
		return 2*i + 1
	def right_child(self, i):
		return 2*i + 2
	def delete(self, i):
		self.decrease(i, float("-inf"))
		self.extract_min()
	def extract_min(self):
		heapq.heappop(self.heap)	
	def decrease(self, i, new_val):
		self.heap[i] = new_val
		while i is not 0 and self.heap[i] < self.heap[self.parent(i)]:
			self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
			print('index:' + str(i))
	def display(self):
		print(self.heap)

new_heap = binary_min_heap()
new_heap.insert(0)
new_heap.insert(-1)
new_heap.insert(2)
new_heap.insert(3)
new_heap.decrease(2, -12)
new_heap.display()
new_heap.insert(-5)
new_heap.insert(10)
new_heap.insert(6)
new_heap.display()

