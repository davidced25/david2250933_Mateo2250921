class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecho)

    # a) Peso del árbol: Número total de nodos
    def obtener_peso(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.obtener_peso(nodo.izquierdo) + self.obtener_peso(nodo.derecho)

    # b) Orden: Se refiere al grado máximo de los nodos (en árbol binario es 2)
    def obtener_orden(self):
        return 2

    # c) Altura: Longitud del camino más largo desde la raíz a una hoja
    def obtener_altura(self, nodo):
        if nodo is None:
            return -1  # Un árbol vacío tiene altura -1, un nodo raíz tiene altura 0
        
        altura_izq = self.obtener_altura(nodo.izquierdo)
        altura_der = self.obtener_altura(nodo.derecho)
        
        return 1 + max(altura_izq, altura_der)

# --- Lógica de ingreso por teclado ---
def menu():
    arbol = ArbolBinario()
    print("--- Creador de Árbol Binario ---")
    
    while True:
        entrada = input("Ingrese un número para el nodo (o 'salir' para finalizar): ")
        if entrada.lower() == 'salir':
            break
        try:
            valor = int(entrada)
            arbol.insertar(valor)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    if arbol.raiz:
        print("\n--- Propiedades del Árbol ---")
        print(f"a) Peso del árbol (nodos): {arbol.obtener_peso(arbol.raiz)}")
        print(f"b) Orden del árbol: {arbol.obtener_orden()}")
        print(f"c) Altura del árbol: {arbol.obtener_altura(arbol.raiz)}")
    else:
        print("El árbol está vacío.")

if __name__ == "__main__":
    menu()
