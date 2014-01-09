import sys

#-*- coding:utf-8 -*-

# module that implements graphs and checks some properties 
# author: Marcos Castro

class Node:

	def __init__(self, key):
		self.key = key
		self.neighbors = []
		self.visited = False
	
	def get_key(self):
		return self.key
	
	def set_key(self, new_key):
		self.key = new_key
	
	# neighbors successors
	def add_neighbor(self, node):
		if self.exist_neighbor(node.get_key()) == False:
			self.neighbors.append(node)
			return True
		return False

	def remove_neighbor(self, node):
		if self.exist_neighbor(node.get_key()) == True:
			for i in range(0, len(self.neighbors)):
				if self.neighbors[i].get_key() == node.get_key():
					self.neighbors.pop(i)
					return True
		return False
	
	def get_neighbors(self):
		return self.neighbors
	
	def exist_neighbor(self, key):
		for i in range(0, len(self.neighbors)):
			if self.neighbors[i].get_key() == key:
				return True
		return False
	
	def get_neighbor_pos(self, key):
		for i in range(0, len(self.neighbors)):
			if self.neighbors[i].get_key() == key:
				return i
		return -1

	def is_visited(self):
		return self.visited 

	def set_visited(self, visited):
		self.visited = visited

class Edge:

	def __init__(self, node_source, node_destination, weight = 0):
		self.node_source = node_source
		self.node_destination = node_destination
		self.weight = weight
	
	def set_weight(self, new_weight):
		self.weight = new_weight
	
	def get_weight(self):
		return self.weight
	
	def get_node_source(self):
		return self.node_source

	def get_node_destination(self):
		return self.node_destination

