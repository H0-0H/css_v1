"""
创建时间 : 2018/06/17
版本号 : V1
文档名 : manage.py
编辑人 : he_wm
作 用 : flask启动文件
源存储位置 : \\css_v1\\manage.py
修改及增加功能记录 :
"""

from flask_session import Session

from css_v1 import create_app

app = create_app()
# 引入配置文件
app.config.from_object("config.Manage")
Session(app)

if __name__ == '__main__':
    app.run()
