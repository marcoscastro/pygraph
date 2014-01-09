#-*- coding:utf-8 -*-

from pygraph import *

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

edge12 = Edge(node1, node2)
edge13 = Edge(node1, node3)
edge14 = Edge(node1, node4)
edge21 = Edge(node2, node1)
edge23 = Edge(node2, node3)
edge24 = Edge(node2, node4)
edge31 = Edge(node3, node1)
edge32 = Edge(node3, node2)
edge34 = Edge(node3, node4)
edge41 = Edge(node4, node1)
edge42 = Edge(node4, node2)
edge43 = Edge(node4, node3)

graph = Graph()

graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)

graph.add_edge(edge12)
graph.add_edge(edge13)
graph.add_edge(edge14)
graph.add_edge(edge21)
graph.add_edge(edge23)
graph.add_edge(edge24)
graph.add_edge(edge31)
graph.add_edge(edge32)
graph.add_edge(edge34)
graph.add_edge(edge41)
graph.add_edge(edge42)
graph.add_edge(edge43)

def run_test_directed(expected, returned):
	if expected != returned:
		print("Não passou no teste: run_test_directed")
	else:
		print("Passou no teste: run_test_directed")

def run_test_connected(expected, returned):
	if expected != returned:
		print("Não passou no teste: run_test_connected")
	else:
		print("Passou no teste: run_test_connected")

def run_test_completed(expected, returned):
	if expected != returned:
		print("Não passou no teste: em run_test_completed")
	else:
		print("Passou no teste: run_test_completed")

def run_test_cyclic(expected, returned):
	if expected != returned:
		print("Não passou no teste: run_test_cyclic")
	else:
		print("Passou no teste: run_test_cyclic")

run_test_directed(False, graph.is_directed())
run_test_connected(True, graph.is_connected())
run_test_completed(True, graph.is_complete())
run_test_cyclic(True, graph.is_cyclic())