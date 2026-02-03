#.add permite agregar elementos al set
set1 = {"manzana", "pera", "uva"}
set1.add("naranja")
print(set1)

#print(set1[0]) -> No es permitido el acceso por medio de indice []
print("\n----------------------------------------------------------------")
#update = permite agregar un conjunto (set), al conjunto actual
#se puede agregar lista, diccionarios, tuplas
set1 = {"manzana", "pera", "uva"}
tropical_set = {"piña", "mango", "papaya"}

set1.update(tropical_set)
print(set1)

lista_frutas = ["kiwi", "coco", "fresa"]
set1.update(lista_frutas)
print(set1)