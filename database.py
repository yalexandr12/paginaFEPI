from pymongo import MongoClient
import certifi

mongo_URI = 'mongodb+srv://Sistema_recomendador:sistemaRecomendador@cluster0.dzdudgs.mongodb.net/?retryWrites=true&w=majority'


ca = certifi.where()

#Funcion para conectar a la base de datos
def dbConection():
    try:
        client = MongoClient(mongo_URI, tlsCAFile=ca)
        db = client["sistema_recomendador"]

        return db
    except ConnectionError:
        print("Error en la coneccion")