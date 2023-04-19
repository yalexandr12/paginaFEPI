class Usuarios:
    def __init__(self, name, last_nameP, last_nameM, email, password):

        self.name = name
        self.last_nameP = last_nameP
        self.last_nameM = last_nameM
        self.email = email
        self.password = password

    def collectionUser(self):
        return{
            'nombre': self.name,
            'apellidoP': self.last_nameP,
            'apellidoM': self.last_nameM,
            'correo': self.email,
            'contraseña': self.password 
        }