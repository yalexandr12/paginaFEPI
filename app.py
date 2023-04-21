from flask import Flask
from flask import render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from usuarios import Usuarios 

db = dbase.dbConection()

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('InicioSesion.html')  #


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
    password = request.form['contraseña']

    # Verificar si el correo electrónico ya está en la base de datos
    existing_user = user.find_one({'email': email})
    if existing_user is not None:
        return 'El correo electrónico ya está registrado en la base de datos'


    if user is not None and name is not None and last_nameP is not None and last_nameM is not None and password is not None:
        newUser = Usuarios(name, last_nameP, last_nameM, email, password)
        user.insert_one(newUser.__dict__)
        response = jsonify({
            'name' : name,
            'last_nameP' : last_nameP,
            'last_nameM' : last_nameM,
            'email' : email,
            'password' : password
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Funcion para alertar que una pagina no se ha encontrado    
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message' : 'No encontrado ' + request.url,
        'status' : '404 Not Found'
    }
    return jsonify(message)


@app.route('/Inicio_sesion')
def inicio():
    return render_template('InicioSesion.html')

@app.route('/Registro')
def registro():
    return render_template('Registro.html')

@app.route('/Noticia')
def entrar():
    return render_template('Noticia.html')


#Funcion para iniciar sesion y verificar que el usuario se encuentre en la bd
@app.route('/Iniciar_sesion', methods=['GET'])
def validate_user():
    #Se mandan a llamar los parametros a validar, en la collecion usuarios
    email = request.args.get('email')
    password = request.args.get('password')
    user = db['usuarios']
    #Verificar que el usuario y la contraseñan correspondan al usuario
    user_data = user.find_one({"email": email, "password": password})
    if user_data is None:
        return "El usuario o contraseña son incorrectos."
    else:
        return render_template('FeelNews.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')



@app.route('/Calendario')
def registro():
    return render_template('Calendario.html')