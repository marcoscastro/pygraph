from pygraph import GeneratorCompleteGraph
import sys

# redirect output of print to a TXT file
sys.stdout = open("log_graph_complete.txt", "w")
generator = GeneratorCompleteGraph(100, max_recursion_depth = 100000)
generator.get_graph().show_connections()
print("Completo? {0}".format(generator.get_graph().is_complete()))
print("Direcionado? {0}".format(generator.get_graph().is_directed()))
print("Conectado? {0}".format(generator.get_graph().is_connected()))
print("Tem ciclo? {0}".format(generator.get_graph().is_cyclic()))
print("Quantidade de arestas: {0}".format(generator.get_number_edges()))