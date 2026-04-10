
class nodo:
    def __init__(self, valor):
        self.dato = dato
        self.padre = None
        self.siguiente = None  # lista enlazada


class arbol:
    def __init__(self):
        self.raiz = None
        self.cabeza = None

    def crear_nodo(self, dato):
        dato_padre=None
        nuevo = nodo(dato)

        # comienzo creando la raiz
        if self.raiz is None:
            self.raiz = nuevo
            self.cabeza = nuevo
            print("raiz creada")
            return

        # Buscar el padre
        actual = self.cabeza
        padre = None

        while actual is not None:
            if actual.dato == dato_padre:
                padre = actual
                break
            actual = actual.siguiente

        if padre is None:
            print("padre no encontrado")
            return

        nuevo.padre = padre
        print("Nodo creado")

        # Insertar en la lista enlazada
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    #Peso
    def peso(self):
        contadorPeso = 0
        actual = self.cabeza

        while actual is not None:
            contadorPeso += 1
            actual = actual.siguiente
        return contadorPeso

    # Altura
    def altura(self):
        if self.raiz is None:
            return 0

        max_altura = 0
        actual = self.cabeza

        while actual is not None:
            altura = 0
            nodo_act = actual
            while nodo_act.padre is not None:
                altura += 1
                nodo_act = nodo_act.padre
            if altura > max_altura:
                max_altura = altura

            actual = actual.siguiente

        return max_altura + 1

    #Orden
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

#Menu que llama las funciones ya definidas anteriormente:
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
                arbol.crear_nodo(dato)
            else:
                padre = input("Valor del padre: ")
                arbol.crear_nodo(dato)

            seguir = input("Desea agregar otro nodo? (s/n): ").lower()
            if seguir != "s":
                break

    elif opcion == 2:
        print("Peso del arbol:", arbol.peso())

    elif opcion == 3:
        print("Altura del arbol:", arbol.altura())

    elif opcion == 4:
        print("Orden del arbol:", arbol.orden())

    elif opcion == 5:
        print("saliendo es saliendo")
        break

    else:
        print("opcion no valida")
#por el momento estamos analizando con la creacion inicial de nodos donde nos estamos basando en lo inicial de listas simples
