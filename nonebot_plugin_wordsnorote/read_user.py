import json
import os
from pathlib import Path

# 本地单独调试文件内容
# filepath = os.path.dirname ( __file__ )
# file_name = os.path.join ( filepath, "student.json" )


# 服务器调试 data/wordsnorote/student.json
file_name = 'data/wordsnorote/student.json'


# 所有用户信息
def user_data():
    with open ( file_name ) as f:
        get_data = json.load ( f )
    return get_data


# 获取用户名列表
def user_list():
    dic = user_data ()
    users = [ ]

    # "1310446718":{
    #     "date": 28,
    #     "wordID": 50
    # }
    # for i in dic:
    #     temp= list ( i.keys () )[0]
    #     user.append ( temp )

    # {
    #     "user": "1310446718",
    #     "date": 28,
    #     "wordID": 50
    # }
    for i in dic:
        users.append ( i.get ( 'user' ) )
    return users


# 获取用户wordID
def user_wordID(userID):
    dic = user_data ()
    for i in dic:
        if i[ 'user' ] == userID:
            wordID = i[ 'wordID' ]
    return wordID


# 获取用户date
def user_date(userID):
    dic = user_data ()
    for i in dic:
        if i[ 'user' ] == userID:
            date = i[ 'date' ]
    return date
