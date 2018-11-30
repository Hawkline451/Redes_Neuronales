import numpy as np

# Pequeña clase que permite leer archivos cvs para usarlos como numpy array
class Data:
    def __init__(self, file_name):
        self.data = np.loadtxt(open(file_name, "rb"), delimiter=",", skiprows=0, dtype=None)

    def get_array(self):
        return self.data