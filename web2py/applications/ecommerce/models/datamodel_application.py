#coding: utf-8
#definir objetos de app (Auth, Mail, Service)

from gluon.tools import Auth, Mail

auth = Auth(db, hmac_key=Auth.get_or_create_key() )

# auth.settings.registration_requires_verification = False
# auth.settings.registration_requires_approvval = False
# auth.settings.reset_password_requires_verification = False

mail = Mail()
#configuração vem de appsettings
mail.settings.sender = config.mail.sender
mail.settings.server = config.mail.server
mail.settings.login = config.mail.login


auth.settings.mailer = mail

#aut.setting.login_field = 'cpf'.  
auth.define_tables() # ou auth.define_tables(username=True)
