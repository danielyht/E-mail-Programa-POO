from peewee import *
from datetime import datetime

# cria o banco de dados sqlite com o nome email_system.db
db = SqliteDatabase("email_system.db")

# classe base para os modelos usarem o mesmo banco
class BaseModel(Model):
    class Meta:
        database = db

# tabela para armazenar os remetentes
class Remetente(BaseModel):
    nome = CharField()              # nome do remetente
    emailAddress = CharField()      # email do remetente

# tabela para armazenar os destinatários
class Destinatario(BaseModel):
    nome = CharField()              # nome do destinatário
    emailAddress = CharField()      # email do destinatário

# tabela para armazenar os emails enviados
class Email(BaseModel):
    titulo = CharField()                          # título do email
    corpo = TextField()                           # corpo do email
    dataEnvio = DateTimeField(default=datetime.now)  # data e hora de envio
    remetente = ForeignKeyField(Remetente, backref="emails")  # quem enviou

# tabela para relacionar email com vários destinatários
class EmailDestinatario(BaseModel):
    email = ForeignKeyField(Email, backref="destinatarios")             # email enviado
    destinatario = ForeignKeyField(Destinatario, backref="emails")      # quem recebeu

# conecta com o banco de dados
db.connect()

# cria as tabelas se ainda não existirem
db.create_tables([Remetente, Destinatario, Email, EmailDestinatario])
from peewee import *
from datetime import datetime

# cria o banco de dados sqlite com o nome email_system.db
db = SqliteDatabase("email_system.db")

# classe base para os modelos usarem o mesmo banco
class BaseModel(Model):
    class Meta:
        database = db

# tabela para armazenar os remetentes
class Remetente(BaseModel):
    nome = CharField()              # nome do remetente
    emailAddress = CharField()      # email do remetente

# tabela para armazenar os destinatários
class Destinatario(BaseModel):
    nome = CharField()              # nome do destinatário
    emailAddress = CharField()      # email do destinatário

# tabela para armazenar os emails enviados
class Email(BaseModel):
    titulo = CharField()                          # título do email
    corpo = TextField()                           # corpo do email
    dataEnvio = DateTimeField(default=datetime.now)  # data e hora de envio
    remetente = ForeignKeyField(Remetente, backref="emails")  # quem enviou

# tabela para relacionar email com vários destinatários
class EmailDestinatario(BaseModel):
    email = ForeignKeyField(Email, backref="destinatarios")             # email enviado
    destinatario = ForeignKeyField(Destinatario, backref="emails")      # quem recebeu

# conecta com o banco de dados
db.connect()

# cria as tabelas se ainda não existirem
db.create_tables([Remetente, Destinatario, Email, EmailDestinatario])
