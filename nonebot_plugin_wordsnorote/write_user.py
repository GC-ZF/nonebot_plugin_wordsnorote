import json
import os
from pathlib import Path
from nonebot import get_driver

# 本地单独调试文件内容
# filepath = os.path.dirname ( __file__ )
# file_name = os.path.join ( filepath, "student.json" )

# 服务器调试 用户数据在 data/student.json ，如果不存在，自动创建(派克)
try:
    resPath = Path ( get_driver ().config.resources_dir )/"wordsnorote"
    assert os.path.exists ( resPath )
    file_name = resPath/"student.json"
except (AttributeError, AssertionError):
    resPath = Path ()/"data"/"wordsnorote"
    if not os.path.exists ( resPath ):
        resPath.mkdir ( parents=True, exist_ok=True )
    file_name = resPath/"student.json"

# 初始JSON数据(young)
student_config = [{
    "user": "1310446718",
    "date": 1,
    "wordID": 0
}]


# 用户数据在 data/student.json ，如果不存在，自动创建
class FileTool:
    def __init__(self):
        if not os.path.exists ( file_name ):
            with open ( file_name, 'w', encoding='utf-8' ) as f:
                json.dump ( student_config, f, ensure_ascii=False, indent=4 )


def write_file(user_id, wordID, date, bool):
    # 获取json数据
    with open ( file_name ) as f:
        get_data = json.load ( f )
    # print(get_data)

    # 第一次背加入新数据
    if bool == True:
        new_data = {"user": user_id, "date": date, "wordID": wordID}
        get_data.append ( new_data )
    # 不是第一次背，修改数据
    elif bool == False:
        for i in get_data:
            if i[ 'user' ] == user_id:
                i[ 'wordID' ] = wordID
                i[ 'date' ] = date
    # print(get_data)

    # 写入数据
    # with open ( file_name, 'w' ) as f:
    #     json.dump ( get_data, f )

    # 以格式化写入
    with open ( file_name, 'w' ) as write_f:
        write_f.write ( json.dumps ( get_data, indent=4, ensure_ascii=False ) )

# write_file ( '1310446718', 5, 28, True )
