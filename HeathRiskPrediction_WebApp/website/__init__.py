from flask import Flask
from flask_mail import Mail
import os, random

mail = Mail()

def create_app():
    app = Flask(__name__)
    random.seed(0)
    app.config['SECRET_KEY'] = os.urandom(24)

    # Mail Configuration (Gmail)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'mr3097633@gmail.com'
    app.config['MAIL_PASSWORD'] = 'jpjiglecxcpitegs'

    mail.init_app(app)

    from .views import views
    from .prediction import prediction
    from .messages import messages

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(prediction, url_prefix='/')
    app.register_blueprint(messages, url_prefix='/')

    return app
