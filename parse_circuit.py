def parse_circuit(filename):
    circuit_graph = {}
    try:
        with open(filename, 'r') as file:
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
                    'delay': get_delay(node_type)
                }
    except FileNotFoundError:
        raise Exception(f"File {filename} not found.")
    except Exception as e:
        raise Exception(f"Error parsing {filename}: {e}")
    return circuit_graph

def get_delay(node_type):
    delays = {
        'ADD': 1.0,
        'MUL': 1.0,
        'REG': 0.2,
        'MUX': 1.0
    }
    return delays.get(node_type, 1.0)
