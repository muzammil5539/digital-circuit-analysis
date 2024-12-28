import os
import networkx as nx
import matplotlib.pyplot as plt

class CircuitAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.circuit_graph = self.parse_circuit()

    def parse_circuit(self):
        """
        Parses the circuit description from a text file and constructs the graph.

        Returns:
            dict: The circuit graph.
        """
        circuit_graph = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.startswith('#') or not line.strip():
                        continue
                    parts = line.strip().split()
                    node_type = parts[0]
                    node_id = parts[1]
                    inputs = parts[2:]
                    circuit_graph[node_id] = {
                        'type': node_type,
                        'inputs': inputs,
                        'delay': self.get_delay(node_type)
                    }
        except FileNotFoundError:
            raise Exception(f"File {self.filename} not found.")
        except Exception as e:
            raise Exception(f"Error parsing {self.filename}: {e}")
        return circuit_graph

    @staticmethod
    def get_delay(node_type):
        """
        Returns the delay for a given component type.

        Args:
            node_type (str): The type of the component.

        Returns:
            float: The delay of the component.
        """
        delays = {
            'ADD': 1.0,
            'MUL': 1.0,
            'REG': 0.2,
            'MUX': 1.0
        }
        return delays.get(node_type, 1.0)

    def find_critical_path(self):
        """
        Finds the critical path in the circuit graph.

        Returns:
            tuple: A tuple containing the critical path (list of node IDs) and the total delay (float).
        """
        def dfs(node, visited, stack):
            visited.add(node)
            for input_node in self.circuit_graph[node]['inputs']:
                if input_node not in visited:
                    dfs(input_node, visited, stack)
            stack.append(node)

        def longest_path():
            visited = set()
            stack = []
            for node in self.circuit_graph:
                if node not in visited:
                    dfs(node, visited, stack)
            dist = {node: float('-inf') for node in self.circuit_graph}
            dist[stack[-1]] = 0
            while stack:
                node = stack.pop()
                if dist[node] != float('-inf'):
                    for input_node in self.circuit_graph[node]['inputs']:
                        if dist[input_node] < dist[node] + self.circuit_graph[input_node]['delay']:
                            dist[input_node] = dist[node] + self.circuit_graph[input_node]['delay']
            max_dist = max(dist.values())
            critical_path = []
            for node, d in dist.items():
                if d == max_dist:
                    critical_path.append(node)
                    break
            while critical_path[-1] in self.circuit_graph:
                next_node = None
                for input_node in self.circuit_graph[critical_path[-1]]['inputs']:
                    if dist[input_node] == dist[critical_path[-1]] - self.circuit_graph[input_node]['delay']:
                        next_node = input_node
                        break
                if next_node is None:
                    break
                critical_path.append(next_node)
            critical_path.reverse()
            return critical_path, max_dist

        return longest_path()

    def visualize_circuit(self, critical_path):
        """
        Visualizes the circuit graph and highlights the critical path.

        Args:
            critical_path (list): The critical path (list of node IDs).
        """
        G = nx.DiGraph()
        for node, data in self.circuit_graph.items():
            for input_node in data['inputs']:
                G.add_edge(input_node, node, weight=data['delay'])

        pos = {}
        layer = 0
        for node in self.circuit_graph:
            if self.circuit_graph[node]['type'] == 'INPUT':
                pos[node] = (0, layer)
                layer += 1

        layer = 0
        for node in self.circuit_graph:
            if self.circuit_graph[node]['type'] == 'OUTPUT':
                pos[node] = (1, layer)
                layer += 1

        for node in self.circuit_graph:
            if node not in pos:
                pos[node] = (0.5, layer)
                layer += 1

        edge_labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_edges(G, pos, edgelist=[(critical_path[i], critical_path[i+1]) for i in range(len(critical_path)-1)], edge_color='r', width=2)

        plt.title(f"Circuit Visualization with Critical Path: {self.filename}")

        # Save the plot to the output folder
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        plt.savefig(os.path.join(output_dir, f"{self.filename.split('.')[0]}.png"))
        plt.close()
