class binary_max_heap:
	def __init__(self):
		self.heap = []
	def parent(self, i):
		return (i-1) // 2
	def left_child(self, i):
		return 2*i+1
	def right_child(self, i):
		return 2*i+2
	def increase(self, i, new_val):
		self.heap[i] = new_val
		while i is not 0 and self.heap[i] > self.heap[self.parent(i)]:
			self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
			i = self.parent(i)
	def insert(self, data, i = 0):
		size = len(self.heap)
		left = self.left_child(i)
		right = self.right_child(i)
		if self.heap == [] or self.heap[self.parent(size)] > data:
			self.heap.append(data)
		else:
			self.heap.insert(0, data)
			self.max_heapify()
	def get_max(self):
		print(self.heap[0])
	def extract_max(self):
	 	return self.heap.pop(0)
	def delete(self, i):
		self.increase(i, float('inf'))
		self.extract_max()
	def display(self):
		print(self.heap)
	# not that the heapify is doing simple fixes, clustered arrays cannot be transefered into a max heap successfully
	def max_heapify(self, i = 0):
		print(i)
		size = len(self.heap)
		left = self.left_child(i)
		right = self.right_child(i)
		largest = i
		if left < size and self.heap[left] > self.heap[i]:
			largest = left
		if right < size and self.heap[right] > self.heap[largest]:
			largest = right
		if largest != i:	
			self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
			self.max_heapify(largest)
	# like heapify in heapq, transfer an array into a max heap by calling heapify on parent-nodes
	def build_max_heap(self, input_array):	
		self.heap = input_array
		size = len(input_array)
		while size > 0:
			size = size - 1
			self.max_heapify(size)
	def heap_sort(self, input_array):
		self.build_max_heap(input_array)
		new_array = []
		while self.heap != []:
			new_array.insert(0, self.extract_max())
			self.max_heapify()
		return new_array		

new_max_heap = binary_max_heap()
new_max_heap.insert(0)
new_max_heap.insert(3)
new_max_heap.insert(2)
new_max_heap.insert(-2)
new_max_heap.insert(20)
new_max_heap.insert(-1)
new_max_heap.display()
new_max_heap.delete(3)
new_max_heap.display()
new_max_heap.build_max_heap([-1, -3, -6, 5, 2])
new_max_heap.display()
print(new_max_heap.heap_sort([-5,2,13,1,-2]))
