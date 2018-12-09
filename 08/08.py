with open("input.txt") as f:
    numbers = list(map(int, f.readline().split()))


def parse_tree_metadata(tree):
    num_nodes = tree[0]
    num_metadata = tree[1]

    leafs = tree[2:]
    total = 0

    for i in range(num_nodes):
        leafs, sum_metadata = parse_tree_metadata(leafs)
        total += sum_metadata

    for i in range(num_metadata):
        total += leafs[i]

    return leafs[num_metadata:], total


print(parse_tree_metadata(numbers)[1])


def get_value_root_node(start):
    node_sum = 0
    num_nodes, num_metadata = numbers[start : start + 2]
    next_start = start + 2

    if num_nodes:
        node_values = []
        for child_node in range(num_nodes):
            temporary_sum, next_start = get_value_root_node(next_start)
            node_values.append(temporary_sum)
        for i in numbers[next_start : next_start + num_metadata]:
            if i - 1 < len(node_values):
                node_sum += node_values[i - 1]
    else:
        node_sum += sum(numbers[next_start : next_start + num_metadata])
    return node_sum, next_start + num_metadata


print(get_value_root_node(0)[0])
