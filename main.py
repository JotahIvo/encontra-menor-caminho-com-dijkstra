import os, sys
from graph import create_graph, create_cost_graph, create_parents_graph
from dijkstra import dijkstra, return_route


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

        graph = create_graph(cities)
        #print(graph)
        cost_graph = create_cost_graph(graph, cities)
        #print(cost_graph)
        parents_graph = create_parents_graph(graph, cities)
        #print(parents_graph)
        input()



if __name__ == "__main__":
    main()