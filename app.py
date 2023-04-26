from flask import Flask
from flask import render_template, request, Response, jsonify, redirect, url_for
from flask import request
import os
from forms import RegistroForm
import database as dbase 
from usuarios import Usuarios 

db = dbase.dbConection()

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def home():
    return render_template('InicioSesion.html')  #


#Metodo POST
@app.route('/registrosesion', methods=['GET','POST'])
def addUser():
    #Crear la colecion 
    db = dbase.dbConection()
    user = db['usuarios']

    form = RegistroForm()
    if request.method == 'POST' and form.validate_on_submit() and 'submit' in request.form:
        form.nombre.data = request.form['nombre']
        form.apellidoP.data = request.form['apellidoP']
        form.apellidoM.data = request.form['apellidoM']
        form.correo.data = request.form['correo']
        form.contraseña.data = request.form['contraseña']
        #confirmar contraseña->>>>>>>
        form.confirmar_contraseña.data = request.form['confirmar_contraseña']

        if form.contraseña.data != form.confirmar_contraseña.data:
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('addUser'))
        #hola
         # Verificar si el correo electrónico ya está en la base de datos
        existing_user = user.find_one({'email': email})
        if existing_user is not None:
         return 'El correo electrónico ya está registrado en la base de datos'
        form.confirmar_contraseña.data = request.form['confirmarcontraseña']
        #form.submit.data=request.form['submit_button']
        # El formulario es válido
        # Procesar los datos del formulario aquí
        
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
            return redirect(url_for('inicio'))
        else:
                return notFound()
        
    return render_template('Registro.html', form=form)







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



@app.route('/Noticia')
def entrar():
    return render_template('FeelNews.html')


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
        return render_template('Noticia.html')
    
#Funcion para inicio y validaciones de las inputs



@app.route('/registro-exitoso')
def registro_exitoso():
    return '¡Registro exitoso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')



