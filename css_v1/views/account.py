"""
创建时间 : 2018/06/17
版本号 : V1.1
文档名 : account.py
编辑人 : he_wm
作 用 : 用户相关
源存储位置 : css_v1\\css_v1\\views\\account.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
from flask import Blueprint, render_template, request, redirect, session
from css_v1.utils.md5 import md5
from css_v1.utils import helper

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    """
    登陆函数
    :return:
    """
    if request.method == 'GET':
        return render_template('login.html')
    # 获取前端返回的用户名与密码
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    pwd_md5 = md5(pwd)
    # 数据库校验
    sql = 'select id,nick from username where user=%s and pwd=%s'
    data = helper.fetch_one(sql, [user, pwd_md5])
    print(data)
    if not data:
        return render_template('login.html', error='用户名或密码错误')
    session['user_info'] = {'id': data['id'], 'nick': data['nick']}
    return redirect('/user_list')


@account.route('/logout')
def logout():
    """
    注销登陆函数
    :return:
    """
    if "user_info" in session:
        del session['user_info']
    return redirect('/login')
