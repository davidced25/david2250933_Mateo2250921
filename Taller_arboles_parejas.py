class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.padre = None
        self.hijos = []   # para poder guardar lo hijos y que se conecten ocn el padre

class arbol:
    def __init__(self):
        self.raiz = None

    def insertar_nodo(self, dato):
        padre=None
        nuevo = nodo(dato)

        # Si el árbol está vacío → se vuelve raíz
        if self.raiz is None:
            self.raiz = nuevo
            return nuevo

        # Si se especifica un padre
        if padre:
            nuevo.padre = padre
            padre.hijos.append(nuevo)
            return nuevo

    # Buscar nodo por valor
    def buscar(self, actual, dato):
        if actual is None:
            return None

        if actual.dato == dato:
            return actual

        for hijo in actual.hijos:
            encontrado = self.buscar(hijo, dato)
            if encontrado:
                return encontrado

        return None
#por el momento estamos analizando con la creacion inicial de nodos donde nos estamos basando en lo inicial de listas simples
