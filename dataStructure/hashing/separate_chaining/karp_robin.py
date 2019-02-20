class hash_str:
	def __init__(self):
		self.string = 0
		self.hash_str = 0
		self.base = 256
		self.length = 0
	def append(self, char):
		self.string = self.base * self.string + ord(char)
		self.hash_str = (self.hash_str * self.base + ord(char)) % 101
		self.length += 1
	def skip(self, char):
		if self.length == 0:
			print('empty string, unable to skip')
			return
		self.string = self.string - ord(char) * self.base**(self.length-1)
		self.hash_str = (self.hash_str - ord(char) * self.base ** (self.length-1)) % 101
		self.length -= 1

def karp_rabin(string, pattern):
	hash_pattern = hash_str()
	hash_string = hash_str()
	for i in range(len(pattern)):
		hash_pattern.append(pattern[i])
	for c in string[:len(pattern)]:
		hash_string.append(c)
	if hash_string.hash_str == hash_pattern.hash_str:
		return True
	for i in range(len(pattern), len(string)):
		hash_string.skip(string[i-len(pattern)])
		hash_string.append(string[i])
		if hash_string.hash_str == hash_pattern.hash_str:
			return True

print(karp_rabin('tiesak', 'as'))
