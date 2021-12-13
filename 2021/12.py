from copy import deepcopy

with open("input/12", "r") as f:
    indata = [row.split('-') for row in f.read().split('\n')][:-1]

def make_graph():
    graph = dict()
    for p1, p2 in indata:
        if p1 not in graph.keys():
            graph[p1] = []
        if p2 not in graph.keys():
            graph[p2] = []
        graph[p1].append(p2)
        graph[p2].append(p1)
    return graph


def small_cave_twice(path):
    small_caves = [cave for cave in path if cave.islower()]
    return len(small_caves) != len(set(small_caves))


condition1 = lambda node, new_path : node not in new_path or node.isupper()
condition2 = lambda node, new_path : node != 'start' and (node.isupper() or \
        node not in new_path or not small_cave_twice(new_path))

def traverse(graph, current_node, condition, path=[]):
    new_path = path + [current_node]
    if current_node == 'end':
        return 1
    to_be_explored = []
    for node in graph[current_node]:
        if condition(node, new_path):
            to_be_explored.append(node)
    if to_be_explored:
        paths = 0
        for node in to_be_explored:
            paths += traverse(graph, node, condition, new_path)
        return paths
    else:
        return 0


if __name__ == "__main__":
    print("part1:", traverse(make_graph(), 'start', condition1))
    print("part2:", traverse(make_graph(), 'start', condition2))
