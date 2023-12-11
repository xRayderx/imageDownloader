from flask import Flask, request, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup
import os
import shutil
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/descargar', methods=['POST'])

def descargar():
    url = request.json['url']

    pattern = re.compile(r"^https?://[^\s/$.?#].[^\s]*$")
    if not pattern.match(url):
        return jsonify({ "error": "La URL no es válida" })
    
    try:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        imagenes = soup.find_all('img')
        #folder = 'imagenes'
        folder = os.path.join('.', 'imagenes')

        os.makedirs(folder, exist_ok=True)
        lista = []

        for imagen in imagenes:
            src = imagen['src']

            if src.startswith('http'):
                img_url = src
            else:
                img_url = url + src

            img = requests.get(img_url, stream = True)
            name = img_url.split('/')[-1]
            path = os.path.join(folder, name)

            with open(path, 'wb') as f:
                shutil.copyfileobj(img.raw, f)
        
            lista.append(path)
        
        if lista:
            return jsonify(lista)
        else:
            return jsonify({ "error": "La URL no contiene imágenes" })
        
    except requests.exceptions.RequestException as e:
        print(e)
        return jsonify({ "error": "No se pudo acceder a la URL" })
    except Exception as e:
        print(e)
        return jsonify({ "error": "Ocurrió un error al descargar las imagenes" })

@app.route('/<path:filename>')
def serve_images(filename):
    return send_from_directory('imagenes', filename)

if __name__ == '__main__':
    app.run(debug=True)