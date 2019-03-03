class graph:
	def __init__(self):
		self.vertices = []
		self.edge = []
	def add_edge(self, start, dest):
		if start not in self.vertices:
			self.vertices.append(start)
		if dest not in self.vertices:
			self.vertices.append(dest)
		new_edge = [start, dest]
		if new_edge not in self.edge:
			self.edge.append(new_edge)
	def delete_edge(self, start, dest):
		edge = [start, dest]
		for i in range(len(self.edge)):
			if edge[i] == edge:
				self.edge.pop(i)
				return
		print('no such edge exist')
				
	def display(self):
		print(self.vertices)
		print(self.edge)

new_graph = graph()
new_graph.add_edge(1,2)
new_graph.add_edge(2, 3)
new_graph.display()
new_graph.delete_edge(0,1)
new_graph.display()
