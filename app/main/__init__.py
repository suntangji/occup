# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
# app.config.from_pyfile('../config.py')
app.config.from_object('config.Config')


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

