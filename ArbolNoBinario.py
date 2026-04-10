from bigtree import Node

# Crear nodo raíz
raiz = Node("Raíz", edad=100)

# Hijos directos (no binario: 3 hijos)
hijo1 = Node("Hijo1", edad=50, parent=raiz)
hijo2 = Node("Hijo2", edad=60, parent=raiz)
hijo3 = Node("Hijo3", edad=55, parent=raiz)

# Nietos bajo Hijo2 (otro nivel no binario)
nieto1 = Node("Nieto1", edad=30, parent=hijo2)
nieto2 = Node("Nieto2", edad=35, parent=hijo2)

# Visualizar
print(raiz.show(attr_list=["edad"]))
