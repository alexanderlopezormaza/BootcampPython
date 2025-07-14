def verificar_semaforo(color):
    """
    Función que verifica el estado del semáforo según el color ingresado
    
    Args:
        color (str): Color del semáforo (verde, amarillo, rojo)
    
    Returns:
        str: Mensaje correspondiente al color del semáforo
    """
    # Convertir a minúsculas para facilitar la comparación
    color = color.lower()
    
    if color == "verde":
        return "Usted puede pasar sin problema"
    elif color == "amarillo":
        return "Usted puede pasar con dificultades"
    elif color == "rojo":
        return "Usted no puede pasar bajo ningún concepto"
    else:
        return "Color no válido. Por favor ingrese: verde, amarillo o rojo"

def main():
    """
    Función principal que solicita el color al usuario y muestra el resultado
    """
    print("=== SISTEMA DE SEMÁFORO ===")
    print("Colores válidos: verde, amarillo, rojo")
    print("(Puede escribir en mayúsculas o minúsculas)")
    print("-" * 40)
    
    # Solicitar el color al usuario
    color_usuario = input("Ingrese el color del semáforo: ")
    
    # Verificar el color y mostrar el mensaje
    mensaje = verificar_semaforo(color_usuario)
    print(f"\n{mensaje}")

# Función alternativa que recibe el color como parámetro
def semaforo_con_parametro(color_parametro):
    """
    Función que puede ser llamada pasando el color como parámetro
    
    Args:
        color_parametro (str): Color del semáforo
    """
    print(f"Color ingresado: {color_parametro}")
    mensaje = verificar_semaforo(color_parametro)
    print(mensaje)

if __name__ == "__main__":
    # Ejecutar el programa principal
    main()
    
    print("\n" + "="*50)
    print("EJEMPLOS DE USO CON PARÁMETROS:")
    print("="*50)
    
    # Ejemplos de uso pasando parámetros
    colores_ejemplo = ["verde", "VERDE", "amarillo", "AMARILLO", "rojo", "ROJO", "azul"]
    
    for color in colores_ejemplo:
        print(f"\nColor: {color}")
        semaforo_con_parametro(color)