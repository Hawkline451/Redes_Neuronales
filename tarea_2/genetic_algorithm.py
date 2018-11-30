from graph import *


# El algoritmo se inica con un grafo, la tasa de mutacion, y el tamaño del torneo
class GeneticAlgorithm:
    def __init__(self, graph, mutation_rate, tournament_size):
        self.graph = graph
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size

    def reproduction(self, population):
        new_population = Population(self.graph, len(population.individuals))

        # Crossover
        for i in range(len(new_population.individuals)):
            parent_1 = self.tournament_selection(population)
            parent_2 = self.tournament_selection(population)
            child = self.crossover(parent_1, parent_2)
            new_population.individuals[i] = child

        # Mutate
        for i in range(len(new_population.individuals)):
            self.mutate(new_population.individuals[i])

        return new_population

    def crossover(self, parent_1, parent_2):
        child = Path(self.graph)
        mixing_point = random.randint(0, len(parent_1.path) - 1)

        for i in range(mixing_point):
            child.path[i] = parent_1.path[i]
        for i in range(mixing_point, len(parent_2.path)):
            child.path[i] = parent_1.path[i]

        return child

    def mutate(self, individual):
        for path_idx_1 in range(len(individual.path)):
            # si hay mutacion hacemos un swap de los nodos (cambiamos la posicion de los pueblos)
            if random.random() < self.mutation_rate:
                path_idx_2 = random.randint(0, len(individual.path) - 1)

                node_1 = individual.path[path_idx_1]
                node_2 = individual.path[path_idx_2]

                individual.path[path_idx_2] = node_1
                individual.path[path_idx_1] = node_2
        # Como se hace el swap reseteamos la distancia del circuito, luego hay que volver a calcularla
        individual.reset_distance()

    def tournament_selection(self, population):
        tournament = Population(self.graph, self.tournament_size)
        best = None
        for i in range(self.tournament_size):
            random_idx = random.randint(0, len(population.individuals) - 1)
            tmp_individual = population.individuals[random_idx]
            tournament.individuals[i] = tmp_individual

            if (best is None) or (best.evaluate_fitness() <= tmp_individual.evaluate_fitness()):
                best = tmp_individual

        return best




