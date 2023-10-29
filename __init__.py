from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")
print('__init__.py 配置后',app.config)
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()








