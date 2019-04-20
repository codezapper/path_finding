from collections import defaultdict

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        if (parent is None):
            self.distance_from_start = 0
        else:
            self.distance_from_start = parent.distance_from_start + 1
        self.distance_from_target = 0
        self.cost = 0

    def __eq__(self, other):
        return self.position == other.position


def get_squared_distance(first, second):
    squared_x_distance = (first.position[0] - second.position[0]) ** 2
    squared_y_distance = (first.position[1] - second.position[1]) ** 2

    return squared_x_distance + squared_y_distance


def get_path_from_node(node):
    path = []
    while node is not None:
        path.append(node.position)
        node = node.parent
    return path[::-1]


def is_invalid_position(maze, node):
    if (node.position[0] >= len(maze[0])):
        return True

    if (node.position[1] >= len(maze)):
        return True

    if (node.position[0] < 0):
        return True

    if (node.position[1] < 0):
        return True

    if (maze[node.position[1]][node.position[0]] != 0):
        return True

    return False

def astar(maze, start_position, end_position):
    start_node = Node(None, start_position)
    end_node = Node(None, end_position)

    nodes = []
    nodes.append(start_node)
    visited_nodes = defaultdict(bool)

    while len(nodes) > 0:
        current_node = nodes[0]
        current_index = 0
        for index, item in enumerate(nodes):
            if item.cost < current_node.cost:
                current_node = item
                current_index = index

        nodes.pop(current_index)
        visited_nodes[current_node.position] = True

        if current_node == end_node:
            return get_path_from_node(current_node)

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            new_node = Node(current_node, node_position)
            if (is_invalid_position(maze, new_node)):
                continue

            if (visited_nodes[new_node.position]):
                continue

            new_node.distance_from_target = get_squared_distance(new_node, end_node)
            new_node.cost = new_node.distance_from_start + new_node.distance_from_target

            found_in_list = False
            for node in nodes:
                if new_node == node and new_node.distance_from_start > node.distance_from_start:
                    found_in_list = True
                    break

            if (found_in_list):
                continue
            nodes.append(new_node)
    return []


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
