
import numbers

def fib(numero):
    #Precondicion: El valor de entrada debe ser un numero entero

    #Definicion de las variables a emplear
    a = 0
    b = 1

    #Se comprueba que el valor de entrada es un numero entero
    #si el valor no es un numero, entonces se le dice al usuario que el valor es incorrecto y que vuelva a probarlo.
    #en caso de que no, pues se ejecuta el algoritmo.
    if isinstance(numero, numbers.Number):
        print("es un numero")

        while a < numero:
                print(a, end='')
                a = b
                b = a + b

                #valores de salida
                print()
        
        print("fin del programa")

    else:
         print("no es un numero")
         print("el programa ha finalizado por que no se ha introducido un valor valido")

fib("numero")
#Precondiciones
#El parametro que va a recibir la funcion, debe ser numerico.
