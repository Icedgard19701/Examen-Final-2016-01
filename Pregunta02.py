a = int(input("Cantidad de numeros a evaluar: "))
datos = []
numeros = []

for i in range (0,a):
    x = int(input("Ingrese numero: "))
    datos.append(x)

for i in range (0,a-1):
    if datos[i+1] > datos[i]:
        y = datos[i+1]
        numeros.append(y)
    elif datos[i+1] < datos[i]:
        z = datos[i+1]    
        numeros.insert(0,z)



print(numeros)
