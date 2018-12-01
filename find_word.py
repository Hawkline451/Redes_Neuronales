import random
import numpy as np

# individuos
class Individual:
    def __init__(self, word):
        self.word = word
        self.word_len = len(word)
        self.new_word = [None] * self.word_len
        self.fitness = 0.0

    # Generamos un individuo random
    def generate_individual(self):
        for gene_idx in range(self.word_len):
            self.new_word[gene_idx] = np.random.choice(self.word)
        self.reset_fitness()

    # Cada vez que cambiamos la palabra debemos resetear el fitness
    def reset_fitness(self):
        self.fitness = 0.0

    def evaluate_fitness(self):
        counter = 0
        for i in range(len(self.new_word)):
            counter = counter + 1 if self.new_word[i] == self.word[i] else counter
        self.fitness = counter
        return self.fitness


# Conjunto de individuos, en este caso los individuos son los circuitos dentro del grafo
class Population:
    def __init__(self, word, population_size):
        self.individuals = []

        for i in range(population_size):
            new_word = Individual(word)
            new_word.generate_individual()
            self.individuals.append(new_word)

    def get_best(self):
        best = self.individuals[0]
        for i in range(len(self.individuals)):
            if best.evaluate_fitness() <= self.individuals[i].evaluate_fitness():
                best = self.individuals[i]
        return best


class GeneticAlgorithm:
    def __init__(self, word, mutation_rate, tournament_size):
        self.word = word
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size

    def reproduction(self, population):
        new_population = Population(self.word, len(population.individuals))

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
        child = Individual(self.word)
        mixing_point = random.randint(0, len(parent_1.word) - 1)

        for i in range(mixing_point):
            child.new_word[i] = parent_1.new_word[i]

        for i in range(mixing_point, len(parent_2.new_word)):

            child.new_word[i] = parent_2.new_word[i]

        return child

    def mutate(self, individual):
        for word_idx_1 in range(len(individual.word)):
            # si hay mutacion hacemos un swap de los genes (cambiamos la posicion algun caracter)
            if random.random() < self.mutation_rate:
                word_idx_2 = random.randint(0, len(individual.word) - 1)

                gene_1 = individual.new_word[word_idx_1]
                gene_2 = individual.new_word[word_idx_2]
                individual.new_word[word_idx_2] = gene_1
                individual.new_word[word_idx_1] = gene_2

        # Como se hace el swap reseteamos la distancia del circuito, luego hay que volver a calcularla
        individual.reset_fitness()

    def tournament_selection(self, population):
        tournament = Population(self.word, self.tournament_size)
        best = None
        for i in range(self.tournament_size):
            random_idx = random.randint(0, len(population.individuals) - 1)
            tmp_individual = population.individuals[random_idx]
            tournament.individuals[i] = tmp_individual

            if (best is None) or (best.evaluate_fitness() <= tmp_individual.evaluate_fitness()):
                best = tmp_individual
        return best



def main():

        max_population = 10
        generations = 400
        mutation_rate = 0.01
        tournament_size = 10


        word = ['0','1','1','0','0','1']

        print("Palabra escogida -> " + str(word))
        # Generamos la poblacion inicial
        population = Population(word, max_population)
        print("Generacion 0     -> " + str(population.get_best().new_word))

        # Corremos el algoritmo n veces dependiento de la cantidad de generaciones
        for i in range(generations):
            genetic = GeneticAlgorithm(word, mutation_rate, tournament_size)
            population = genetic.reproduction(population)

        # Printeamos resultados
        print("Generacion final -> " + str(population.get_best().new_word))


if __name__ == '__main__':
        main()





