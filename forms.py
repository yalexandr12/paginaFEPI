from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length,Regexp,EqualTo
from email_validator import validate_email
import re


class RegistroForm(FlaskForm):
    nombre = StringField('Nombre(s)', validators=[DataRequired(),
    Regexp('^[A-Za-z]{2,10}$', message='El nombre debe contener solo letras y tener entre 2 y 10 caracteres')  
    ])
    apellidoP = StringField('Apellido Paterno', validators=[DataRequired(),
    Regexp('^[A-Za-z]{2,10}$', message='El Apellido paterno debe contener solo letras y tener entre 2 y 10 caracteres')
    ])
    apellidoM = StringField('Apellido Materno', validators=[DataRequired(),
    Regexp('^[A-Za-z]{2,10}$', message='El Apellido paterno debe contener solo letras y tener entre 2 y 10 caracteres')
    ])
    correo = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8),
    Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\W).+$', message='La contraseña debe tener al menos una letra en mayúscula, una letra en minúscula y un carácter especial')
    ])
    #Confirmar contraseña
    confirmar_contraseña = PasswordField('Confirmar Contraseña', validators=[DataRequired(message='Confirme Contra, Equseña')])
