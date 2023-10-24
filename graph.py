import os, sys


def create_graph(cities):
    os.system("clear")
    graph = {}

    for city in cities:
        os.system("clear")
        graph[city] = {}
        
        n_childrens = int(input(f"Quantas cidades estão ligadas a {city}? "))

        if n_childrens > 0:
            for i in range(1, n_childrens+1):
                name_children = str(input("Qual o nome da cidade? "))
                distance = int(input(f"Qual a distância entre {city} e {name_children} em Km? "))

                graph[city][name_children] = distance

    return graph


def create_cost_graph(graph, cities):
    cost = {}
    infinity = float("inf")

    for children in graph[cities[0]]:
        if children in graph[cities[0]]:
            cost[children] = graph[cities[0]][children]

    for nodo in graph:
        if nodo == cities[0] or nodo in cost:
            continue
        else:
            cost[nodo] = infinity

    return cost
                

def create_parents_graph(graph, cities):
    parents = {}

    for children in graph[cities[0]]:
        if children in graph[cities[0]]:
            parents[children] = cities[0]

    for nodo in graph:
        if nodo == cities[0] or nodo in parents:
            continue
        else:
            parents[nodo] = None

    return parents