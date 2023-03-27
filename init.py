import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>Hola Mundo - Suscribete !</h1>"
    data ={
        'titulo': 'Index'
    }
    return render_template('index.html',data=data)

get_plot = False

@app.route('/cantidad_facturas_lectura_correcta', methods=['GET', 'POST'])
def cantidad_facturas_lectura_correcta():
	data = pd.read_csv('facturasocr.csv')

# Eliminar espacios adicionales en los nombres de las columnas
	data.columns = data.columns.str.strip()

# Filtrar los datos que tienen "Leer bien" en la columna 'Estado lectura'
	data_filtrada = data[data['Estado lectura'] == 'Leer bien']
# Filtrar los datos que NO tienen "Leer bien" en la columna 'Estado lectura'
	data_filtrada_mal = data[data['Estado lectura'] != 'Leer bien']
	
	plt.figure(figsize=(12, 6))
	plt.bar(data_filtrada['Proveedor'], data_filtrada['Cantidad facturas'])
	plt.xlabel('Proveedor')
	plt.ylabel('Cantidad de facturas')
	plt.xticks(rotation=90)
	plt.title('Cantidad de facturas por proveedor con lectura correcta')
	plt.savefig('static/my_plot.png')
	return render_template('lectura_correcta.html', cantidad_facturas_lectura_correcta = True, plot_url = 'static/my_plot.png', data = data)

@app.route('/cantidad_facturas_lectura_incorrecta', methods=['GET', 'POST'])
def cantidad_facturas_lectura_incorrecta():
	data = pd.read_csv('facturasocr.csv')

# Eliminar espacios adicionales en los nombres de las columnas
	data.columns = data.columns.str.strip()

# Filtrar los datos que tienen "Leer bien" en la columna 'Estado lectura'
	data_filtrada = data[data['Estado lectura'] == 'Leer bien']
# Filtrar los datos que NO tienen "Leer bien" en la columna 'Estado lectura'
	data_filtrada_mal = data[data['Estado lectura'] != 'Leer bien']
	
	plt.figure(figsize=(12, 6))
	plt.bar(data_filtrada_mal['Proveedor'], data_filtrada_mal['Cantidad facturas'], color='red')
	plt.xlabel('Proveedor')
	plt.ylabel('Cantidad de facturas')
	plt.xticks(rotation=90)
	plt.title('Cantidad de facturas por proveedor con lectura incorrecta')
	plt.savefig('static/my_plot.png')
	return render_template('lectura_incorrecta.html', cantidad_facturas_lectura_incorrecta = True, plot_url = 'static/my_plot.png', data = data)

app.secret_key = 'some key that you will never guess'

#Run the app on localhost port 5000
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)


