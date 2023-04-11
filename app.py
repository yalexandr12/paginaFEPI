from flask import Flask
from flask import render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from usuarios import Usuarios 

db = dbase.dbConection()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#Metodo POST
@app.route('/login', methods=['POST'])
def addUser():
    #Crear la colecion 
    user = db['usuarios']
    name = request.form['nombre']
    last_name = request.form['apellidos']
    username = request.form['nombre_usuario']
    email = request.form['correo']
    pasword = request.form['contraseña']

    if user and name and last_name and username and pasword:
        newUser = Usuarios[name, last_name, username, email, pasword]
        user.insert_one(newUser.collectionUser())
        response = jsonify({
            'name' : name,
            'last_name' : last_name,
            'username' : username, 
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
    return Response


if __name__ == '__main__':
    app.run(host='0.0.0.0')



