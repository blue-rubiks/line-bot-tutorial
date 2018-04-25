from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['postgresql']['URI']

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class UrlData(db.Model):
    __tablename__ = 'UrlData'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))

    def __init__(self, url):
        self.url = url


if __name__ == '__main__':
    manager.run()
