import numpy as np
import random

# Nodos para el grafo, en este caso los nodos son los genes y a su vez representan los puebles en el algoritmo del
# vendedor viajero
class Node:
    def __init__(self, coord):

        self.coord = coord

    def get_x(self):
        return self.coord[0]

    def get_y(self):
        return self.coord[1]

    def distance_to_node(self, node):
        x_distance = self.get_x() - node.get_x()
        y_distance = self.get_y() - node.get_y()
        distance = (x_distance ** 2 + y_distance ** 2) ** .5
        return distance


# Un Grafo que representa las posibles ruta del vendedor con sus respectivos pueblos
class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, city):
        self.nodes.append(city)


# Algun circuito posible dentro del grafo, ademas dentro del algoritmo genetico, estos circuitos representan los
# individuos
class Path:
    def __init__(self, graph):
        self.graph = graph
        self.graph_len = len(graph.nodes)
        self.path = [None]*self.graph_len
        self.fitness = 0.0
        self.distance = 0

    # Generamos un circuito random
    def generate_individual(self):
        for node_idx in range(self.graph_len):
            self.path[node_idx] = self.graph.nodes[node_idx]
        self.reset_fitness()
        random.shuffle(self.path)

    # Cada vez que cambiamos el camino moviendo un nodo resetamos fitness y distance, luego sera necesario volver a calcularlas
    def reset_fitness(self):
        self.fitness = 0.0
        self.distance = 0

    def evaluate_fitness(self):
        # Si la distancia es igual a 0 es porque el path fue inicializado pero todavia no sabemos la distancia,
        # por lo que se debe calcular, analogo para el fitness
        self.distance = self.nodes_distance() if self.distance == 0 else self.distance
        self.fitness = 1 / self.distance if self.fitness == 0 else self.fitness
        return self.fitness

    def nodes_distance(self):
        path_distance = 0
        for node_idx in range(len(self.path)):
            from_node = self.path[node_idx]
            if node_idx + 1 < len(self.path):
                to_node = self.path[node_idx + 1]
            # Como es un circuito volvemos al primero
            else:
                to_node = self.path[0]
            path_distance += from_node.distance_to_node(to_node)
        self.distance = path_distance
        return self.distance


# Conjunto de individuos, en este caso los individuos son los circuitos dentro del grafo
class Population:
    def __init__(self, graph, population_size):
        self.individuals = []

        for i in range(population_size):
            new_path = Path(graph)
            new_path.generate_individual()
            self.individuals.append(new_path)

    def get_best(self):
        best = self.individuals[0]
        for i in range(len(self.individuals)):
            if best.evaluate_fitness() <= self.individuals[i].evaluate_fitness():
                best = self.individuals[i]
        return best