# Red Neuronal

### Prerequisitos
NumPy ==
Python >= 3.6

### Comentarios

Se agregó una clase que separa conjuntos de entranamiento usando una libreria externa (scikit learn) pero no es necesario usarlo.
El archivo manual_split.py cumple la misma función pero sin usar librerias externas. 
Claramente scikit raliza diferentes tipos de validaciones y entrega mejores conjuntos que manual_split.py

Para probar el programa se debe ejecutar main.py , dentro de este archivo encontramos variables que pueden ser modificadas para realizar distintas pruebas como son la cantidad de epocas (1000 por defecto), learning rate (.1) y la cantidad de capas con sus respectivas neuronas.

Al ejecutar el programa se obtienen 2 plots (error y precision) y se imprime en consola la precision de la red luego de ser entrenada, para el conjunto de entrenamiento y prueba. 
