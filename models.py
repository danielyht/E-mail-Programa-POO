from peewee import *
from datetime import datetime

db = SqliteDatabase("email_system.db")

class BaseModel(Model):
    class Meta:
        database = db

class Remetente(BaseModel):
    nome = CharField()
    emailAddress = CharField()

class Destinatario(BaseModel):
    nome = CharField()
    emailAddress = CharField()

class Email(BaseModel):
    titulo = CharField()
    corpo = TextField()
    dataEnvio = DateTimeField(default=datetime.now)
    remetente = ForeignKeyField(Remetente, backref="emails")

class EmailDestinatario(BaseModel):
    email = ForeignKeyField(Email, backref="destinatarios")
    destinatario = ForeignKeyField(Destinatario, backref="emails")

db.connect()
db.create_tables([Remetente, Destinatario, Email, EmailDestinatario])
