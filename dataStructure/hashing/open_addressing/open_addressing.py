import random
class hash_table:
	def __init__(self, size):
		self.table_size = size
		self.slots = [None] * size
		self.prime = self.get_prime()
	def size(self):
		size = 0
		for i in self.slots:
			if i:
				size += 1
		return size
	def get_prime(self):
		if self.size < 2:
			print('table size is less than 2, incorrect')
			return
		valid_primes = []
		for i in range(2, self.table_size):
			valid_primes.append(i)
			for num in range(2, i):
				if i % num == 0:
					valid_primes.pop()
					break
		return random.choice(valid_primes)
			
	def hash(self, data):
		return data % self.table_size
	def hash2(self, data):
		return self.prime - (data % self.prime)
	def double_hashing(self, data, count):
		return (self.hash(data) + count * self.hash2(data)) % self.table_size
	def search(self, data):
		count = 1
		hash_key_boolean = false
		while not hash_key_boolean:
			key = self.double_hashing(data, count)
			if self.slots[key] == None:
				print('search failed, something is wrong')
				break
			if self.slots[key] == data:
				return key
	def insert(self, data):
		count = 1
		hash_key_boolean = False
		while not hash_key_boolean:
			key = self.double_hashing(data, count)
			if not self.slots[key]:
				self.slots[key] = data
				hash_key_boolean = True
			count += 1
		if self.size() == self.table_size:
			print('table is full, bigger table required')
			new_table = hash_table(self.table_size * 2)
			for i in self.slots:
				if i:
					new_table.insert(i)
			return new_table
	def delete(self, data):
		count = 1
		hash_key_boolean = False
		while not hash_key_boolean:
			key = self.double_hashing(data, count)
			if self.slots[key] == None:
				print('deletion failed, something is wrong')
				break
			if self.slots[key] == data:
				self.slots[key] = False
				hash_key_boolean = True
			count += 1
		if self.size() < 0.25 * self.table_size:
			print('data is too few, smaller table required')
			new_table = hash_table(self.table_size / 2)
			for i in self.slots:
				if i:
					new_table.insert(i)
			return new_table
	def display(self):
		print(self.slots)

table = hash_table(5)
table.insert(2)
table.insert(7)
table.insert(9)
table.insert(10)
table = table.insert(18)
table.display()
table.delete(2)
table.delete(7)
table.display()
table = table.delete(9)
table.display()
table.insert(20)
table.insert(20)
table.delete(20)
table.insert(2)
table.display()
