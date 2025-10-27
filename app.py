#Librerías
from flask import Flask, render_template

#Instancia de la app
app = Flask(__name__)

#Ruta Principal
@app.route('/')
def index():
    return render_template("index.html")

#Ejecución de la app
if __name__ == '__main__':
    app.run(debug=True) #Para ver errores en tiempo real 