"""
创建时间 : 2018/06/17
版本号 : V1
文档名 : config.py
编辑人 : he_wm
作 用 : 自定义用户配置
源存储位置 : \\css_v1\\config.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
import redis
import pymysql
from DBUtils.PooledDB import PooledDB, SharedDBConnection


class Manage():
    """
    自定义配置类
    """
    SALT = b"sasa"  # md5盐配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.Redis(host='192.168.131.129', port=6379, password='123456')
    SECRET_KEY = "123fsdsafdadf"
    MAX_CONTENT_LENGTH = 1024 * 1024 * 7
    POOL = PooledDB(
        creator=pymysql,  # 使用链接数据库的模块
        maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
        mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
        maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
        maxshared=3,
        # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，
        # 所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
        maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
        setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
        ping=0,
        # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested,
        # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='css',
        charset='utf8'
    )
