Este programa permite aproximar AST, especificamente encontrar árboles de expresiones conociendo los resultado de la expresión dado un rago de valores de x.

Las expresiones se deben ingresar en post fijo:
	eq = ['x', 'x', '*', '5', '-', '10', 'x', '*', '+']
Dicha eq representa (((x*x)-5)+(10*x))
Estas expresiones se deben cambiar directamente en main.py
En main.py también es posible cambiar los parámetros y el dominio donde se evalua la expresión. Por defecto x esta entre 1 y 10.

Para ejecutar el programa se puede realizar usando un IDE o directamente desde un terminal.

$ python main.py <max_population> <generations> <mutation_rate> <tournament_size>

Se puede ejecutar main sin usar ningún parametro, en este caso sus valores por defecto son:
max_population = 500
generations = 10
mutation_rate = 0.01
tournament_size = 200


Por defecto el algoritmo genera poblaciones iniciales con arboles de 3 a 7 terminales. Si se desea que la poblacion inicial posea arboles mas grandes se debe cambiar directamente en el código, especificamente en la clase Population :(
Para expresiones como la mencionada anteriormente o similares a esta en tamaño, esta configuración deberia ser suficiente. 

Repo: 
Tarea
https://github.com/Hawkline451/Redes_Neuronales/tree/master/tarea_3


