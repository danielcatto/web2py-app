#coding: utf-8

#criar objeto de configuração com storage

#import sys
#sys.path.insert(0, r"/home/daniel/Projetos/web2py/web2py-app/web2py")

from gluon.storage import Storage
config = Storage(
    db=Storage(),
    mail=Storage(),
    auth=Storage()
)
# definir settings para db, auth, mail

config.db.uri = "sqlite://ecommerce.db"
config.db.pool_size=0 
config.db.check_reserved=["all"]
config.db.migrate_enabled=True #desliga em produção

config.mail.sender = "ecommerce@ecommerce.com"
config.mail.server = "logging" #mudar para smpt:
config.mail.login = "usuario:senha"

