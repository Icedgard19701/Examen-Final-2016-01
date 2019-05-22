a = int(input("Cantidad de numeros a evaluar: "))
datos = []

for i in range (0,a):
    x = int(input("Ingrese numero: "))
    datos.append(x)

def ordenar_max(datos):
    for i in range(len(datos)):
        for j in range(len(datos)):
          if datos[i] > datos[j]:
            tmp = datos[i]
            datos[i] = datos[j]
            datos[j] = tmp

print(datos)
