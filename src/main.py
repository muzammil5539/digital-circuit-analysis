import os
from circuit_analyzer import CircuitAnalyzer

def main():
    # Get the path to the examples directory
    examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'examples')
    cir_names = ["cir1.txt", "cir2.txt", "cir3.txt", "cir4.txt", "cir5.txt"]
    for cur_circuit in cir_names:
        circuit_path = os.path.join(examples_dir, cur_circuit)
        try:
            analyzer = CircuitAnalyzer(circuit_path)
            critical_path, total_delay = analyzer.find_critical_path()
            print(f"\nCircuit name: {cur_circuit}")
            print(f"Critical Path: {' -> '.join(critical_path)}")
            print(f"Total Delay: {total_delay:.2f} time units")
            print("\nAll Components:")
            print(f"{'Component':<10} {'ID':<10} {'Delay (tu)':<10}")
            print("-" * 30)
            for node, data in analyzer.circuit_graph.items():
                print(f"{data['type']:<10} {node:<10} {data['delay']:<10}")
            print("\nPath Components:")
            print(f"{'Component':<10} {'ID':<10} {'Delay (tu)':<10}")
            print("-" * 30)
            for node in critical_path:
                component = analyzer.circuit_graph[node]
                print(f"{component['type']:<10} {node:<10} {component['delay']:<10}")
            analyzer.visualize_circuit(critical_path)
        except Exception as e:
            print(f"Error processing {cur_circuit}: {e}")

if __name__ == "__main__":
    main()
