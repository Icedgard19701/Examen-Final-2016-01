a = int(input("Cantidad de numeros a evaluar: "))
datos = []

for i in range (0,a):
    x = int(input("Ingrese numero: "))
    datos.append(x)

datos.reverse()
reversed(datos)


print(datos)
