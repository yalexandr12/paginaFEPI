class Usuarios:
    def __init__(self, name, last_name, username, email, pasword):

        self.name = name
        self.last_name = last_name
        self.username =  username
        self.email = email
        self.pasword = pasword

    def collectionUser(self):
        return{
            'nombre': self.name,
            'apellidos': self.last_name,
            'nombre_usuario': self.username,
            'correo': self.email,
            'contraseña': self.pasword
        }