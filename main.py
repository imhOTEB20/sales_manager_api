from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Configuración de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@localhost/salesmanager_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos y Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    contraseña = db.Column(db.Text, nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    creado_en = db.Column(db.DateTime, default=db.func.current_timestamp())

# Esquema de Usuario
class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

# Crear las tablas
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
