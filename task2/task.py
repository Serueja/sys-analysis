from collections import defaultdict


def process_graph(data: str) -> dict:
    nodes, edges = defaultdict(set), set()
    for line in data.splitlines():
        node1, node2 = map(int, line.split(','))
        edges.add((node1, node2))
        nodes[node1].add(node2)
        nodes[node2].add(node1)

    results = {
        "nodes_out": set(),  # r1
        "nodes_in": set(),  # r2
        "outgoing_edges": set(),  # r3
        "incoming_edges": set(),  # r4
        "multi_in": set(),  # r5
    }

    for edge in edges:
        node1, node2 = edge
        results["nodes_out"].add(node1)
        results["nodes_in"].add(node2)
        if node2 in nodes[node1]:
            results["outgoing_edges"].add(node1)
        if node1 in nodes[node2]:
            results["incoming_edges"].add(node2)
        if len(nodes[node1]) > 1:
            results["multi_in"].add(node2)

    return results