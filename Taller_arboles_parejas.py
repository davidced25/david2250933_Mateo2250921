class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None
        self.siguiente = None  # lista enlazada


class Arbol:
    def __init__(self):
        self.raiz = None
        self.cabeza = None

    def crear_nodo(self, valor, valor_padre=None):
        nuevo = Nodo(valor)

        # Árbol vacío → crear raíz
        if self.raiz is None:
            self.raiz = nuevo
            self.cabeza = nuevo
            print("Raíz creada")
            return

        # Buscar el padre
        actual = self.cabeza
        padre = None

        while actual is not None:
            if actual.valor == valor_padre:
                padre = actual
                break
            actual = actual.siguiente

        if padre is None:
            print("Padre no encontrado")
            return

        nuevo.padre = padre
        print("Nodo creado")

        # Insertar en la lista enlazada
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    # a) Peso
    def peso(self):
        contador = 0
        actual = self.cabeza

        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador

    # c) Altura
    def altura(self):
        if self.raiz is None:
            return 0

        max_altura = 0
        actual = self.cabeza

        while actual is not None:
            altura = 0
            nodo_temp = actual

            while nodo_temp.padre is not None:
                altura += 1
                nodo_temp = nodo_temp.padre

            if altura > max_altura:
                max_altura = altura

            actual = actual.siguiente

        return max_altura + 1

    # b) Orden
    def orden(self):
        max_hijos = 0
        actual = self.cabeza

        while actual is not None:
            hijos = 0
            aux = self.cabeza

            while aux is not None:
                if aux.padre == actual:
                    hijos += 1
                aux = aux.siguiente

            if hijos > max_hijos:
                max_hijos = hijos

            actual = actual.siguiente

        return max_hijos

#Menu
arbol = Arbol()

while True:
    print("\nMENÚ")
    print("1. Crear árbol")
    print("2. Peso del árbol")
    print("3. Altura del árbol")
    print("4. Orden del árbol")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        while True:
            valor = input("Valor del nodo: ")

            if arbol.raiz is None:
                arbol.crear_nodo(valor)
            else:
                padre = input("Valor del padre: ")
                arbol.crear_nodo(valor, padre)

            continuar = input("¿Desea agregar otro nodo? (s/n): ").lower()
            if continuar != "s":
                break

    elif opcion == 2:
        print("Peso del árbol:", arbol.peso())

    elif opcion == 3:
        print("Altura del árbol:", arbol.altura())

    elif opcion == 4:
        print("Orden del árbol:", arbol.orden())

    elif opcion == 5:
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
#por el momento estamos analizando con la creacion inicial de nodos donde nos estamos basando en lo inicial de listas simples
