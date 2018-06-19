"""
创建时间 : 2018/06/17
版本号 : V1
文档名 : md5.py
编辑人 : he_wm
作 用 : 加密用户密码
源存储位置 : \\css_v1\\css_v1\\utils\\md5.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
import hashlib
from config import Manage


def md5(arg):
    """
    加密密码函数
    :param arg:
    :return:
    """
    hash = hashlib.md5(Manage.SALT)
    hash.update(bytes(arg, encoding='utf-8'))
    ret = hash.hexdigest()
    return ret


    # 明文 admin1234
    # 密文 2435d800b38fcca0bf1a6b372def128a
    # 明文 li1234
    # 密文 3661852d43fdb1dac44c66435af92e55
