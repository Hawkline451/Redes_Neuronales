Vendedor Viajero
El script node_generator, genera nodos para el grafo aleatoriamente y los guarda en generated_nodes.csv
Se puede correr el algoritmo genetico desde main.py cambiando los paramatros directamente desde el codigo fuente o se puede ejecutar desde la consola con sus respectivos argumentos.
El algoritmo lee el archivo csv para generar el grafo.

$ python main.py <max_population> <generations> <mutation_rate> <tournament_size>

Si no se ingresan o no se cambian los parametros sus valores por defecto son:
max_population = 30
generations = 250
mutation_rate = 0.01
tournament_size = 15

Repo: 
Tarea
https://github.com/Hawkline451/Redes_Neuronales/tree/master/tarea_2

Adivinar palabras o bits
Para probar diferentes palabras se deben modificar el arreglo de en main, por ejemplo 
	word = ['0','1','1','0','0','1']
	word = ['r','i','p']
Notar que los idividuos los crea eligiendo al azar letras de la palabra original, en el caso de bits elije dentro del arreglo 0 o 1, pero en el caso de una palabra con letras solo escoje usando las letras de la palabra, es posible corregir eso modificando <self.new_word[gene_idx] = np.random.choice(self.word)>, colocando el alfabeto completo solo proboca que se demore mas en adivinar :p
https://github.com/Hawkline451/Redes_Neuronales/blob/master/find_word.py
