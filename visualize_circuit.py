import networkx as nx
import matplotlib.pyplot as plt
import os

def visualize_circuit(circuit_graph, critical_path, circuit_name):
    """
    Visualizes the given circuit graph and highlights the critical path.

    Args:
        circuit_graph (dict): The circuit graph.
        critical_path (list): The critical path (list of node IDs).
        circuit_name (str): The name of the circuit.
    """
    G = nx.DiGraph()
    for node, data in circuit_graph.items():
        for input_node in data['inputs']:
            G.add_edge(input_node, node, weight=data['delay'])

    pos = {}
    layer = 0
    for node in circuit_graph:
        if circuit_graph[node]['type'] == 'INPUT':
            pos[node] = (0, layer)
            layer += 1

    layer = 0
    for node in circuit_graph:
        if circuit_graph[node]['type'] == 'OUTPUT':
            pos[node] = (1, layer)
            layer += 1

    for node in circuit_graph:
        if node not in pos:
            pos[node] = (0.5, layer)
            layer += 1

    edge_labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edgelist=[(critical_path[i], critical_path[i+1]) for i in range(len(critical_path)-1)], edge_color='r', width=2)

    plt.title(f"Circuit Visualization with Critical Path: {circuit_name}")

    # Save the plot to the output folder
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(os.path.join(output_dir, f"{circuit_name}.png"))
    plt.close()
