class Usuarios:
    def __init__(self, name, last_nameP, last_nameM, username, email, pasword):

        self.name = name
        self.last_nameP = last_nameP
        self.last_nameM = last_nameM
        self.username =  username
        self.email = email
        self.pasword = pasword

    def collectionUser(self):
        return{
            'nombre': self.name,
            'apellidoP': self.last_nameP,
            'apellidoM': self.last_nameM,
            'nombre_usuario': self.username,
            'correo': self.email,
            'contraseña': self.pasword
        }