"""
创建时间 : 2018/06/17
版本号 : V1
文档名 : helper.py
编辑人 : he_wm
作 用 : 处理数据库请求【开启数据库连接池】
源存储位置 : css_v1\\css_v1\\utils\\helper.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
import pymysql
from config import Manage


def connect():
    """
    链接数据库函数
    :return:
    """
    conn = Manage.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


def connect_close(conn, cursor):
    """
    关闭数据库函数
    :param conn:
    :param cursor:
    :return:
    """
    cursor.close()
    conn.close()


def fetch_one(sql, arg):
    """
    查询单条数据
    :param sql: sql语句
    :param arg: 条件
    :return:
    """
    conn, cursor = connect()
    cursor.execute(sql, arg)
    result = cursor.fetchone()
    connect_close(conn, cursor)
    return result


def fetch_all(sql, arg):
    """
    查询所有数据
    :param sql: sql语句
    :param arg: 条件
    :return:
    """
    conn, cursor = connect()
    cursor.execute(sql, arg)
    result_list = cursor.fetchall()
    connect_close(conn, cursor)
    return result_list


def insert(sql, arg):
    """
    向数据库插入数据函数
    :param sql: sql语句
    :param arg: 条件
    :return:
    """
    conn, cursor = connect()
    row = cursor.execute(sql, arg)
    conn.commit()
    connect_close(conn, cursor)
    return row
