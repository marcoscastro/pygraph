from pygraph import *

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

edge12 = Edge(node1, node2)
edge15 = Edge(node1, node5)
edge31 = Edge(node3, node1)

my_graph = Graph()

my_graph.add_node(node1)
my_graph.add_node(node2)
my_graph.add_node(node3)
my_graph.add_node(node4)
my_graph.add_node(node5)

my_graph.add_edge(edge12)
my_graph.add_edge(edge15)
my_graph.add_edge(edge31)

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
		print("Não passou no teste: run_test_completed")
	else:
		print("Passou no teste: run_test_completed")

def run_test_cyclic(expected, returned):
	if expected != returned:
		print("Não passou no teste: run_test_cyclic")
	else:
		print("Passou no teste: run_test_cyclic")

run_test_directed(True, my_graph.is_directed())
run_test_connected(False, my_graph.is_connected())
run_test_completed(False, my_graph.is_complete())
run_test_cyclic(False, my_graph.is_cyclic())