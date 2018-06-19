"""
创建时间 : 
版本号 : V
文档名 : 
编辑人 : he_wm
作 用 : 
源存储位置 : 
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""

from flask import Flask
from .views.account import account
from .views.index import ind


def create_app():
    app = Flask(__name__)
    app.register_blueprint(account)
    app.register_blueprint(ind)
    return app
