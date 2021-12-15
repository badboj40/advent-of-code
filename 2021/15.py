from copy import deepcopy

with open("input/15", "r") as f:
    indata = f.read().split('\n')[:-1]

class Node:
    def __init__(self, y, x, value):
        self.y = y
        self.x = x
        self.value = value
        self.cost = float("Inf")
        self.discovered = False

    def get_neighbors(self, node_map):
        neighbors = []
        if self.y >= 1:
            neighbors.append(node_map[self.y-1][self.x])
        if self.y < len(node_map)-1:
            neighbors.append(node_map[self.y+1][self.x])
        if self.x >= 1:
            neighbors.append(node_map[self.y][self.x-1])
        if self.x < len(node_map[0])-1:
            neighbors.append(node_map[self.y][self.x+1])
        return neighbors


def generate_map1():
    node_map = [[None] * len(indata[0]) for row in range(len(indata))]
    for y in range(len(indata)):
        for x in range(len(indata[0])):
            node_map[y][x] = Node(y, x, int(indata[y][x]))
    node_map[0][0].discovered = True
    node_map[0][0].cost = 0
    return node_map


def generate_map2():
    width = len(indata[0])
    height = len(indata)
    node_map = [[None] * width*5 for row in range(height*5)]
    for y in range(height*5):
        for x in range(width*5):
            tile_y = int((y - y % height) / height)
            tile_x = int((x - x % width) / width)
            value = int(indata[y % height][x % width]) + tile_y + tile_x
            if value > 9:
                value -= 9
            node_map[y][x] = Node(y, x, value)
    node_map[0][0].discovered = True
    node_map[0][0].cost = 0
    return node_map


def find_path(node_map):
    queue = [node_map[0][0]]
    while queue:
        node = queue.pop(0)
        for neighbor in node.get_neighbors(node_map):
            new_cost = node.cost + neighbor.value
            if not neighbor.discovered or new_cost < neighbor.cost:
                neighbor.discovered = True
                neighbor.cost = new_cost
                queue.append(neighbor)
    goal_node = node_map[-1][-1]
    return goal_node.cost


if __name__ == "__main__":
    print("part1:", find_path(generate_map1()))
    print("part2:", find_path(generate_map2()))
