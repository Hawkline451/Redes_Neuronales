from numpy import exp, random, dot, shape, array, mean


class Neuron():
    def __init__(self, number_inputs, bias=0.0):
        # Random numbers desde -1 to 1 [0-1,2-1]
        self.weight_list = (2 * random.rand(number_inputs) - 1)
        self.bias = float(bias)


# Solo se usa la clase Neuron para generar los pesos y bias, es mas eficiente multiplicar matrices
# que iterar sobre cada neurona
class Layer():
    def __init__(self, number_inputs, number_neurons):
        self.neurons = [Neuron(number_inputs) for i in range(number_neurons)]

        # Cada neurona se representa como una fila en la matriz de NxM, analogo con el bias
        self.weights = array([neuron.weight_list for neuron in self.neurons])
        self.bias = array([neuron.bias for neuron in self.neurons])

        self.delta = []
        self.out = []


# La clase neural network soporta n capas, una de estas es el input con n-1 capas ocultas
class NeuralNetwork():
    def __init__(self, list_layers, learning_rate=.1):
        self.layers = list_layers
        self.lr = learning_rate

        self.precision = []
        self.errors = []

    def sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def sigmoid_transfer_derivative(self, x):
        return x * (1 - x)

    def backpropagation(self, layers, expected_out):

        self.check(self.training_features)
        # Backpropagation
        for i in range(len(layers)):
            idx = len(layers) - i - 1
            # Es la ultima layer
            if idx == (len(layers) - 1):
                # print("asd")
                hidden_out = layers[idx].out
                out_error = expected_out - hidden_out
            else:
                # print("asd2")
                output_layer = layers[idx + 1]
                out_error = delta.dot(output_layer.weights)

            input_out = layers[idx].out
            delta = out_error * self.sigmoid_transfer_derivative(input_out)
            self.layers[idx].delta = delta

        # Los inputs de una capa son los outs de la capa anterior
        for i in range(len(layers)):
            if i == 0:
                input_data = self.training_features
            else:
                input_data = layers[i - 1].out

            input_adjustment = input_data.T.dot(self.layers[i].delta)
            # Ajustamos los pesos
            self.layers[i].weights += self.lr * input_adjustment.T

            # Ajustamos los bias
            for j in range(len(self.training_classes)):
                self.layers[i].bias += self.lr * self.layers[i].delta[j]

        return input_out, hidden_out

    def train(self, training_features, training_classes, epochs):
        self.training_features = training_features
        self.training_classes = training_classes
        expected_out = training_classes

        for iteration in range(epochs):
            input_out, input_data = self.backpropagation(self.layers, expected_out)

            # print((input_delta[0]))
            # print((self.input.bias[0]))

            # Obtenemos precision y error luego de cada epoca
            self.getStats()

    # Feed Forward
    def feed(self, inputs, layer):
        # print(np.shape(dot(inputs, layer.weights.T)))
        output = self.sigmoid(dot(inputs, layer.weights.T) + layer.bias.T)

        layer.out = output

        return output

    def check(self, feature):
        # 1 input_layer n hidden layers
        number_layers = len(self.layers)
        # Entramos a la 1ra capa
        output = self.feed(feature, self.layers[0])

        # Input layer already fed
        # Encontramos los outputs de las n-1 capas siguientes
        for idx in range(number_layers - 1):
            # Back propagation from layer[n] to layer[n-1]
            output = self.feed(output, self.layers[idx + 1])

        return output

    # Obtenemos la precision y el error luego de cada epoca
    def getStats(self):

        training_features = self.training_features
        training_classes = self.training_classes
        precision_count = 0
        error_count = 0
        for i in range(len(training_features)):
            output = self.check(training_features[i])
            # print(output," ", d.classes[i])
            output = mean(output)

            error_count += abs(output - training_classes[i])

            output = self.filter_out(output)
            precision_count = (precision_count + 1) if output == training_classes[i] else precision_count

        self.precision.append(precision_count / len(training_classes))
        self.errors.append(error_count / len(training_classes))

    # En este caso tenemos 3 clases [0, .5, 1] tomamos 3 umbrales arbitrarios para clasificar
    # En realidad no es tan arbitrario, es un rango coherente dentro de lo esperado (mayores a.75 son clase 1 menores a .25 son clase 0)
    def filter_out(self, output):
        return 1 if output > .75 else (0 if output < 0.25 else 0.5)
