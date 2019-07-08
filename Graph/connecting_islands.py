import heapq


def create_graph(num_islands, bridge_config):

    adjacency_list = [list() for _ in range(num_islands+1)]

    for source, destination, cost in bridge_config:
        adjacency_list[source].append((destination, cost))
        adjacency_list[destination].append((source, cost))

    return adjacency_list


def minimum_cost(graph):
    start_vertex = 1

    visited = [False for _ in range(len(graph)+1)]

    heap = [(0, start_vertex)]
    total_cost = 0

    while len(heap) > 0:
        cost, current_vertex = heapq.heappop(heap)

        if visited[current_vertex]:
            continue

        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(heap, (edge_cost, neighbor))

        visited[current_vertex] = True
    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
heapq.heapify(bridge_config)
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