class Graph:

	def __init__(self, generator = False, max_recursion_depth = 1000):
		self.list_edges = []
		self.list_nodes = []
		self.generator = generator
		sys.setrecursionlimit(max_recursion_depth)
	
	def add_node(self, node):
		if(self.exists_node(node.get_key()) == False):
			self.list_nodes.append(node)
			return True
		print("Alert: node with key {0} exists in the graph".format(node.get_key()))
		return False
	
	def add_edge(self, edge):
		if self.generator == True:
			edge.get_node_source().add_neighbor(edge.get_node_destination())
			self.list_edges.append(edge)
			return True
		else:
			if(self.exists_edge(edge) == False):
				if self.exists_node(edge.get_node_source().get_key()) == False:
					self.add_node(edge.get_node_source()) # add node
				elif self.exists_node(edge.get_node_destination().get_key()) == False:
					self.add_node(edge.get_node_destination()) # add node
				pos_node = self.get_node_pos(edge.get_node_source().get_key())
				self.list_nodes[pos_node].add_neighbor(edge.get_node_destination())
				self.list_edges.append(edge)
				return True
			print("Alert: edge exists in the graph (linker node {0} with node {1})".format(edge.get_node_source().get_key(), edge.get_node_destination().get_key()))
			return False
	
	def exists_node(self, key):
		for i in range(0, len(self.list_nodes)):
			if self.list_nodes[i].get_key() == key:
				return True
		return False
	
	def get_node_pos(self, key):
		for i in range(0, len(self.list_nodes)):
			if self.list_nodes[i].get_key() == key:
				return i
		return -1
	
	def exists_edge(self, edge):
		for i in range(0, len(self.list_edges)):
			if self.list_edges[i].get_node_source().get_key() == edge.get_node_source().get_key() and self.list_edges[i].get_node_destination().get_key() == edge.get_node_destination().get_key():
					return True
		return False
	
	def remove_edge(self, edge):
		if(self.exists_edge(edge) == True):
			for i in range(0, len(self.list_edges)):
				if self.list_edges[i].get_node_source().get_key() == edge.get_node_source().get_key():
					if self.list_edges[i].get_node_destination().get_key() == edge.get_node_destination().get_key():
						self.list_edges.pop(i)
						# remove node successor
						pos_neighbor = self.get_node_pos(edge.get_node_source().get_key())
						self.list_nodes[pos_neighbor].remove_neighbor(edge.get_node_destination())
						return True
		print("Alert: edge not found in the graph (linker node {0} with node {1})".format(edge.get_node_source().get_key(), edge.get_node_destination().get_key()))
		return False
	
	def get_edges(self):
		return self.list_edges
	
	def show_connections(self):
		print("Showing connections...")
		for edge in self.list_edges:
			print("Node {0} linked with Node {1}. Weight: {2}".format(edge.get_node_source().get_key(), edge.get_node_destination().get_key(), edge.get_weight()))
	
	def get_neighbors_successors(self, key):
		if self.exists_node(key) == True:
			return self.list_nodes[self.get_node_pos(key)].get_neighbors()
		print("Alert: node with key {0} no exists in the graph".format(key))
		return None

	def get_neighbors_predecessors(self, key):
		if self.exists_node(key) == True:
			list_predecessors = []
			for node in self.list_nodes:
				key_node = node.get_key()
				if key_node != key:
					list_neighbors = node.get_neighbors()
					for node_neighbor in list_neighbors:
						if node_neighbor.get_key() == key:
							list_predecessors.append(node)
			return list_predecessors
		print("Alert: node with key {0} no exists in the graph".format(key))
		return None
	
	# show neighbors successors
	def show_neighbors_successors(self, key):
		print("Showing neighbors successors of node with key {0}...".format(key))
		self.list_neighbors_successors = self.get_neighbors_successors(key)
		if self.list_neighbors_successors != None:
			if len(self.list_neighbors_successors) != 0:
				for node in self.list_neighbors_successors:
					print("Node with key {0}".format(node.get_key()))
			else:
				print("Node with key {0} has no neighbors successors".format(key))

	# show neighbors predecessors
	def show_neighbors_predecessors(self, key):
		print("Showing neighbors predecessors of node with key {0}...".format(key))
		self.list_neighbors_predecessors = self.get_neighbors_predecessors(key)
		if self.list_neighbors_predecessors != None:
			if len(self.list_neighbors_predecessors) != 0:
				for node in self.list_neighbors_predecessors:
					print("Node with key {0}".format(node.get_key()))
			else:
				print("Node with key {0} has no neighbors predecessors".format(key))

	# check if graph is directed (graph symmetrical)
	# graph is symmetrical if for each edge (u,v), exists edge(v,u)
	def is_directed(self):
		flag_directed = False
		for node in self.list_nodes:
			list_neighbors = node.get_neighbors()
			for i in range(0, len(list_neighbors)):
				# get neighbor's key
				key_neighbor = list_neighbors[i].get_key()
				# get successors of eighbor
				list_neighbors_successors = self.get_neighbors_successors(key_neighbor)
				# check if node is successor of neighbor
				is_successor = False
				for j in range(0, len(list_neighbors_successors)):
					if list_neighbors_successors[j].get_key() == node.get_key():
						is_successor = True
						break
				if is_successor == False:
					flag_directed = True
					break
			if flag_directed == True:
				break
		return flag_directed		


	# check if graph is connected, uses DFS (deph first search)
	def is_connected(self):
		# Undirected Graph: just do a DFS starting from any vertex

		# Directed Graph: do DFS X times starting from every vertex, if
		# any DFS doesn't visit all vertices, then graph is not strongly connected

		number_nodes = len(self.list_nodes)
		for k in range(0, number_nodes):
			# set all to not visited
			for i in range(0, len(self.list_nodes)):
				self.list_nodes[i].set_visited(False)
			def dfs(pos):
				self.list_nodes[pos].set_visited(True)
				list_neighbors = self.list_nodes[pos].get_neighbors()
				for neighbor in list_neighbors:
					pos_neighbor = self.get_node_pos(neighbor.get_key())
					if self.list_nodes[pos_neighbor].is_visited() == False:
						dfs(pos_neighbor)
			dfs(k)
			flag_connected = True
			for i in range(0, len(self.list_nodes)):
				if self.list_nodes[i].is_visited() == False:
					flag_connected = False
					break
			# set all to not visited
			for i in range(0, len(self.list_nodes)):
				self.list_nodes[i].set_visited(False)
			if flag_connected == True:
				return True
		return False

	# check if graph is complete
	# graph complete is a graph where all pairs of vertices are adjacent
	def is_complete(self):
		number_nodes = len(self.list_nodes)
		for node in self.list_nodes:
			if len(self.get_neighbors_successors(node.get_key())) < (number_nodes - 1):
				return False
		return True

	# check if graph contains cycle
	# return True if the graph contains at least one cycle, else return false.
	# Solution: DFS (Depth First Traversal) can be used to detect cycle in a graph.
	def is_cyclic(self):
		visited = []
		rec_stack = [] # array to keep track of vertices in the recursion stack

		# this function is a variation of dfs
		def is_cycle(v):
			if(visited[v] == False):
				# mark the current node as visited and part of recursion stack
				visited[v] = True
				rec_stack[v] = True
				# recur for all the vertices adjacent to this vertex
				list_adj = self.list_nodes[v].get_neighbors()
				for node in list_adj:
					pos_node = self.get_node_pos(node.get_key())
					if(visited[pos_node] == False and is_cycle(pos_node) == True):
						return True
					elif(rec_stack[pos_node] == True):
						return True
			rec_stack[v] = False # remove vertex from recursion stack
			return False

		# set all vertices as not visited
		for i in range(0, len(self.list_nodes)):
			visited.append(False)
			rec_stack.append(False)
		# call the recursive function to detect cycle in different DFS trees
		for i in range(0, len(self.list_nodes)):
			if(is_cycle(i) == True):
				return True
		return False

class GeneratorCompleteGraph():
	
	def __init__(self, vertex_number, max_recursion_depth = 1000):
		self.vertex_number = vertex_number
		list_nodes = []
		self.max_recursion_depth = max_recursion_depth
		self.graph = Graph(generator = True, max_recursion_depth = self.max_recursion_depth)
		# creates nodes
		for i in range(0, vertex_number):
			node = Node(i)
			list_nodes.append(node)
			self.graph.add_node(node)
		# add all edges to make complete graph
		for i in range(0, len(list_nodes)):
			for j in range(0, len(list_nodes)):
				if list_nodes[i].get_key() != list_nodes[j].get_key():
					edge = Edge(list_nodes[i], list_nodes[j]) # creates edge
					self.graph.add_edge(edge) # add edge in the graph

	def get_number_edges(self):
		return self.vertex_number * (self.vertex_number - 1)

	def get_graph(self):
		return self.graph