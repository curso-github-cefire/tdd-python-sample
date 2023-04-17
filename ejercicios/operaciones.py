# En principio el alumno solo recibiría la definición de la función en el archivo correspondiente
def suma(x,y):

    # El alumno deberá implementar correctamente el código de la función para pasar el test correspondiente
    return x + y

# Operación resta de dos números
def resta(x,y):
    
    return x - y

"""esPar: 
Función que comprueba si un número dado es par o no
Un número es par si es un número entero y es divisible por 2. 
Expresados matemáticamente, incluso los números enteros está en la forma 2k donde está un número entero k. 
En la notación del conjunto, incluso los números enteros son {x|x=2k, k está en Z} = {…, -4, -2, 0, 2, 4,…}.

Parameters
----------
x : entero
    La función debe recibir un parámetro entero

Returns
-------
Boolean
    Devuelve un valor booleano, True si es par y False si no lo es
"""
def esPar(x):
    return x % 2 == 0

"""Factorial: factorial de n es el producto de todos los números enteros a partir de la 1 a n, inclusivo. 
La marca de exclamación (!) es el operador unario que representa factorial. La expresión “5!" se lee, “cinco factoriales? 
y los medios 1·2·3·4·5 que iguales 120. 
Factorial cero (0!) se trata como un caso especial y se define para ser 0! = 1. 
A este nivel de las matemáticas, la n en n! debe ser un número entero no negativo.

Parameters
----------
x : entero
    La función debe recibir un parámetro entero

Returns
-------
entero
    Devuelve el factorial del número pasado como párametro
"""
def factorial(x):
    if (x<0):
        raise ValueError("El parámetro debe ser mayor o igual que 0")
    if x==0 or x==1: 
        return 1
    cont = 1
    for i in range(1, x+1):
        cont = cont * i 
    return cont

