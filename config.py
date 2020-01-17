# -*- coding=utf-8 -*-
import os
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@192.168.0.107:3306/flask_config'
    DEBUG = True

# define the config
config = {
    'default': DevelopmentConfig
}
