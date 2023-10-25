import os, sys
from graph import create_graph, create_cost_graph, create_parents_graph, travel_cost
from dijkstra import dijkstra, return_route
import time


def print_route(route):
    route_str = ""
    for i in range(len(route)-1):
        route_str += route[i] + " -> "
    route_str += route[-1]

    return route_str 


def main():
    while True:
        os.system("clear")
        print('''Seja bem vindo ao Encurtador de Caminho, que utiliza do algoritmo de Dijkstra para encontrar o menor caminho que você deve percorer para sair de uma cidade A para uma cidade B!
Para isso, responda as perguntar sobre o caminho para que o algoritmo possa te mostrar o menor caminho para sua viagem!

Vamos lá???
        ''')
        input("Pressione 'Enter' para continuar...")

        os.system("clear")

        n = int(input("Quanta cidades tem entre a cidade A e a cidade B incluindo A e B??? "))

        input("\nÓtimo... vamos continuar!")
        os.system("clear")

        print("Vamos começar a cadastrar as cidades e as distâncias entre elas: ")
        cities = []
        for i in range(1, n+1):
            os.system("clear")
            city = str(input(f"\nQual o nome da cidade {i}: "))
            cities.append(city)

        #criando os grafos
        graph = create_graph(cities)
        cost_graph = create_cost_graph(graph, cities)
        parents_graph = create_parents_graph(graph, cities)

        os.system("clear")
        print("O algoritmo está procurando o caminho mais rápido...")
        time.sleep(3)
        
        lowest_cost_parents = dijkstra(graph, cost_graph, parents_graph)
        route = return_route(cities[0], cities[-1], lowest_cost_parents)
        route_cost = travel_cost(graph, route)

        print(f"\nA menor rota partindo de {cities[0]} até {cities[-1]} é: ")
        print(print_route(route))
        print(f"E a distância em Km dessa viagem é de: {route_cost} Km")

        input()


if __name__ == "__main__":
    main()