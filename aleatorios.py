"""
Irania Aguinaga Muñoz 
Descripción: Fichero que implementa un generador de números aleatorios 
usando el algoritmo Lineal Congruente (LGC).
"""

class Aleat:
    """
    Clase que implementa un generador de números aleatorios LGC como un iterador.
    
    Atributos:
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        x (int): Estado actual (semilla/valor generado).

    Métodos:
        __next__(): Calcula y devuelve el siguiente número aleatorio.
        __call__(x0): Reinicia la secuencia con una nueva semilla.
        
    Pruebas unitarias:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m, self.a, self.c, self.x = m, a, c, x0

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0):
        """Reinicia la semilla de forma posicional."""
        self.x = x0

def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números aleatorios usando LGC.
    
    Argumentos:
        m, a, c: Parámetros del algoritmo.
        x0: Semilla inicial.
    
    Yields:
        int: Siguiente número de la secuencia.
        
    Pruebas unitarias:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        reinicio = yield x
        if reinicio is not None:
            x = reinicio

if __name__ == "__main__":
    import doctest
    doctest.testmod()