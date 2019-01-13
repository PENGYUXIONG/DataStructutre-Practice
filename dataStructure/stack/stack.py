class stack:
	def __init__(self):
		self.stack = []
	def isEmpty(self):
		return self.stack == []
	def push(self, item):
		return self.stack.append(item)
	def pop(self):
		return self.stack.pop()
	def peek(self):
		return self.stack[len(self.stack)-1]
	def size(self):
		return len(self.stack)
	def reverse(self):
		if self.isEmpty():
			return "this is an empty stack"
		self.stack.reverse()
		return self.stack
	def recursive_reverse(self):
		if self.isEmpty():
			return self.stack
		temp = self.pop()
		self.recursive_reverse()
		return self.insert_at_bottom(temp)
	def insert_at_bottom(self, temp):
		if self.isEmpty():
			self.push(temp)
			return self.stack
		new_temp = self.pop()
		self.insert_at_bottom(temp)
		self.push(new_temp)
		return self.stack
	def recursive_sort(self):
		if self.isEmpty():
			return self.stack
		temp = self.pop()
		self.recursiver_sort()
		self.recursive_insert(temp)		
	def recursive_sorted_insert(self, temp):
		if self.isEmpty() or self.peek() < temp:
			self.push(temp)
			return self.stack
		new_temp = self.pop()
		self.recursive_sorted_insert(temp)
		self.push(new_temp)
	def delete_mid(self, mid, index=0):
		if self.isEmpty():
			return index
		temp = self.pop()
		index = self.delete_mid(mid, index)
		if index != mid:
			self.push(temp)
		index+=1
		return index
	def temp_stack_sort(self):
		temp_stack = stack()
		while not self.isEmpty():
			top = self.pop()
			while not temp_stack.isEmpty() and temp_stack.peek() > top:
				temp = temp_stack.pop()
				self.push(temp)
			temp_stack.push(top)
		self.stack = temp_stack.stack
		return self.stack

new_stack = stack()
print(new_stack.isEmpty())
new_stack.push(1)
print(new_stack.stack)
new_stack.pop()
print(new_stack.stack)
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
print(new_stack.peek())
print(new_stack.size())

print(new_stack.reverse())

print(new_stack.recursive_reverse())
new_stack.delete_mid(new_stack.size()//2)
print(new_stack.stack)
new_stack.push(10)
new_stack.push(3)
new_stack.push(-2)
new_stack.push(0)
print(new_stack.stack)

print(new_stack.temp_stack_sort())
