from flask import Flask, session
from flask import render_template, request, Response, jsonify, redirect, url_for
from flask import render_template_string
import database as dbase 
from usuarios import Usuarios 
from flask_mail import Mail, Message
import secrets
import pprint
import random
from bson.objectid import ObjectId
from jinja2 import *
from flask import Markup
import html5lib


db = dbase.dbConection()

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('Main.html')  #

#Configurar la conexion para enviar el correo
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sistemarecomendador@outlook.com'
app.config['MAIL_PASSWORD'] = '+programaTT951'
app.config['MAIL_STARTTLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

app.secret_key = 'clave_secreta'

def crear_token(email):
    #Se crea un token y se guarda en la collecion del usuario
    db = dbase.dbConection()
    user = db['usuarios']
    token = secrets.token_urlsafe(64)
    user.update_one({'email': email}, {'$set': {'email_token': token}})
    return token

@app.route('/confirmar_correo/<token>')
def confirmar_correo(token):
    db = dbase.dbConection()
    user = db['usuarios']
    user.update_one({'email_token': token}, {"$set": {'email_confirmed':True}})
    user.update_one({'email_token': token}, {'$unset': {'email_token': ""}})
    return "Tu correo electrónico ha sido confirmado con éxito"

def enviar_confirmacion(email, token):
    msg = Message('Confirma tu dirección de correo electrónico',sender="sistemarecomendador@outlook.com", recipients=[email])
    msg.body = f'Haz clic en el siguiente enlace para confirmar tu dirección de correo electrónico: {url_for("confirmar_correo", token=token, _external=True)}'
    mail.send(msg)

#Resgistro de un nuevo usuario
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
        return redirect(url_for('registro', error='El correo electrónico ya está registrado en la base de datos'))

    if user is not None and name is not None and last_nameP is not None and last_nameM is not None and password is not None:
        newUser = Usuarios(name, last_nameP, last_nameM, email, password)

        # Generar un token para la dirección de correo electrónico del usuario
        email_token = crear_token(email)

        # Enviar el correo electrónico de confirmación al usuario
        enviar_confirmacion(email, email_token)

        # Agregar el token y el estado de la dirección de correo electrónico a la base de datos
        newUser.email_token = email_token
        newUser.email_confirmed = False
        user.insert_one(newUser.__dict__)

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
    error = request.args.get('error')
    return render_template('Registro.html', error=error)

@app.route('/noticia/<noticia_id>')
def ver_noticia(noticia_id):
    db = dbase.dbConection()
    notas = db['noticias']

    # Utiliza el ID de la noticia para obtener la información de la noticia desde MongoDB
    noticia = notas.find_one({'_id': ObjectId(noticia_id)})
    # Escapa el contenido para evitar que se muestren las etiquetas HTML
    
    # Renderiza la plantilla de la noticia con la información obtenida
    return render_template('Noticia.html', noticia=noticia, Contenido=Markup(noticia['Contenido']))


@app.route('/noticia/<noticia_id>/guardar_reaccion', methods=['POST'])
def guardar_reaccion(noticia_id):
    db = dbase.dbConection()
    clasificados = db['noticias_clasificadas']
    # Obtener el user_id desde la variable de sesión
    user_id = session.get('user_id')
    # Obtener el valor de la reacción desde la solicitud POST
    reaction = request.json['reaction']
    # Guardar la noticia clasificada en la colección de noticias clasificadas
    clasificados.insert_one({
        'noticia_id': ObjectId(noticia_id),
        'reaccion': reaction,
        'usuario_id': user_id
    })
    # Devolver una respuesta con el código de estado HTTP 200 (OK)
    return '', 200


#Cards Noticias
@app.route('/FeelNews', methods=['GET'])
def noticias():
    db = dbase.dbConection()
    collection = db['noticias']
    secciones = ['cdmx', 'deportes', 'mundo'] # Secciones a las que se quiere obtener noticias
    noticias = []
    for seccion in secciones:
        noticias_seccion = list(collection.aggregate([
            {"$match": {"Seccion": seccion}}, # Filtrar por sección
            {"$sample": {"size": 4}} # Obtener 3 documentos al azar de cada sección
        ]))
        noticias += noticias_seccion
    if not noticias:
        print("No se encontraron noticias en la base de datos")
        return render_template('FeelNews.html', noticias=[])
    noticias_encabezado = random.sample(noticias, 6)
    return render_template('FeelNews.html', noticias=noticias ,noticias_encabezado=noticias_encabezado)

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
    elif user_data['email_confirmed'] is False:
        #revisar si en la base de datos el correo ya ha sido verificado
        return "El correo no ha sido verificado."
    else:
        session['user_id'] = str(user_data['_id'])
        return redirect(url_for('noticias'))
    





if __name__ == '__main__':
    app.run(host='0.0.0.0')



@app.route('/Calendario')
def registro():
    return render_template('Calendario.html')


