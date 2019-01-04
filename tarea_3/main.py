from genetic_tree import *
import matplotlib.pyplot as plt
import sys

import time


start_time = time.time()
if __name__ == "__main__":

    try:
        max_population = int(sys.argv[1])
        generations = int(sys.argv[2])
        mutation_rate = int(sys.argv[3])
        tournament_size = int(sys.argv[3])
    except:
        max_population = 500
        generations = 10
        mutation_rate = 0.01
        tournament_size = 200


    ops = ['+', '-', '*']
    terminals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'x']

    # Generamos la expresion que se quiere aproximar en notacion postfija
    # (((x*x)-5)+(10*x))
    eq = ['x', 'x', '*', '5', '-', '10', 'x', '*', '+']


    eq_tree = ExpressionTree(eq)
    domain = [{'x' : 1},{'x' : 2},{'x' : 3},{'x' : 4}, {'x' : 5}, {'x' : 6},{'x' : 7},{'x' : 8},{'x' : 9}, {'x' : 10}]
    results = eq_tree.eval_function(domain)

    # Generamos la poblacion inicial
    population = Population(ops, terminals, max_population)

    # Corremos el algoritmo n veces dependiento de la cantidad de generaciones
    genetic = GeneticTree(terminals, ops, mutation_rate, tournament_size)
    genetic.expected_vals = results
    genetic.env_list = domain

    evolution = []
    for i in range(generations):
        print("Generacion: ", i)
        population = genetic.reproduction(population)
        avg = 0

        best = population.individuals[0]
        for individual in population.individuals:
            individual.evaluate_fitness(genetic.expected_vals, genetic.env_list)
            avg += individual.error
            best = individual if individual.error <= best.error else best

        avg = avg / len(population.individuals)
        evolution.append(avg)
        print("Error por generacion: ", avg)



    best = population.get_best(results, domain)


    print("\nExpresion a inferir: ", eq_tree.inorder(eq_tree.root))
    print("Resultados esperados: ",results)

    print("\nExpresion encontrada: ", best.inorder(best.root))
    print("Expresion evaluada en el dominio:", best.eval_function(domain))
    print("Error expresion evaluada en el dominio:", best.error)

    plt.figure(0)
    plt.plot(evolution)
    plt.title('Error promedio por generacion')
    plt.ylabel('Error')
    plt.xlabel('Generacion')
    plt.grid(True)

    plt.show()

print("--- %s seconds ---" % (time.time() - start_time))


