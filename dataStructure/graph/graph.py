class vertex:
	def __init__(self, id):
		self.neighbours = dict()
		self.id = id
	def add_neighbour(self, neighbour, weight = 0):
		self.neighbours[neighbour] = weight
	def get_id(self):
		return self.id
	def get_neighbours(self):
		return self.neighbours
	def get_weight(self, vertex_id):
		for i in self.neighbours:
			if i == vertex_id:
				return self.neighbours[i]
		print('no such neighbour vertex')

class min_heap:
	def __init__(self):
		self.heap = []
	def left_child(self, i):
		return 2*i+1
	def right_child(self, i):
		return 2*i+2
	def parent(self, i):
		return i//2
	def fix_heap_up(self, i):
		if i == 0:
			return
		parent = self.parent(i)
		if self.heap[parent][1] > self.heap[i][1]:
			self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
			self.fix_heap_up(parent)
	# min_heapify
	def fix_heap_down(self, i):
		if self.left_child(i) > len(self.heap)-1:
			return
		min = i
		if self.heap[self.left_child(i)][1] < self.heap[min][1]:
			min = self.left_child(i)
		if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)][1] < self.heap[min][1]:
			min = self.right_child(i)
		if min != i:
			self.fix_heap_down(min)
	def extract_min(self):
		if len(self.heap) == 0:
			print('empty heap unable to pop')
			return
		result = self.heap[0]
		del self.heap[0]
		if self.heap:
			self.fix_heap_down(0)
		return result
	def add(self, key, value):
		self.heap.append([key, value])
		self.fix_heap_up(len(self.heap)-1)
class graph:
	def __init__(self):
		self.vertices = dict()
	def add_vertices(self, id):
		new_vertex = vertex(id)
		self.vertices[id] = new_vertex
	def add_edge(self, start, dest, cost = 0):
		start_vertex = None
		dest_vertex = None
		for i in self.vertices:
			if self.vertices[i].id == start:
				start_vertex = self.vertices[i]
			if self.vertices[i].id == dest:
				dest_vertex = self.vertices[i]
		if not start_vertex:
			self.add_vertices(start)
		if not dest_vertex:
			self.add_vertices(dest)
		self.vertices[start].add_neighbour(dest, cost)
	# bfs traversal
	def bfs(self, start, route = set()):
		start_vertex = None
		visited = dict()
		queue = []
		for i in self.vertices:
			if self.vertices[i].id == start:
				start_vertex = self.vertices[i]
		if not start_vertex:
			print('start vertex is not in the graph')
			return
		queue.append(start)
		visited[start] = True
		while queue:
			vertex_id = queue.pop(0)
			for i in self.vertices[vertex_id].neighbours:
				if not visited.has_key(i):
					queue.append(i)
					visited[i] = True
			route.add(vertex_id)
		return route
	# dfs traversal
	def dfs(self, start, route = set(), visited = dict()):
		if not self.vertices.has_key(start):
			print('start vertex is not in the graph')
			return
		start_vertex = self.vertices[start]
		route.add(start)
		visited[start] = True
		for i in start_vertex.neighbours:
			if not visited.has_key(i):
				route = self.dfs(i, route, visited)
		return route
	# shortest path, dijkstra
	def find_shortest_path(self, start, dest):
		if not self.vertices.has_key(start):
			print('start point is not in the graph')
			return
		if not self.vertices.has_key(dest):
			print('dest point is not in the graph')
			return
		distance = dict()
		route = []
		queue = min_heap()
		# relax method for dijkstra
		def relax(v1, v2, cost):
			if v2 not in distance or distance[v2][1] < distance[v1][1] + cost:
				queue.add([v1, v2], distance[v1][1] + cost)
		queue.add([start, start], 0)
		while len(queue.heap) > 0:
			cur = queue.extract_min()
			if cur[0][1] not in distance or distance[cur[0][1]][1] > cur[1]:
				distance[cur[0][1]] = [cur[0][0], cur[1]]
			else:
				continue
			cur_vertex = self.vertices[cur[0][1]]
			for neighbour in cur_vertex.neighbours:
				relax(cur[0][1], neighbour, cur_vertex.neighbours[neighbour])
		if len(queue.heap) == 0 and not distance.has_key(dest):
			return []
		route.append(dest)
		while dest != start:
			route.append(distance[dest][0])
			dest = distance[dest][0]
		route.reverse()
		return route
	def display(self):
		for i in self.vertices:
			print(self.vertices[i].id)
			print(self.vertices[i].neighbours)

new_graph = graph()
new_graph.add_edge(1,2)
new_graph.add_edge(2,6)
new_graph.add_edge(2,7)
new_graph.add_edge(1,5)
new_graph.add_edge(5,1)
new_graph.add_edge(3,4,2)
new_graph.display()
print(new_graph.bfs(1))
print(new_graph.dfs(1))
print(new_graph.find_shortest_path(1,6))
