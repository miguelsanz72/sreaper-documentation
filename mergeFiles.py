import os

def unir_archivos():
    carpeta_texto_limpio = 'texto_limpio'
    archivo_salida = 'texto_completo.txt'

    # Abrir el archivo de salida en modo escritura
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        # Recorrer todos los archivos en la carpeta 'texto_limpio'
        for nombre_archivo in sorted(os.listdir(carpeta_texto_limpio)):
            if nombre_archivo.endswith('.txt'):
                ruta_archivo = os.path.join(carpeta_texto_limpio, nombre_archivo)

                # Leer el contenido del archivo limpio
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()

                # Escribir el contenido en el archivo de salida
                salida.write(f"--- Contenido de {nombre_archivo} ---\n")
                salida.write(contenido)
                salida.write("\n\n")  # Añadir dos saltos de línea entre archivos

                print(f"Archivo añadido: {nombre_archivo}")

    print(f"\nTodos los archivos han sido unidos en '{archivo_salida}'")

if __name__ == '__main__':
    unir_archivos()
