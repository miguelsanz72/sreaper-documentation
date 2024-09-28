import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

def scrape_website(start_url):
    visited = set()
    to_visit = [start_url]
    base_domain = urlparse(start_url).netloc

    # Crear la carpeta 'paginas' si no existe
    if not os.path.exists('paginas'):
        os.makedirs('paginas')

    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)

        try:
            response = requests.get(url)
            content = response.text

            # Analizar el HTML
            soup = BeautifulSoup(content, 'html.parser')

            # Extraer y encolar nuevos enlaces
            for link in soup.find_all('a', href=True):
                href = link['href']
                # Resolver URLs relativas
                full_url = urljoin(url, href)
                # Solo visitar enlaces dentro del mismo dominio
                if urlparse(full_url).netloc == base_domain and full_url not in visited:
                    to_visit.append(full_url)

            # Guardar el contenido en un archivo
            # Crear un nombre de archivo válido
            path = urlparse(url).path
            if path == '' or path == '/':
                filename = 'inicio'
            else:
                filename = path.strip('/').replace('/', '_')
            filename = filename if filename else 'pagina'
            filename = f"{filename}.txt"
            filepath = os.path.join('paginas', filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Guardado {url} en {filepath}")

        except Exception as e:
            print(f"No se pudo acceder a {url}: {e}")

if __name__ == "__main__":
    start_url = input("Ingresa la URL inicial: ")
    scrape_website(start_url)
