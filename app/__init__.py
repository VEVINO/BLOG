from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inițializează aplicația Flask
app = Flask(__name__)

# Configurație pentru Flask și SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inițializează SQLAlchemy cu aplicația Flask
db = SQLAlchemy(app)

# Aici poți importa modelele și rutele după ce ai inițializat 'db'
from . import models, routes

# Asigură-te că rutele sunt accesibile
# app.register_blueprint(routes.main)

# Acum ai o aplicație Flask simplă, cu suport pentru o bază de date.

# adugare migrari pentru baze de date
migrate = Migrate(app, db)

# folosim (flask db init) in Terminal pentru creare director migrations(se creaza migrations>done)
# pentru aducere articol nou folosim : flask db migrate -m "Descriere migrație"
# flask db upgrade

# pip install flask flask_sqlalchemy flask_migrate
# typed in Terminal : flask --main run >>>> Running on http://127.0.0.1:5000
# daca error 404 apare in pagina pls use http://127.0.0.1:5000/home
