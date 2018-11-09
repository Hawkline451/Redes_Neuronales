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

    def backpropagation(self, in_layer, output_layer, input_data):

        input_out = self.feed(input_data, in_layer)
        hidden_out = self.feed(input_out, output_layer)

        # Backpropagation
        hidden_error = self.training_classes - hidden_out
        hidden_delta = hidden_error * self.sigmoid_transfer_derivative(hidden_out)

        hidden_adjustment = input_out.T.dot(hidden_delta)

        input_error = hidden_delta.dot(output_layer.weights)
        input_delta = input_error * self.sigmoid_transfer_derivative(input_out)

        input_adjustment = self.training_features.T.dot(input_delta)

        # Ajustamos los pesos
        in_layer.weights += self.lr * input_adjustment.T
        output_layer.weights += self.lr * hidden_adjustment.T

        # Ajustamos los bias al final de cada epoca
        for i in range(len(self.training_classes)):
            in_layer.bias += self.lr * input_delta[i]
            output_layer.bias += self.lr * hidden_delta[i]

        return hidden_out

    def train(self, training_features, training_classes, epochs):
        self.training_features = training_features
        self.training_classes = training_classes

        for iteration in range(epochs):

            # 1 input_layer n hidden layers
            number_layers = len(self.layers) - 1

            input_data = training_features
            for idx in range(number_layers):
                input_layer = self.layers[idx]
                output_layer = self.layers[idx + 1]
                input_data = self.backpropagation(input_layer, output_layer, input_data)

            # print((input_delta[0]))
            # print((self.input.bias[0]))

            # Obtenemos precision y error luego de cada epoca
            self.getStats()


    # Feed Forward
    def feed(self, inputs, layer):
        # print(np.shape(dot(inputs, layer.weights.T)))
        output = self.sigmoid(dot(inputs, layer.weights.T) + layer.bias.T)
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
