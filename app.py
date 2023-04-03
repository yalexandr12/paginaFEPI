from flask import Flask
from pymongo import MongoClient
from flask import render_template
import csv
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def home():
    client = MongoClient('mongo', 27017)
    db = client.mydatabase
    collection = db.mycollection
    collection.insert_one({'name': 'John'})

    # se crea la colección
    db.create_collection('noticias')

    #Cargar los datos a la coleccion
    with open('noticias_jornada.csv', 'r') as f:
        reader = csv.DictReader(f)
        noticias = [dict(row) for row in reader]
        db.noticias.insert_many(noticias)

    #se crea la colección de emociones
    db.create_collection('emociones')
    # se agregan los documentos de emociones
    emociones = [
        {"_id": ObjectId("6158f9a60c6a2f6a3c937d3c"), "tipo": "Neutro"},
        {"_id": ObjectId("6158f9d40c6a2f6a3c937d3d"), "tipo": "Tristeza"},
        {"_id": ObjectId("6158f9f80c6a2f6a3c937d3e"), "tipo": "Enojo"},
        {"_id": ObjectId("6158fa200c6a2f6a3c937d3f"), "tipo": "Miedo"},
        {"_id": ObjectId("6158fa440c6a2f6a3c937d40"), "tipo": "Sorpresa"}
    ]
    db.emociones.insert_many(emociones)

    db.create_collection('noticias_clasificadas')

    #Se crea la coleccion de usuarios
    db.create_collection('usuarios')

    #  Agregar un usuario
    db.usuarios.insert_one({
    "username": "yael",
    "password": "123",
    "email": "yalexandr12@gmail.com",
    "emotion": ObjectId("6158f9a60c6a2f6a3c937d3c")  # Esta haciendo referencia a neutro
})




    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')



