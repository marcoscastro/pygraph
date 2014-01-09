#-*- coding:utf-8 -*-

from pygraph import *

graph = Graph()

graph.add_edge(Edge(Node(0), Node(1)))
graph.add_edge(Edge(Node(0), Node(2)))
graph.add_edge(Edge(Node(1), Node(2)))
graph.add_edge(Edge(Node(2), Node(0)))
graph.add_edge(Edge(Node(2), Node(3)))
graph.add_edge(Edge(Node(3), Node(3)))

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

run_test_directed(True, graph.is_directed())
run_test_connected(True, graph.is_connected())
run_test_completed(False, graph.is_complete())
run_test_cyclic(True, graph.is_cyclic())