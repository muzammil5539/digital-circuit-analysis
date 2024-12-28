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
                # Handle expressions like a^3
                processed_inputs = []
                for input in inputs:
                    processed_inputs.extend(process_expression(input))
                circuit_graph[node_id] = {
                    'type': node_type,
                    'inputs': processed_inputs,
                    'delay': get_delay(node_type)
                }
    except FileNotFoundError:
        raise Exception(f"File {filename} not found.")
    except Exception as e:
        raise Exception(f"Error parsing {filename}: {e}")
    return circuit_graph

def process_expression(expression):
    if '^' in expression:
        base, exponent = expression.split('^')
        exponent = int(exponent)
        return [f"{base}^{exponent}"]
    return [expression]

def get_delay(node_type):
    delays = {
        'ADD': 1.0,
        'MUL': 1.0,
        'REG': 0.2,
        'MUX': 1.0
    }
    return delays.get(node_type, 1.0)
