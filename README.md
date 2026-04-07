class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []  # Lista enlazada de hijos

class ArbolNario:
    def __init__(self):
        self.raiz = None

    def establecer_raiz(self, nombre):
        self.raiz = Nodo(nombre)
        print(f"Raíz '{nombre}' creada.")

    def buscar_nodo(self, actual, nombre):
        """Busca un nodo por su nombre de forma recursiva."""
        if actual is None:
            return None
        if actual.nombre == nombre:
            return actual
        for hijo in actual.hijos:
            encontrado = self.buscar_nodo(hijo, nombre)
            if encontrado:
                return encontrado
        return None

    def añadir_hijo(self, nombre_padre, nombre_hijo):
        padre = self.buscar_nodo(self.raiz, nombre_padre)
        if padre:
            nuevo_hijo = Nodo(nombre_hijo)
            padre.hijos.append(nuevo_hijo)
            print(f"Nodo '{nombre_hijo}' añadido como hijo de '{nombre_padre}'.")
        else:
            print(f"Error: No se encontró el padre '{nombre_padre}'.")

    # a) Peso del árbol (Total de nodos)
    def obtener_peso(self, nodo):
        if nodo is None:
            return 0
        total = 1
        for hijo in nodo.hijos:
            total += self.obtener_peso(hijo)
        return total

    # b) Orden del árbol (Máximo número de hijos que tiene un solo nodo)
    def obtener_orden(self, nodo, max_orden=0):
        if nodo is None:
            return max_orden
        
        # El orden local es la cantidad de hijos de este nodo
        orden_actual = len(nodo.hijos)
        max_orden = max(max_orden, orden_actual)
        
        for hijo in nodo.hijos:
            max_orden = self.obtener_orden(hijo, max_orden)
            
        return max_orden

    # c) Altura del árbol
    def obtener_altura(self, nodo):
        if nodo is None or not nodo.hijos:
            return 0
        
        max_altura_hijos = 0
        for hijo in nodo.hijos:
            max_altura_hijos = max(max_altura_hijos, self.obtener_altura(hijo))
            
        return 1 + max_altura_hijos

# --- Interfaz por teclado ---
def ejecutar_programa():
    arbol = ArbolNario()
    
    print("1. Establecer Raíz")
    nombre_raiz = input("Nombre de la raíz: ")
    arbol.establecer_raiz(nombre_raiz)

    while True:
        print("\n--- MENÚ ---")
        print("1. Añadir hijo")
        print("2. Ver Propiedades (Peso, Orden, Altura)")
        print("3. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            padre = input("¿A qué nodo padre desea añadirle un hijo?: ")
            hijo = input("Nombre del nuevo nodo hijo: ")
            arbol.añadir_hijo(padre, hijo)
        
        elif opcion == "2":
            print(f"\n[PROPIEDADES]")
            print(f"Peso: {arbol.obtener_peso(arbol.raiz)}")
            print(f"Orden: {arbol.obtener_orden(arbol.raiz)}")
            print(f"Altura: {arbol.obtener_altura(arbol.raiz)}")
            
        elif opcion == "3":
            break

if __name__ == "__main__":
    ejecutar_programa()



    
