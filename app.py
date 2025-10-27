#Librerías
from flask import Flask

#Instancia de la app
app = Flask(__name__)

#Ruta Principal
@app.route('/')
def home():
    return "Hola"

#Ejecución de la app
if __name__ == '__main__':
    app.run(debug=True) #Para ver errores en tiempo real 