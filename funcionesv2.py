print("Funciones version 2")
print("Angel Alvarado")
# zona de listas tuplas set y diccionario
celulares = ["Samsung a52", "Iphone 11", "Chafa"]
empleados = ("Empleado1", "Empleado2", "Empleado3")
Pan = {"Pan blanco", "Pan dulce", "Pan de mantequilla"}
Carros = {
  "Marca ->": "Nissan",
  "Modelo ->": "Skyline",
  "Año -> ": 2013
}
# zona de funciones 
# Lista
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
# Tuplas
def vertupla(Empleados):
    for unempleado in Empleados:
        print(unempleado)
# Set
def verset(Panesito):
    for unpan in Panesito:
        print(unpan)
# Diccionario
def verDiccionario(Automovil):
    for unauto, uncarro in Automovil.items():
        print(unauto, uncarro)
# Llamadas a funciones
# Lista 
print("--imprime celulares--")
verlista(celulares)
# Tupla
print("--imprime empleados--")
vertupla(empleados)
# set 
print("--imprime pan--")
verset(Pan)
# Diccionario
print("--imprime carros--")
verDiccionario(Carros)
