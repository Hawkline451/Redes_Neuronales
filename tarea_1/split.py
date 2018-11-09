import numpy as np
from sklearn.model_selection import train_test_split


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

        # Train Test split valida internamente la representatividad de las clases.
        self.train_features, self.test_features, self.train_classes, self.test_classes = train_test_split(
            x, y, test_size=0.2)

        '''
        #self.train_classes = normalize(self.train_classes)
        self.train_features = normalize(self.train_features)
        #self.test_classes = normalize(self.test_classes)
        self.test_features = normalize(self.test_features)
        '''

    def run(self):
        np.random.shuffle(self.db)

        x = self.db[:, :-1]
        y = self.db[:, -1]

        self.features = x
        self.classes = y

    # Filtramos las clases de manera binaria clases igual a 1 son 0 y clases igual a 2 o 3 son 1
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


'''
d = Data('out.csv')
#d .filterClasss()
d.run()
print(d.classes)
print(d.features)
'''
