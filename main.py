"""
Mi Asistente de Texto Inteligente

Objetivo:
Permitir al usuario ingresar un texto inicial y aplicar distintas
operaciones de procesamiento de cadenas (string methods) mediante
un menú interactivo, usando estructuras de control (while, if/elif/else).
"""

def mostrar_menu():
    """
    Muestra las opciones disponibles en el menú interactivo.
    """
    print("\n--- Menú de Asistente de Texto ---")
    print("1. Contar caracteres (len())")
    print("2. Reemplazar palabra (replace())")
    print("3. Eliminar espacios al inicio y final (strip())")
    print("4. Dividir texto en palabras (split())")
    print("5. Verificar si una palabra está en el texto (in/not in)")
    print("6. Formatear texto con variables (format())")
    print("7. Salir")
    print("-----------------------------------")

def asistente_de_texto():
    """
    Función principal que ejecuta el bucle del menú interactivo.
    """
    # 1. Solicitar el texto inicial
    texto_base = input("Por favor, ingresa el texto inicial con el que deseas trabajar: ")
    
    # Estructura de repetición (while) para mantener el menú activo
    ejecutando = True
    while ejecutando:
        print(f"\nTu texto actual es: '{texto_base}'")
        mostrar_menu()
        
        opcion = input("Elige una opción (1-7): ")
        
        # Estructura de selección (if/elif/else) para manejar las opciones
        
        # Opción 1: Contar caracteres (len())
        if opcion == '1':
            # len() cuenta todos los caracteres, incluyendo espacios y signos de puntuación
            conteo = len(texto_base)
            print(f"\n Resultado: El texto tiene {conteo} caracteres.")

        # Opción 2: Reemplazar palabra (replace())
        elif opcion == '2':
            palabra_antigua = input("Ingresa la palabra a reemplazar: ")
            palabra_nueva = input("Ingresa la nueva palabra: ")
            
            # El método replace() devuelve una nueva cadena con los cambios.
            nuevo_texto = texto_base.replace(palabra_antigua, palabra_nueva)
            print(f"\n Texto Antiguo: '{texto_base}'")
            print(f" Texto Nuevo:   '{nuevo_texto}'")
            
            # Se pregunta si el usuario quiere actualizar el texto base
            if nuevo_texto != texto_base:
                actualizar = input("¿Deseas usar el texto modificado como el nuevo texto base? (s/n): ")
                if actualizar.lower() == 's':
                    texto_base = nuevo_texto
                    print(" Texto base actualizado.")

        # Opción 3: Eliminar espacios al inicio y final (strip())
        elif opcion == '3':
            # strip() solo elimina los espacios iniciales y finales, no los intermedios
            texto_limpio = texto_base.strip()
            print("\nTexto original (entre comillas para ver los espacios):")
            print(f"'{texto_base}'")
            print("Texto con espacios eliminados (strip()):")
            print(f"'{texto_limpio}'")
            
            # Se pregunta si el usuario quiere actualizar el texto base
            if texto_limpio != texto_base:
                actualizar = input("¿Deseas usar el texto limpio como el nuevo texto base? (s/n): ")
                if actualizar.lower() == 's':
                    texto_base = texto_limpio
                    print(" Texto base actualizado.")
            else:
                print("El texto base no tenía espacios iniciales o finales para eliminar.")

        # Opción 4: Dividir texto en palabras (split())
        elif opcion == '4':
            # split() divide la cadena en una lista de subcadenas usando un separador (por defecto, cualquier espacio)
            lista_palabras = texto_base.split()
            print(f"\n El texto se ha dividido en {len(lista_palabras)} palabras:")
            print(lista_palabras)

        # Opción 5: Verificar si una palabra está en el texto (in/not in)
        elif opcion == '5':
            palabra_a_buscar = input("Ingresa la palabra a verificar: ")
            
            # El operador 'in' verifica la existencia de una subcadena
            if palabra_a_buscar in texto_base:
                # Se utiliza 'not in' solo para el mensaje de negación
                print(f"\n ¡Sí! La palabra '{palabra_a_buscar}' está presente en el texto.")
            else:
                print(f"\n No. La palabra '{palabra_a_buscar}' no está presente en el texto.")


        # Opción 6: Formatear texto con variables (format())
        elif opcion == '6':
            # Ejemplo de formateo de texto usando el método format()
            nombre = input("Ingresa un nombre para el ejemplo: ")
            lugar = input("Ingresa un lugar para el ejemplo: ")
            
            plantilla = "El texto original era: '{}'. Ahora, {} está en {}."
            
            texto_formateado = plantilla.format(texto_base, nombre, lugar)
            print("\n Resultado de Formateo:")
            print(texto_formateado)

        # Opción 7: Salir
        elif opcion == '7':
            print("\n¡Gracias por usar el Asistente de Texto Inteligente! ¡Hasta pronto! ")
            ejecutando = False # Se cambia la condición para salir del bucle while

        # Manejo de opción no válida (estructura else)
        else:
            print("\n Opción no válida. Por favor, elige un número del 1 al 7.")

# --- Ejecución del Programa ---
if __name__ == "__main__":
    asistente_de_texto()