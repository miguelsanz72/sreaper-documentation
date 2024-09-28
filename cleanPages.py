import os
from bs4 import BeautifulSoup

def limpiar_texto():
    carpeta_paginas = 'paginas'
    carpeta_texto_limpio = 'texto_limpio'

    # Crear la carpeta 'texto_limpio' si no existe
    if not os.path.exists(carpeta_texto_limpio):
        os.makedirs(carpeta_texto_limpio)

    # Recorrer todos los archivos en la carpeta 'paginas'
    for nombre_archivo in os.listdir(carpeta_paginas):
        # Verificar que el archivo termine con '.txt' y no contenga '.png' en el nombre
        if nombre_archivo.endswith('.txt') and '.png' not in nombre_archivo and '.svg' not in nombre_archivo:
            ruta_archivo = os.path.join(carpeta_paginas, nombre_archivo)

            # Leer el contenido del archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido_html = archivo.read()

            # Utilizar BeautifulSoup para eliminar el código HTML y CSS
            soup = BeautifulSoup(contenido_html, 'html.parser')
            texto_limpio = soup.get_text(separator='\n', strip=True)

            # Guardar el texto limpio en un nuevo archivo en 'texto_limpio'
            ruta_archivo_limpio = os.path.join(carpeta_texto_limpio, nombre_archivo)
            with open(ruta_archivo_limpio, 'w', encoding='utf-8') as archivo_limpio:
                archivo_limpio.write(texto_limpio)

            print(f"Archivo procesado: {nombre_archivo}")
        else:
            print(f"Archivo omitido: {nombre_archivo}")

if __name__ == '__main__':
    limpiar_texto()
