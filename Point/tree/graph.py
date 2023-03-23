import pydot
from .models import Leaf, Edge


def generate_graph():
    # Create a new graph
    graph = pydot.Dot(graph_type='graph')

    # Add nodes to the graph
    for leaf in Leaf.objects.all():
        node = pydot.Node(str(leaf.id), label=leaf.name, shape='box')
        graph.add_node(node)

    # Add edges to the graph
    for edge in Edge.objects.all():
        edge = pydot.Edge(str(edge.parent_leaf.id), str(edge.child_leaf.id))
        graph.add_edge(edge)
        
        graph.write_png('static\tree\graph.png')