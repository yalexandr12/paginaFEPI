from flask import Flask
from flask import render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from usuarios import Usuarios 

db = dbase.dbConection()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Main.html')

#Metodo POST
@app.route('/login', methods=['POST'])
def addUser():
    #Crear la colecion 
    db = dbase.dbConection()
    user = db['usuarios']
    name = request.form['nombre']
    last_nameP = request.form['apellidoP']
    last_nameM = request.form['apellidoM']
    email = request.form['correo']
    pasword = request.form['contraseña']

    if user is not None and name is not None and last_nameP is not None and last_nameM is not None and pasword is not None:
        newUser = Usuarios(name, last_nameP, last_nameM, email, pasword)
        user.insert_one(newUser.__dict__)
        response = jsonify({
            'name' : name,
            'last_nameP' : last_nameP,
            'last_nameM' : last_nameM,
            'email' : email,
            'pasword' : pasword
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Funcion para alertar que una pagina no se ha encontrado    
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message' : 'No encontrado' + request.url,
        'status' : '404 Not Found'
    }
    return jsonify(message)

@app.route('/Inicio_sesion')
def inicio_sesion():
    return render_template('InicioSesion.html')

@app.route('/Registro')
def registro():
    return render_template('Registro.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')



