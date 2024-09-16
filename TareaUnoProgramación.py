#%%
"""""
1.- ¿Qué es un paradigma de programación?

Se refiere a un enfoque o estilo de programación que proporciona una forma particular de pensar y estructurar los programas.

2.- ¿En qué se basa la programación orientada a objetos?

Es un método para organizar programas modulares y agrupar la información con comportamientos relacionados. Este está hecho de clases, las cuales describen a un grupo de objetos que comparten propiedades y métodos comunes, por lo cual actúa como una plantilla.

La clase se compone de información (campos, atributos, propiedades), y comportamiento (métodos, operaciones, funciones), y un objeto es una instancia de una clase.

Los beneficios de usar la programación orientada a objetos:

Es adecuada para crear aplicaciones triviales y complejas

Permite reutilizar el código

Se pueden incorporar fácilmente nuevas funcoines

Reduce los costos de producción y mantenimiento.

3.- ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación big 𝑂?

Iteración es cuando el mismo procedimiento se repite varias veces, lo cual se logra mediante dos tipos de bucles: for y while. El bucle for permite repetir un procedimiento un número determinado de veces configurado con el largo de una lista o un rango. El bucle while se implementa cuando se busca iterar hasta que se cumpla una condición determinada.

En cambio una función recursiva es cuando el cuerpo de esta se llama a sí misma, directa o indirectamente. Es decir, una función recursiva requiere la aplicación de dicha función varias veces. Estos implementan un caso base, formas de reducir el problema para luego resolverlo con recursividad, y formas de utilizar la solución de cada problema pequeño para resolver el problema más grande. Su uso más común es mediante la función "if" y "elif" o "else", las cuales permiten decir "ejecuta si ocurre la primera condición, y si no ocurre entonces pasa al siguiente caso.

La notación Big O es el lenguaje que se utiliza para hablar del tiempo que tarda en ejecutarse un algoritmo, y este puede variar en escala: O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n2) < O(2n) < O(n!). Esto se relaciona con la iteración y recursión ya que estos por cada ciclo que realicen dentro de un ciclo previo, aumenta de manera exponencial el tiempo necesario para ejecutar el código.

Ejemplo: Con respecto a la relación de la iteratividad con Big O, para un bucle for que se repite n veces, corresponde a escala O(n), pero si dentro del bucle hay otro "for" este pasa a ser O(n^2), y así aumenta exponencialmente su tiempo. Por otro lado para la recursividad se tendría que un

4.- Explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)

El rendimiento O(1) está definido por un paso o procedimiento que ocurre en un instante, por ejemplo una suma con números enteros, la cual no llama a una iteración o a recursividad. En cambio O(n) se refiere a un algoritmo que se repite n veces, como lo es el repetir una función con un for en una lista de n nímeros.

5.- ¿Cómo se calcula el orden en un programa que funciona por etapas?

Para calcular el orden se debe ver línea a línea del código clasificandolos en su orden, donde si existe uno de mayor a orden que otro es este el que predomina. Por ejemplo si una línea es O(1) y otra O(n), entonces hasta ese punto el código es de orden O(n), ya que O(1) < O(n).

6.- ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?

Se puede determinar en función de la cantidad de recursiones en cadena que tenga. Es decir, la complejidad temporal aumenta en función de las recursiones que existen dentro de otras recursiones, lo cual aumenta de manera exponencial en estos casos.
"""""

# %%
import time
import matplotlib.pyplot as plt

class PCB:

  def __init__(self,InDes,x,y):
    self.inicio_destino = InDes
    self.x = x
    self.y = y

  def suma_x (self, suma_x):
    self.x += suma_x

  def suma_y (self, suma_y):
    self.y += suma_y

print("Clase creada PCB")



# %%
""""
Caso general función recursiva, donde el punto B puede estar en cualquier dirección con respecto al punto A

"""

# Función para contar caminos de A a B considerando cualquier dirección
def movimientoABRecGeneral(coord1, coord2):
    # Desempaquetar las coordenadas
    c, d = coord1
    e, f = coord2
    A = PCB("Posición_Inicial", c, d)
    B = PCB("Posición_Final", e, f)

    # Si llegamos al destino, cuenta un camino
    if A.x == B.x and A.y == B.y:
        return 1

    # Inicializamos la cuenta de movimientos posibles
    total_movimientos = 0

    # Continuamos moviéndonos en todas las direcciones posibles
    if A.x < B.x:  # Podemos movernos a la derecha
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_x(1)
        total_movimientos += movimientoABRecGeneral((nueva_A.x, nueva_A.y), (B.x, B.y))

    if A.x > B.x:  # Podemos movernos a la izquierda
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_x(-1)
        total_movimientos += movimientoABRecGeneral((nueva_A.x, nueva_A.y), (B.x, B.y))

    if A.y < B.y:  # Podemos movernos hacia arriba
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_y(1)
        total_movimientos += movimientoABRecGeneral((nueva_A.x, nueva_A.y), (B.x, B.y))

    if A.y > B.y:  # Podemos movernos hacia abajo
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_y(-1)
        total_movimientos += movimientoABRecGeneral((nueva_A.x, nueva_A.y), (B.x, B.y))

    return total_movimientos

