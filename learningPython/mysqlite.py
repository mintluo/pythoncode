# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__),'mytest.db')
if os.path.isfile(db_file):
    os.remove(db_file)

#初始数据:
myconn=sqlite3.connect(db_file)
mycursor = myconn.cursor()
mycursor.execute('create table user(id varchar(20) primary key,name varchar(20), score int)')
mycursor.execute(r"insert into user values ('A-001','Adam', 95)")
mycursor.execute(r"insert into user values ('A-002','Bart', 69)")
mycursor.execute(r"insert into user values ('A-003','Lisa',78)")
mycursor.execute(r"insert into user values ('A-004','Lucy', 49)")
mycursor.close()
myconn.commit()
myconn.close()

def get_score_in(low,high):
    'get score from low to high'
    with sqlite3.connect('mytest.db') as mynewconn:
        mynewcursor = mynewconn.cursor()
        mynewcursor.execute('select name from user where score between ? and ? order by score',(low,high))
        values = mynewcursor.fetchall()
        out_result = list()
        for i in values:
            out_result += i
        return out_result
        #print('%s,get_score_in(%d, %d)'%(values,low,high))

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print(get_score_in(40, 100))
print('Pass')
