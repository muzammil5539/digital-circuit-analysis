def find_critical_path(circuit_graph):
    """
    Finds the critical path in the given circuit graph.

    Args:
        circuit_graph (dict): The circuit graph.

    Returns:
        tuple: A tuple containing the critical path (list of node IDs) and the total delay (float).
    """
    def dfs(node, visited, stack):
        visited.add(node)
        for input_node in circuit_graph[node]['inputs']:
            if input_node not in visited:
                dfs(input_node, visited, stack)
        stack.append(node)

    def longest_path():
        visited = set()
        stack = []
        for node in circuit_graph:
            if node not in visited:
                dfs(node, visited, stack)
        dist = {node: float('-inf') for node in circuit_graph}
        dist[stack[-1]] = 0
        while stack:
            node = stack.pop()
            if dist[node] != float('-inf'):
                for input_node in circuit_graph[node]['inputs']:
                    if dist[input_node] < dist[node] + circuit_graph[input_node]['delay']:
                        dist[input_node] = dist[node] + circuit_graph[input_node]['delay']
        max_dist = max(dist.values())
        critical_path = []
        for node, d in dist.items():
            if d == max_dist:
                critical_path.append(node)
                break
        while critical_path[-1] in circuit_graph:
            next_node = None
            for input_node in circuit_graph[critical_path[-1]]['inputs']:
                if dist[input_node] == dist[critical_path[-1]] - circuit_graph[input_node]['delay']:
                    next_node = input_node
                    break
            if next_node is None:
                break
            critical_path.append(next_node)
        critical_path.reverse()
        return critical_path, max_dist

    return longest_path()
