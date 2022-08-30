import json
import os

filepath = os.path.dirname ( __file__ )
file_name = os.path.join ( filepath, "student.json" )


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
