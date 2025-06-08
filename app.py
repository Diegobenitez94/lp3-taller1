"""
Archivo principal de la aplicación Flask
"""
import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from models import db
from resources.video import Video
from config import config

def create_app(config_name='default'):
    """
    Función factory para crear la aplicación Flask
    
    Args:
        config_name (str): Nombre de la configuración a utilizar
        
    Returns:
        Flask: Aplicación Flask configurada
    """
    
   
    # TODO : Crear el objeto 'app'
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    # Inicializar extensiones
    db.init_app(app)
    migrate = Migrate(app, db)
    
    api = Api(app)
    
    # Registrar rutas
    api.add_resource(Video, "/api/videos/<int:video_id>")
    
    return app

if __name__ == "__main__":
    # Obtener configuración del entorno o usar 'development' por defecto
    config_name = os.getenv('FLASK_CONFIG', 'development')
    
    # Crear aplicación
    app = create_app(config_name)
    
    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()
    
    # Ejecutar servidor
app.run(host='0.0.0.0', port=5000)
api = Api(app)


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    
    app.run(debug=True)

  