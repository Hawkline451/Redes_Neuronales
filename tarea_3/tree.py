import numpy as np

class Node:

    def __init__(self, token):
        self.token = token
        self.left = None
        self.right = None

    def left(self, value):
        if not isinstance(value, Node):
            raise TypeError("Left node must be of type Node")
        self.left = value

    def right(self, value):
        if not isinstance(value, Node):
            raise TypeError("Right node must be of type Node")
        self.right = value


OPERATOR = ['+', '-', '*', '/']


class ExpressionTree:

    def __init__(self, postfixtokens):
        stack = list()
        self.root = None
        self.env = {}
        self.expected_values = []
        self.fitness = 0.0
        self.eval = 0.0
        self.error = 0.0

        for token in postfixtokens:
            if token not in OPERATOR:
                stack.append(Node(token))
            else:
                operator_node = Node(token)

                if len(stack) < 2:
                    raise TypeError('Incorrectly formatted expression - check operators.')

                operator_node.right = stack.pop()
                operator_node.left = stack.pop()

                stack.append(operator_node)

        if len(stack) > 1:
            raise TypeError('Incorrectly formatted expression - check operands.')
        self.root = stack.pop()

    def reset_fitness(self):
        self.fitness = 0.0
        self.eval = 0.0

    def evaluate_fitness(self, expected_vals, env_list):
        error = 0
        solution_list = self.eval_function( env_list)

        for idx in range(len(expected_vals)):
            error += abs(expected_vals[idx] - solution_list[idx])

        # No quiero dividir por 0
        self.fitness = 1 / (error + .0000000000001)
        self. error = error
        return self.fitness

    def solve(self, node):
        if node.token not in OPERATOR:
            if node.token.isalpha():
                return self.eval_env(node.token)
            else:
                return int(node.token)

        left_value = self.solve(node.left)
        right_value = self.solve(node.right)

        operator = node.token
        if operator == '+':
            return left_value + right_value
        if operator == '-':
            return left_value - right_value
        if operator == '*':
            return left_value * right_value
        if operator == '/':
            return left_value / right_value

    def eval_env(self, var):
        return self.env[var]

    def eval_function(self, env_list):
        res = []
        node = self.root
        for env in env_list:
            self.env = env
            res.append(self.solve(node))
        return res


    def inorder(self, root):
        res = ""
        if root:
            if root.token in OPERATOR:
                res += '('
                res += self.inorder(root.left)
                res += root.token
                res += self.inorder(root.right)
                res += ')'

            else:
                res += self.inorder(root.left)
                res += root.token
                res += self.inorder(root.right)

        return  res











