# -*- coding: utf-8 -*-


class Config(object):
    SECRET_KEY = 'some secret words'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql://suntangji:hehe@suntangji.me/occup2'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