# Pruebas
print("Caso general recursivo")
print("Caso (6,0) a (7,2):")
print("Caso (7,2) a (6,0):")
print("Caso (0,0) a (6,2):")
print("Caso (0,0) a (2,6):")

print(movimientoABRecGeneral((6, 0), (7, 2)))  # Caminos de (6,0) a (7,2) -> 3
print(movimientoABRecGeneral((7, 2), (6, 0)))  # Caminos de (7,2) a (6,0) -> 3
print(movimientoABRecGeneral((0, 0), (6, 2)))  # Caminos de (0,0) a (6,2) -> 28
print(movimientoABRecGeneral((0, 0), (2, 6)))  # Caminos de (0,0) a (2,6) -> 28



# %%

"""
Caso simplificado función recursiva, donde B está en el cuadrante arriba a la derecha con respecto a A

"""

import time
import matplotlib.pyplot as plt

# Función para contar caminos de A a B considerando solo movimientos a la derecha y hacia arriba
def movimientoABRec(coord1, coord2):
    # Desempaquetar las coordenadas
    c, d = coord1
    e, f = coord2
    A = PCB("Posición_Inicial", c, d)
    B = PCB("Posición_Final", e, f)

    # Si llegamos a B, cuenta un camino
    if A.x == B.x and A.y == B.y:
        return 1  # Hay un camino válido cuando llegamos al destino

    # Inicializamos la cuenta de movimientos posibles
    total_movimientos = 0

    # Si no hemos alcanzado la coordenada final, continuamos
    if A.x < B.x:  # Podemos movernos a la derecha
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_x(1)
        total_movimientos += movimientoABRec((nueva_A.x, nueva_A.y), (B.x, B.y))

    if A.y < B.y:  # Podemos movernos hacia arriba
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_y(1)
        total_movimientos += movimientoABRec((nueva_A.x, nueva_A.y), (B.x, B.y))

    return total_movimientos

# Pruebas
print("Caso simplificado recursivo, B a la derecha arriba de A")
print("Caso (6,0) a (7,2):")
print("Caso (0,0) a (6,2):")
print("Caso (0,0) a (2,6):")

print(movimientoABRec((6, 0), (7, 2)))  # Caminos de (6,0) a (7,2)
print(movimientoABRec((0, 0), (6, 2)))  # Caminos de (0,0) a (6,2)
print(movimientoABRec((0, 0), (2, 6)))  # Caminos de (0,0) a (2,6)


# %%
"""
Se grafica los tiempos del método Recursivo

"""

# Nueva función para medir el tiempo de ejecución acumulado
def medir_tiempos_acumulados(coordenadas_inicial, coordenadas_final):
    tiempos_acumulados = []
    tiempo_total = 0
    puntos = []

    # Recorrer todas las posibles coordenadas finales desde (0,0) hasta coordenadas_final
    for x in range(coordenadas_inicial[0], coordenadas_final[0] + 1):
        for y in range(coordenadas_inicial[1], coordenadas_final[1] + 1):
            start_time = time.time()
            movimientoABRec(coordenadas_inicial, (x, y))
            end_time = time.time()
            
            # Calcular el tiempo de ejecución para este paso
            elapsed_time = end_time - start_time
            tiempo_total += elapsed_time  # Acumular el tiempo de ejecución
            tiempos_acumulados.append(tiempo_total)
            puntos.append((x, y))
    print("Gráfico tiempo de ejecución Recursivo, caso de ejemplo (0,0) a (12,9)")
    # Graficar los resultados
    plt.plot(range(len(tiempos_acumulados)), tiempos_acumulados, marker='o')
    plt.xlabel('Número de puntos alcanzados')
    plt.ylabel('Tiempo de ejecución acumulado (segundos)')
    plt.title('Tiempo de ejecución acumulado del Caso Recursivo')
    plt.grid(True)
    plt.show()

# Uso de la función para calcular tiempos acumulados desde (0,0) hasta cualquier coordenada final, por ejemplo, (5, 5)
medir_tiempos_acumulados((0, 0), (12, 9))


# %%
"""
Método Iterativo caso generalizado

"""


