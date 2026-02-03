print("--------------------------------")
#Si inserta más elementos de los que reemplaza, 
# los nuevos elementos se insertarán donde especificó, 
# y los elementos restantes se moverán en consecuencia
frutas = ["manzana", "fresa", "uva"]
frutas[1:2] = ["mango", "melon"]
print(frutas)

print("--------------------------------")
#Si inserta menos elementos de los que reemplaza, 
# los nuevos elementos se insertarán donde especificó, 
# y los elementos restantes se moverán en consecuencia:

frutas = ["manzana", "fresa", "uva"]
frutas[1:3] = ["mango"]
print(frutas)

frutas = ["manzana", "fresa", "uva", "pera"]
frutas[1:3] = ["mango"]
print(frutas)