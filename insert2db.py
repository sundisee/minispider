#coding:utf-8
import os,MySQLdb
fp = os.popen('').read()


import time, MySQLdb

#连接
conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")
cursor = conn.cursor()

#写入
sql = "insert into user(name,created) values(%s,%s)"
param = ("aaa",int(time.time()))
n = cursor.execute(sql,param)