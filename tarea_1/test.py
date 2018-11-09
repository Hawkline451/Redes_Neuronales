import unittest
import numpy

from network import NeuralNetwork, Layer
from manual_split import *


class Test1(unittest.TestCase):

    def test_and(self):
        # Creamos las capas
        input_layer = Layer(2, 1)
        hidden_layer = Layer(1, 1)

        # Inicializamos la red
        neural_network = NeuralNetwork([input_layer, hidden_layer], .1)

        training_features = numpy.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        training_classes = numpy.array([[0, 0, 0, 1]]).T
        neural_network.train(training_features, training_classes, 5000)

        result_1_1 = round(neural_network.check([1,1])[0])
        result_1_0 = round(neural_network.check([1,0])[0])
        result_0_1 = round(neural_network.check([0,1])[0])
        result_0_0 = round(neural_network.check([0,0])[0])

        result = (result_1_1, result_1_0, result_0_1, result_0_0)
        self.assertEqual(result, (1, 0, 0, 0 ))

    def test_xor(self):
        # Creamos las capas
        input_layer = Layer(2, 2)
        hidden_layer = Layer(2, 1)

        # Inicializamos la red
        neural_network = NeuralNetwork([input_layer, hidden_layer], .1)

        training_features = numpy.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        training_classes = numpy.array([[0, 1, 1, 0]]).T
        # Este amigo derepente fallaba con pocas epocas asi que se colocaron muchas para evitar problemas con los test
        neural_network.train(training_features, training_classes, 30000)

        result_1_1 = round(neural_network.check([1, 1])[0])
        result_1_0 = round(neural_network.check([1, 0])[0])
        result_0_1 = round(neural_network.check([0, 1])[0])
        result_0_0 = round(neural_network.check([0, 0])[0])

        result = (result_1_1, result_1_0, result_0_1, result_0_0)
        self.assertEqual(result, (0, 1, 1, 0))

    def test_split(self):
        d = Data('sin_normalizar.csv')
        d.normalize()
        d.run_split()

        # 20% test, 80% train
        self.assertEqual(len(d.test_features), 43)
        self.assertEqual(len(d.train_features), 172)



if __name__ == '__main__':
    unittest.main()