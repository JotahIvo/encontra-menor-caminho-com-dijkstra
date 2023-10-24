def find_lowest_cost(costs, processed):
    lowest_cost = float("inf")
    nodo_lowest_cost = None
    for nodo in costs:
        cost = costs[nodo]
        if cost < lowest_cost and nodo not in processed:
            lowest_cost = cost
            nodo_lowest_cost = nodo
    return nodo_lowest_cost


def dijkstra(graph, costs, parents):
    #array que guarda os vértices já processed
    processed = []
    nodo = find_lowest_cost(costs, processed)
    while nodo is not None:
        cost = costs[nodo]
        neighbors = graph[nodo]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = nodo
        processed.append(nodo)
        nodo = find_lowest_cost(costs, processed)
    return parents


def return_route(first, last, parents):
    vertex = parents[last]
    route = [last]

    while vertex != first:
        route.append(vertex)
        vertex = parents[vertex]
    route.append(first)
    route.reverse()
    return route