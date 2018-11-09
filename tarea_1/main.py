# Se puede descomentar la siguiente linea y comentar manual_split para usar train_test_split() de
# sklearn.model_selection si se tiene instalada dicha libreria
# from split import *
from manual_split import *
from network import NeuralNetwork, Layer

import matplotlib.pyplot as plt
import sys

import time

def main():
    # Dependiendo de los pesos iniciales se necesitan entre 1000 y 1500 epocas. Sobre 2000 epocas entrega una precision sobre
    # el 95% en los casos de prueba, aunque dependiendo de los pesos iniciales podemos alcanzar un overfitting a las 1000 epocas :(
    try:
        EPOCHS = int(sys.argv[1])
        learning_rate = float(sys.argv[2])
    except:
        EPOCHS = 1000
        learning_rate = .2

    '''
    Creamos las capas
    '''
    # Se crean las capas necesarias para la red
    # Input layer (inputs, neurons)
    input_layer = Layer(5, 8)
    # Cada neurona es un input de la siguiente layer
    # Hidden layer (inputs, neurons)
    hidden_layer = Layer(8, 3)
    # Esta capa esta solo para experimentar, pro lo general usar 2 hidden layers entrega malos resultados
    hidden_layer2 = Layer(3, 1)

    '''
    Inicializamos la red
    '''
    # Neural network (podemos agregar la capa hidden_layer2 para experimentar
    neural_network = NeuralNetwork([input_layer, hidden_layer], learning_rate)

    '''
    Creamos los datos de un archivo csv y entranamos
    '''
    d = Data('sin_normalizar.csv')
    # Primero se normaliza luego extremos los conjuntos de entranamiento y prueba
    d.normalize()
    d.run_split()
    training_features = d.train_features
    training_classes = np.array([d.train_classes]).T

    start_time = time.time()
    neural_network.train(training_features, training_classes, EPOCHS)
    print("Tiempo entrenamiento red: %s seconds" % (time.time() - start_time))

    '''
    Test test_data
    '''

    def test_data(features, classes):
        precision_count = 0
        for i in range(len(features)):
            output = neural_network.check(features[i])
            # print(output," ", classes[i])
            output = np.mean(output)
            output = neural_network.filter_out(output)
            precision_count = (precision_count + 1) if output == classes[i] else precision_count
        return (precision_count / len(classes))

    print("Precision test data")
    print(test_data(d.test_features, d.test_classes))

    print("Precision training data")
    print(test_data(d.train_features, d.train_classes))

    '''
    Plot
    '''

    # ploting errors
    plt.figure(0)
    plt.title("Error")
    plt.xlabel("Epochs")
    plt.plot(neural_network.errors)

    # ploting precision
    plt.figure(1)
    plt.title("Precision")
    plt.xlabel("Epochs")
    plt.plot(neural_network.precision)


if __name__ == '__main__':
    main()
    plt.show()
