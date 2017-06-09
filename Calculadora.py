
print("*********  Calculadora beta 0.1 ***********")
print("*           Por marco Azúa Ulloa          *")
print("*********  Bienvenido Señor/a   ***********")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


numero = int(float(input("Ingresa un numero: ")))
numero_2 = int(float(input("Ingresa el segundo numero: ")))

print("Opciones\n1.- Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir")

operaciones = {'1': sumar, '2': restar, '3': multiplicar, '4': dividir}

seleccion = input('Ahora escoga una opcion: ')

try:
    resultado = operaciones[seleccion](int(numero), int(numero_2))
    print(resultado)
except ValueError:
    print("Escoga una opcion valida")
