print("*********  Calculadora beta 0.1 ***********")
print("*          Por marco Azúa Ulloa          *")
print("*********   Bienvenido Señor/a   ***********")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def Menu():
    print("Opciones: \n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir\n5.-Salir")

def MenuOpcion():
    print("¿Desea hacer otra operacion?: \n1.-Si\n2.-No")
    
def no():
    print("Gracias por usar la aplicacion")

try:
    while True:
        numero = int(input("Ingresa un numero: "))
        numero_2 = int(input("Ingresa el segundo numero: "))
        Menu()
        operaciones = {'1': sumar, '2': restar,
                       '3': multiplicar, '4': dividir, '5': 'salir'}
        seleccion = input('Ahora escoja una opcion: ')
        if(int(seleccion) == 5):
            no()
            break
        else:            
            resultado = operaciones[seleccion](int(numero), int(numero_2))
            print("El resultado es: " + str(resultado) )       
            opcion = {'1': 'si', '2': no}
            MenuOpcion()
            select = input("Escoja una opcion ")
            result = opcion[select]
            if(int(select) == 1):
                True
            else:
                no()
                break
except ValueError:
    print("Escoga una opcion valida")