# Función iterativa generalizada para contar caminos de A a B en cualquier dirección
def movimientoABIterwhileGeneralizada(coord1, coord2):
    # Desempaquetar las coordenadas
    c, d = coord1
    e, f = coord2
    A = PCB("Posición_Inicial", c, d)
    B = PCB("Posición_Final", e, f)

    # Si llegamos a B, cuenta un camino
    if A.x == B.x and A.y == B.y:
        return 1  # Hay un camino válido cuando llegamos al destino

    # Inicializamos la cuenta de caminos posibles
    caminos = 0

    # Movimientos hacia la derecha
    if A.x < B.x:
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_x(1)
        caminos += movimientoABIterwhileGeneralizada((nueva_A.x, nueva_A.y), (B.x, B.y))

    # Movimientos hacia la izquierda
    if A.x > B.x:
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_x(-1)
        caminos += movimientoABIterwhileGeneralizada((nueva_A.x, nueva_A.y), (B.x, B.y))

    # Movimientos hacia arriba
    if A.y < B.y:
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_y(1)
        caminos += movimientoABIterwhileGeneralizada((nueva_A.x, nueva_A.y), (B.x, B.y))

    # Movimientos hacia abajo
    if A.y > B.y:
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_y(-1)
        caminos += movimientoABIterwhileGeneralizada((nueva_A.x, nueva_A.y), (B.x, B.y))

    return caminos

# Pruebas
print("Caso Iterativo Generalizado")
print("Caso (6,0) a (7,2):")
print("Caso (7,2) a (6,0):")
print("Caso (0,0) a (6,2):")
print("Caso (0,0) a (2,6):")
print(movimientoABIterwhileGeneralizada((6, 0), (7, 2)))  # Caminos de (6,0) a (7,2)
print(movimientoABIterwhileGeneralizada((7, 2), (6, 0)))  # Caminos de (7,2) a (6,0)
print(movimientoABIterwhileGeneralizada((0, 0), (6, 2)))  # Caminos de (0,0) a (6,2)
print(movimientoABIterwhileGeneralizada((0, 0), (2, 6)))  # Caminos de (0,0) a (2,6)

#%%
"""
Método iterativo simplificado

"""

# Función iterativa para contar caminos de A a B moviéndose solo a la derecha y hacia arriba
def movimientoABIterwhile(coord1, coord2):
    # Desempaquetar las coordenadas
    c, d = coord1
    e, f = coord2
    A = PCB("Posición_Inicial", c, d)
    B = PCB("Posición_Final", e, f)

    # Si llegamos a B, cuenta un camino
    if A.x == B.x and A.y == B.y:
        return 1  # Hay un camino válido cuando llegamos al destino

    # Inicializamos la cuenta de caminos posibles
    caminos = 0

    # Si no hemos alcanzado la coordenada final, continuamos
    if A.x < B.x:  # Podemos movernos a la derecha
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_x(1)
        caminos += movimientoABIterwhile((nueva_A.x, nueva_A.y), (B.x, B.y))

    if A.y < B.y:  # Podemos movernos hacia arriba
        nueva_A = PCB("Posición_Inicial", A.x, A.y)
        nueva_A.suma_y(1)
        caminos += movimientoABIterwhile((nueva_A.x, nueva_A.y), (B.x, B.y))

    return caminos

# Pruebas
print("Caso simplificado iterativo, B a la derecha arriba de A")
print("Caso (6,0) a (7,2):")
print("Caso (0,0) a (6,2):")
print("Caso (0,0) a (2,6):")
print(movimientoABIterwhile((6, 0), (7, 2)))  # Caminos de (6,0) a (7,2) -> Debe dar 3
print(movimientoABIterwhile((0, 0), (6, 2)))  # Caminos de (0,0) a (6,2) -> Debe dar 28
print(movimientoABIterwhile((0, 0), (2, 6)))  # Caminos de (0,0) a (2,6) -> Debe dar 28


#%%
"""
Graficar caso Iterativo
"""
import time
import matplotlib.pyplot as plt

# Nueva función para medir el tiempo de ejecución acumulado
def medir_tiempos_iterativo_acumulados(coordenadas_inicial, coordenadas_final):
    tiempos_acumulados = []
    tiempo_total = 0
    puntos = []

    # Recorrer todas las posibles coordenadas finales desde coordenadas_inicial hasta coordenadas_final
    for x in range(coordenadas_inicial[0], coordenadas_final[0] + 1):
        for y in range(coordenadas_inicial[1], coordenadas_final[1] + 1):
            start_time = time.time()
            movimientoABIterwhile(coordenadas_inicial, (x, y))
            end_time = time.time()
            
            # Calcular el tiempo de ejecución para este paso
            elapsed_time = end_time - start_time
            tiempo_total += elapsed_time  # Acumular el tiempo de ejecución
            tiempos_acumulados.append(tiempo_total)
            puntos.append((x, y))
    print("Gráfico tiempo de ejecución Iterativo, caso de ejemplo (0,0) a (12,9)")

    # Graficar los resultados
    plt.plot(range(len(tiempos_acumulados)), tiempos_acumulados, marker='o')
    plt.xlabel('Número de puntos alcanzados')
    plt.ylabel('Tiempo de ejecución acumulado (segundos)')
    plt.title('Tiempo de ejecución acumulado de movimientoABIterwhile')
    plt.grid(True)
    plt.show()

# Uso de la función para calcular tiempos acumulados desde (0,0) hasta (5,5)
medir_tiempos_iterativo_acumulados((0, 0), (12, 9))
# %%
