import os

current_dir = os.path.dirname(__file__)
db_filename = 'database/daoctor.sqlite3'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(current_dir, db_filename)}'

# SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:mysql2021@localhost:3306/tt'
# SQLALCHEMY_DATABASE_URI='sqlite:///./database/daoctor.sqlite3'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///D:/Python/plant_disease/crop-pest-control-system-based-on-image-recognition-develop/daoctor/database/daoctor.sqlite3'
SECRET_KEY = "random string"
SQLALCHEMY_TRACK_MODIFICATIONS=True