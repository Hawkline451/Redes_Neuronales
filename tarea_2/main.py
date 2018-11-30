import matplotlib.pyplot as plt
import sys

from data import Data
from genetic_algorithm import *


def main():
    try:
        max_population = int(sys.argv[1])
        generations = int(sys.argv[2])
        mutation_rate = int(sys.argv[3])
        tournament_size = int(sys.argv[3])
    except:
        max_population = 30
        generations = 500
        mutation_rate = 0.01
        tournament_size = 5

    nodes = Data("generated_nodes.csv").get_array()
    graph = Graph()

    for node in nodes:
        tmp_node = Node(node)
        graph.add_node(tmp_node)

    # Generamos la poblacion inicial
    population = Population(graph, max_population)
    print("Distancia generacion 0      -> " + str(population.get_best().nodes_distance()))

    # Corremos el algoritmo n veces dependiento de la cantidad de generaciones
    genetic = GeneticAlgorithm(graph, mutation_rate, tournament_size)
    population = genetic.reproduction(population)
    evolution = []
    for i in range(generations):
        population = genetic.reproduction(population)
        evolution.append(population.get_best().nodes_distance())

    # Printeamos resultados
    print("Distancia ultima generacion -> " + str(population.get_best().nodes_distance()))
    print("Circuito:")
    res_path = population.get_best().path
    for node in res_path:
        print("[", node.get_x(), node.get_y(), end=" ]")

    plt.figure(0)
    plt.plot(evolution)
    plt.ylabel('Distancia')
    plt.xlabel('Generacion')
    plt.grid(True)

    points = res_path

    plt.figure(1)
    for i in range(len(points) - 1):
        x = points[i].get_x()
        y = points[i].get_y()
        x_1 = points[i + 1].get_x()
        y_1 = points[i + 1].get_y()

        plt.plot([x, x_1], [y, y_1], 'ro-')

    # plot last union
    x = points[0].get_x()
    y = points[0].get_y()
    x_1 = points[-1].get_x()
    y_1 = points[-1].get_y()
    plt.plot([x, x_1], [y, y_1], 'r-')
    plt.plot([x], [y], 'bo')
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt.grid(True)


if __name__ == '__main__':
    main()
    plt.show()