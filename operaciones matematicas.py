#Ejercicio sumar, restar, multiplicar y dividir dos numeros.

#ALGORITMO
#Dos variables que guarden la informacion de los valores de entrada.
#Una variable que guarden el resultado de la operacion.
#Comprobar si los valores introducidos por el usuario, son numeros o no son (ambos)
    #Si son numeros, hacer la correspondiente operacion.
    #Si no, escribir "parametros de entrada no validos"



import numbers

def operaciones(N1, N2):
    num1 = N1
    num2 = N2
    resultado = 0
    listaResultados=(0,0,0,0)

    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):

        #Suma de dos valores (+)
        listaResultados[0] = num1 + num2
        
        #Resta de dos valores (-)
        listaResultados[1] = num1 - num2

        #Multiplicacion de dos valores (*)
        listaResultados[2] = num1 * num2

        #Division de dos valores (/)
        listaResultados[3] = num1 / num2 

        for i in range (0, len(listaResultados)):
            print("El resultado de la operacion es..")
            print(listaResultados[i])
    
    else:
        print("ERROR")
operaciones(4,2)