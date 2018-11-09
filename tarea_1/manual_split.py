import numpy as np


class Data:
    def __init__(self, file_name):
        self.db = np.loadtxt(open(file_name, "rb"), delimiter=",", skiprows=0, dtype=None)

        self.train_features = np.array([])
        self.train_classes = ()
        self.test_features = np.array([])
        self.test_classes = ()

        self.features = np.array([])
        self.classes = ()

    def run_split(self):

        np.random.shuffle(self.db)

        x = self.db[:, :-1]
        y = self.db[:, -1]

        self.features = x
        self.classes = y

        # x = self.db[:,1:]
        # y = self.db[:,1]

        number_clases = np.unique(self.classes)
        # self.db = np.array(sorted(self.db, key=lambda x: x[-1]))

        # number_clases contiene un arreglo con nuestras clases en este caso [1, 2, 3]
        tmp_classes_array = []
        for i in (number_clases):
            aux = [row for row in self.db if row[-1] == i]
            tmp_classes_array.append(aux)

        # Descomentar para obtener siempre la misma division de arreglos
        # np.random.seed(o)

        train = []
        test = []
        # extraemos el 20% de cada clase para el test y el 80% para entrenamiento
        for class_array in tmp_classes_array:
            tmp_train, tmp_test = np.split(class_array, [int(.8 * len(class_array))])
            train.append(tmp_train)
            test.append(tmp_test)

        train = np.vstack(train)
        test = np.vstack(test)

        self.train_features = train[:, :-1]
        self.train_classes = train[:, -1]
        self.test_features = test[:, :-1]
        self.test_classes = test[:, -1]

    # Separamos feaures de clases
    def run(self):
        np.random.shuffle(self.db)

        x = self.db[:, :-1]
        y = self.db[:, -1]

        self.features = x
        self.classes = y

    # Usamos esta funcion si se quiere una clasificacion binaria, filtramos las clases de manera binaria clases igual
    # a 1 son 0 y clases igual a 2 o 3 son 1
    # 1 (normal) 2 (hyperthyroidism) 3 (hypothyroidism), solo nos interesa normal o enfermo
    def filterClasss(self):
        for i in range(0, len(self.db)):
            # La clase se encuentra en el ultimo elemento del arreglo
            if self.db[i][-1] == 1:
                self.db[i][-1] = 0
            else:
                self.db[i][-1] = 1

    def normalize(self):

        min = self.db.min(axis=0)
        max = self.db.max(axis=0)
        max_min = max - min

        for i in range(len(self.db)):
            self.db[i] = np.divide((self.db[i] - min), max_min)
