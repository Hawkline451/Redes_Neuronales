import numpy as np
import random
import copy

from tree import ExpressionTree


OPERATOR = ['+', '-', '*', '/']


class GeneticTree:

    def __init__(self, terminals, ops, mutation_rate, tournament_size):
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.terminals = terminals
        self.ops = ops
        self.expected_vals = []
        self.env_list = []

    def reproduction(self, population):
        new_population = Population(self.ops, self.terminals, len(population.individuals))

        # Crossover
        for i in range(len(new_population.individuals)):
            parent_1 = self.tournament_selection(population, self.expected_vals, self.env_list)
            parent_2 = self.tournament_selection(new_population, self.expected_vals, self.env_list)

            child = self.tree_crossover(parent_1, parent_2)
            new_population.individuals[i] = child

        # Mutate

        for i in range(len(new_population.individuals)):
            self.tree_mutate(new_population.individuals[i])
            new_population.individuals[i].evaluate_fitness(self.expected_vals, self.env_list)

            new_population.individuals[i] = population.individuals[i] if population.individuals[i].error < new_population.individuals[i].error else new_population.individuals[i]

        return new_population

    def inorder_traverse(self, root):
        res = []
        if root:
            res = self.inorder_traverse(root.left)
            res.append(root)
            res += self.inorder_traverse(root.right)
        return res

    def traverse(self, root, target_node=None, operator=True):
        node = None
        if target_node is None:
            res = self.inorder_traverse(root)
            node = np.random.choice(res, replace=False)

            if operator:
                # Mientras el nodo no sea un operador (+,-,*,/) buscamos un nodo nuevo
                while node.token not in OPERATOR:
                    node = np.random.choice(res, replace=False)
            else:
                while node.token in OPERATOR:
                    node = np.random.choice(res, replace=False)
        else:
            res = self.inorder_traverse(root)
            for tmp_node in res:
                if tmp_node.token == target_node.token:
                    node = tmp_node
                    break
        return node

    def tree_crossover(self, parent_1, parent_2):

        parent_1.evaluate_fitness(self.expected_vals, self.env_list)
        parent_2.evaluate_fitness(self.expected_vals, self.env_list)

        child_1_tmp = copy.deepcopy(parent_1)
        child_2_tmp = copy.deepcopy(parent_2)

        try:
            gene_1 = self.traverse(child_1_tmp.root, target_node=None)
            gene_2 = self.traverse(child_2_tmp.root, target_node=gene_1)

            tmp_left = gene_1.left
            tmp_right = gene_1.right

            gene_1.left = gene_2.left
            gene_1.right = gene_2.right

            gene_2.left = tmp_left
            gene_2.right = tmp_right

            child_1_tmp.evaluate_fitness(self.expected_vals, self.env_list)
            child_2_tmp.evaluate_fitness(self.expected_vals, self.env_list)

            tree_list = [parent_1,parent_2,child_1_tmp,child_2_tmp]
            best = parent_1
            for tree in tree_list:
                best = tree if tree.error <= best.error else best

            return best

        except:
            return (parent_2 if parent_2.error < parent_1.error else parent_1)

    def tree_mutate(self, tree):

        gene_1 = self.traverse(tree.root, target_node=None, operator=False)
        gene_2 = self.traverse(tree.root, target_node=None, operator=False)

        token_tmp = gene_1.token
        gene_1.token = gene_2.token
        gene_2.token = token_tmp

    def tournament_selection(self, population, expected_vals, env_list):
        best = None
        for i in range(self.tournament_size):
            random_idx = random.randint(0, len(population.individuals) - 1)
            tmp_individual = population.individuals[random_idx]

            if (best is None) or (best.evaluate_fitness(expected_vals, env_list) <= tmp_individual.evaluate_fitness(expected_vals, env_list)):
                best = tmp_individual

        return best


class Population:
    def __init__(self, ops, terminals, population_size):
        self.individuals = []
        self.ops = []
        self.terminals = []
        # Dependiendo de la expresón que se queira encontrar este rango podria cambiarse
        self.range_number_terminals = range(3,7)

        for i in range(population_size):
            exp_tree = self.generate_individual(ops, terminals, self.range_number_terminals)
            self.individuals.append(exp_tree)

    # A post fix expression always begins with 2 operands (varibles or numbers) and ends with an operator
    def generate_random_postfix(self, operators, terminals, range_number_terminals):

        postfix = []
        number_terminals = np.random.choice(range_number_terminals)
        for i in range(number_terminals):

            if len(postfix) == 0:
                end_operator = np.random.choice(operators, size=1)
                operands = np.random.choice(terminals, size=2)

            else:
                end_operator = np.random.choice(operators, size=1)
                operands = np.random.choice(terminals, size=1)


            selector = np.random.choice([True, False])
            if selector:
                tmp_list = operands.tolist()
                tmp_list.extend(postfix)
                postfix = tmp_list
            else:
                postfix.extend(operands)
            postfix.extend(end_operator)

        return postfix

    def generate_individual(self, ops, terminals, range_number_terminals):
        postfix_expression = self.generate_random_postfix(ops, terminals, range_number_terminals)
        exp_tree = ExpressionTree(postfix_expression)
        exp_tree.reset_fitness()
        return exp_tree

    def get_best(self, expected_vals, env_list):
        best = self.individuals[0]
        for i in range(len(self.individuals)):
            if best.evaluate_fitness(expected_vals, env_list) <= self.individuals[i].evaluate_fitness(expected_vals, env_list):
                best = self.individuals[i]
        return best


