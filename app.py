from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')

def home():
    x = requests.get('https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt')
    numeros = ('3','4','5','7')
    texto = x.text.splitlines()
    lineas = list(filter(lambda x: x.startswith(numeros), texto))

    html = """
    <style>
        table { border-collapse: collapse; margin: 20px auto; font-family: Arial; }
        th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }
    </style>
    <table>
        <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Pais</th>
            <th>Direccion</th>
        </tr>
    """
    for linea in lineas:
        columnas = linea.split('|')  
        html += "<tr>"
        for i in columnas:
            html += f"<td>{i}</td>"
        html += "</tr>"

    html += "</table>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)