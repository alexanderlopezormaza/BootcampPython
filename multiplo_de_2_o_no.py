def es_multiplo_de_2(numero):
    """
    Determina si un número es múltiplo de 2.
    
    Args:
        numero (int): El número a verificar
        
    Returns:
        bool: True si es múltiplo de 2, False en caso contrario
    """
    return numero % 2 == 0

def main():
    # Solicitar el número al usuario
    try:
        num = int(input("Ingresa un número: "))
        
        if es_multiplo_de_2(num):
            print(f"El número {num} SÍ es múltiplo de 2")
        else:
            print(f"El número {num} NO es múltiplo de 2")
            
    except ValueError:
        print("Error: Por favor ingresa un número válido")

# Versión que recibe el número como parámetro
def verificar_multiplo(numero):
    """
    Función que recibe un número como parámetro y verifica si es múltiplo de 2.
    
    Args:
        numero (int): Número a verificar
        
    Returns:
        str: Mensaje indicando si es múltiplo de 2 o no
    """
    if numero % 2 == 0:
        return f"El número {numero} SÍ es múltiplo de 2"
    else:
        return f"El número {numero} NO es múltiplo de 2"

# Ejecutar el programa principal
if __name__ == "__main__":
    main()