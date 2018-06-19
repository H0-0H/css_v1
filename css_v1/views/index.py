"""
创建时间 : 2018/06/17
版本号 : V1
文档名 : account.py
编辑人 : he_wm
作 用 : 用户上传代码处理相关
源存储位置 : css_v1\\css_v1\\views\\account.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
import os
import json
import uuid
import shutil
import datetime
from flask import Blueprint, render_template, request, redirect, session
from werkzeug.utils import secure_filename

from css_v1.utils import helper

ind = Blueprint('ind', __name__)


# 通用检查是否登录
@ind.before_request
def inner():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return None


# @ind.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         sql = 'select * from code'
#         helper.Manage
#         cursor.execute(sql)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         result = cursor.fetchall()
#         print(result)
#         return render_template('index.html', **{'result_list': result})


@ind.route('/detail/<int:nid>')
def detail(nid):
    """
    代码上传个人详情页
    :param nid: 与用户关联的user_id
    :return:
    """
    if request.method == 'GET':
        sql = 'select id,line,ctime from code WHERE user_id=%s'
        result_list = helper.fetch_all(sql, [nid])
        print(result_list)
        lis_time = []
        lis_lin = []
        for item in result_list:
            lis_time.append(str(item['ctime']))
            lis_lin.append(int(item['line']))
        lis_time = json.dumps(lis_time)
        lis_lin = json.dumps(lis_lin)
        return render_template('detail.html', **{'result_list': result_list, "lis_time": lis_time, "lis_lin": lis_lin})


@ind.route('/upload', methods=['GET', 'POST'])
def uplosd():
    """
    上传代码函数
    :return:
    """
    if request.method == 'GET':
        return render_template("upload.html")
    # 接收用户上传的文件
    file = request.files.get('file')
    path, ext = file.filename.rsplit('.', maxsplit=1)
    # 检查是否是.zip压缩的文件
    if ext != 'zip':
        return '仅支持上传.zip格式文件'
    # 存储到本地
    uplosd_path = os.path.join('funk.config.root_path', 'files', str(uuid.uuid4()))
    # 解压文件
    shutil._unpack_zipfile(file.stream, uplosd_path)

    total_num = 0
    """
    dirpath:当前所处位置路径
    dirnames:当前所处位置有那几个文件夹
    filenames:当前所处位置有哪些文件
    """
    for (dirpath, dirnames, filenames) in os.walk(uplosd_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_path_ext = file_path.rsplit('.', maxsplit=1)
            # 仅计算.py文件的行数
            if len(file_path_ext) != 2:
                continue
            if file_path_ext[1] != 'py':
                continue

            line_num = 0
            with open(file_path, mode='rb') as f:
                for line in f:
                    if line.strip().startswith(b'#'):
                        continue
                    line_num += 1
                total_num += line_num
    ctime = datetime.date.today()
    sql = 'select id from code WHERE ctime=%s and user_id = %s'
    ret = helper.fetch_one(sql, (ctime, session['user_info']['id']))
    if ret:
        return "今日已经上传"
    sql = 'insert into code(line, ctime,user_id) VALUES (%s,%s,%s)'
    helper.insert(sql, (total_num, ctime, session['user_info']['id']))


@ind.route('/user_list')
def user_list():
    """
    所有用户上传代码详情主页
    :return:
    """
    sql = 'SELECT id,user,nick from username'
    data_list = helper.fetch_all(sql, [])
    sql1 = 'SELECT user,SUM(line) FROM code INNER JOIN username ON username.id = code.user_id GROUP BY user_id'
    data_list1 = helper.fetch_all(sql1, [])
    print(data_list1)
    lis_lin = []
    for item in data_list1:
        data = []
        data.append(str(item['user']))
        data.append(int(item['SUM(line)']))
        lis_lin.append(data)
    lis_lin = json.dumps(lis_lin)
    print(lis_lin)
    return render_template('user_list.html', data_list=data_list, lis_lin=lis_lin)
