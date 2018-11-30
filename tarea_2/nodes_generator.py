import numpy as np

# Pequeño script que nose genera los pueblos para el problema del vendedor viajero

# Enteros en el rango de [0, 200], 20 filas, 2 columnas
nodes = np.random.randint(200, size=(20, 2))
nodes.astype(int)
np.savetxt("generated_nodes.csv", nodes, delimiter=",")