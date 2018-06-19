# css_v1
基于烧瓶写的一个统计用户每日代码量的一个

包含方法有：
  1、登录（密码传输保存加密）；
  2、登出；
  3、上传代码并统计行数(设定每日仅可以上传一次，只能上传压缩包)；4、展示每个用户截至当前共上传代码量；5、展示个人每次上传代码量。
  
 需要安装的模块

pymysql
flask_session
redis
DBUtils	

注意：
因为使用的是redis存储的用户登陆信息，故需要配置	redis地址在config.py中配置【需要redis服务器】
用户名与密码需要手动添加到数据库中
两条分别为
	# 用户名 admin
    # 明文 admin1234
    # 密文 2435d800b38fcca0bf1a6b372def128a[数据库存储此密码]
	# 用户名 li
    # 明文 li1234
    # 密文 3661852d43fdb1dac44c66435af92e55[数据库存储此密码]
数据库准备：

CREATE DATABASE css CHARSET utf8
	
表准备：

用户表：
CREATE TABLE username(
    id INT NOT NULL auto_increment PRIMARY KEY,
    user VARCHAR(250) NOT NULL,
    pwd VARCHAR(250) NOT NULL,
    nick VARCHAR(250) NOT NULL
)ENGINE = INNODB DEFAULT CHARSET = utf8;


代码存储表
CREATE TABLE code(
    id INT NOT NULL auto_increment PRIMARY KEY,
    line VARCHAR(250) NOT NULL,
    ctime date NOT NULL,
    user_id INT NOT NULL
)ENGINE = INNODB DEFAULT CHARSET = utf8;

创建外键
alter table code add CONSTRAINT FK_ID foreign key(user_id) REFERENCES username(id); 

