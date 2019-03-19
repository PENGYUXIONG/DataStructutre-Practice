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
				if i not in visited:
					queue.append(i)
					visited[i] = True
			route.add(vertex_id)
		return route
	# dfs traversal
	def dfs(self, start, route = set(), visited = dict()):
		if start not in self.vertices:
			print('start vertex is not in the graph')
			return
		start_vertex = self.vertices[start]
		route.add(start)
		visited[start] = True
		for i in start_vertex.neighbours:
			if i not in visited:
				route = self.dfs(i, route, visited)
		return route
	# find cycles using dfs
	def detect_cycles(self, cur):
		def find_cycles(cur, visited = [], recur = dict(), cycle = 0):
			cur_ver = self.vertices[cur]
			visited.append(cur)
			recur[cur] = True
			for neighbour in cur_ver.neighbours:
				if neighbour in recur:
					cycle += 1
					continue
				visited, recur, cycle = find_cycles(neighbour, visited, recur, cycle)
			del recur[cur]
			return visited, recur, cycle
		visited, recur, cycle = find_cycles(cur)
		return cycle
	# shortest path, dijkstra
	def find_shortest_path(self, start, dest):
		if start not in self.vertices:
			print('start point is not in the graph')
			return
		if dest not in self.vertices:
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
		if len(queue.heap) == 0 and dest not in distance:
			return []
		route.append(dest)
		while dest != start:
			route.append(distance[dest][0])
			dest = distance[dest][0]
		route.reverse()
		return route
	def bfs_find_shortest_path(self, start, dest):
		visited = []
		parent = dict()
		route = []
		queue = []
		if start not in self.vertices:
			print('start point not in graph')
			return
		if dest not in self.vertices:
			print('dest point not in graph')
			return
		start_vertex = self.vertices[start]
		parent[start] = [start, 0]
		queue.append(start_vertex)
		while queue:
			cur_vertex = queue.pop()
			visited.append(cur_vertex.id)
			for neighbour in cur_vertex.neighbours:
				cost = parent[cur_vertex.id][1] + cur_vertex.neighbours[neighbour]
				if neighbour in visited and parent[neighbour][1] <= cost:
					continue
				new_vertex = self.vertices[neighbour]
				parent[neighbour] = [cur_vertex.id, cost]
				if neighbour == dest:
					break
				queue.append(new_vertex)
		while dest is not start:
			route.append(dest)
			dest = parent[dest][0]
		route.append(start)
		route.reverse()
		return route
	def dfs_find_shortest_path(self, start, dest):
		route = []
		visited, parent = self.inner_dfs(start, dest)
		while dest is not start:
			route.append(dest)
			dest = parent[dest][0]
		route.append(start)
		route.reverse()
		return route
	def inner_dfs(self, start, dest, visited = [], parent = dict()):
		start_vertex = self.vertices[start]
		visited.append(start)
		for neighbour in start_vertex.neighbours:
			cost = None
			if start not in parent:
				cost = start_vertex.neighbours[neighbour]
				parent[start] = [start, 0]
			else:
				cost = start_vertex.neighbours[neighbour] + parent[start][1]
			if neighbour not in visited:
				parent[neighbour] = [start, cost]
			elif parent[neighbour][1] > cost:
				parent[neighbour] = [start, cost]
			else:
				break
			visited, parent = self.inner_dfs(neighbour, dest, visited, parent)
		return visited, parent
	# assume following the basic topological rule
	def topological_sort(self):
		def recur_sort(cur, visited, result):
			visited.append(cur)
			for neighbour in self.vertices[cur].neighbours:
				if neighbour not in visited:
					visited, result = recur_sort(neighbour, visited, result)
			result.insert(0, cur)
			return visited, result
		visited = []
		result = []
		for vertex in self.vertices:
			if vertex not in visited:
				visited, result = recur_sort(vertex, visited, result)
		return result
	# direct acyclic graph shortest path
	def dag_shortest_path(self, start, dest):
		def topological_sort(start):
			def loop(start, visited = [], result = []):
				visited.append(start)
				start_vertices = self.vertices[start]
				for neighbour in start_vertices.neighbours:
					if neighbour not in visited:
						visited, result = loop(neighbour, visited, result)
				result.insert(0, start)
				return visited, result
			visited, result = loop(start)
			return result
		def relax(cur, neighbour, cost, weight):
			cur_ver = self.vertices[cur]
			neighbour_ver = self.vertices[neighbour]
			if neighbour not in weight:
				weight[neighbour] = [cur, cost]
			elif weight[neighbour][1] > cost:
				weight[neighbour] = [cur, cost]
			return weight
		weight = dict()
		weight[start] = [start, 0]
		result = []
		sorted_vertices = topological_sort(start)
		for vertex in sorted_vertices:
			cur = self.vertices[vertex]
			for neighbour in cur.neighbours:
				cost = cur.neighbours[neighbour] + weight[start][1]
				weight = relax(vertex, neighbour, cost, weight)
		while dest is not start:
			result.insert(0, dest)
			dest = weight[dest][0]
		result.insert(0, start)
		return result
	# bellman-ford, did not build a edges container, so negative cycles will cause error
	def general_find_shortest_path(self, start, dest):
		weight = dict()
		result = []
		weight[start] = [start, 0]
		cur = start
		def return_edges(cur, edges = []):
			for neighbour in self.vertices[cur].neighbours:
				if [cur, neighbour, self.vertices[cur].neighbours[neighbour]] not in edges:
					edges.append([cur, neighbour, self.vertices[cur].neighbours[neighbour]])
					edges = return_edges(neighbour, edges)
			return edges
		def check_edges(cur,  weight):
			is_neg_cycles = False
			for neighbour in self.vertices[cur].neighbours:
				cost = weight[cur][1] + self.vertices[cur].neighbours[neighbour]
				if neighbour in weight and weight[neighbour][1] > cost:
					print('detected negative cycles!!!')
					return True
				if neighbour == dest:
					continue
				is_neg_cycles = check_edges(neighbour, weight)
			return is_neg_cycles
		def relax(cur, neighbour, cost, weight):
			if neighbour not in weight:
				weight[neighbour] = [cur, cost]
			elif weight[neighbour][1] > cost:
				weight[neighbour] = [cur, cost]
			return weight
		edges = return_edges(cur)
		for i in range(len(self.vertices)):
			for edge in edges:
				weight = relax(edge[0], edge[1], edge[2], weight)
		if check_edges(cur, weight):
			return
		while dest is not start:
			result.insert(0, dest)
			dest = weight[dest][0]
		result.insert(0, start)
		return result
	def display(self):
		for i in self.vertices:
			print(self.vertices[i].id)
			print(self.vertices[i].neighbours)

new_graph = graph()
new_graph.add_edge(1,2)
new_graph.add_edge(2,6)
new_graph.add_edge(2,7)
new_graph.add_edge(7, 2)
new_graph.add_edge(1,5)
new_graph.add_edge(5,1)
new_graph.add_edge(3,4,2)
new_graph.display()
print(new_graph.bfs(1))
print(new_graph.dfs(1))
print(new_graph.find_shortest_path(1,6))
print(new_graph.bfs_find_shortest_path(1,7))
print(new_graph.dfs_find_shortest_path(1, 7))
print(new_graph.detect_cycles(1))

second_graph = graph()
second_graph.add_edge(5,0)
second_graph.add_edge(5, 3, -2)
second_graph.add_edge(5,2, 4)
second_graph.add_edge(2,3, -10)
second_graph.add_edge(3,2,-1)
second_graph.add_edge(3,1)
second_graph.add_edge(4, 1)
second_graph.add_edge(4, 0)
print(second_graph.topological_sort())
#print(second_graph.dag_shortest_path(5, 3))
print(second_graph.general_find_shortest_path(5, 3))
