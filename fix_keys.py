import json


# 修复缺失的键值对
def fix():
    for i in get_data:
        try:
            # 例句
            print ( i[ 'content' ][ 'word' ][ 'content' ][ 'sentence' ][ 'sentences' ][ 0 ] )
        except KeyError as e:
            e = str ( e )
            print ( "error:" + e )
            if e == '\'sentence\'':
                print ( '例句错误' )
                fix_sentence = {"sentence": {"sentences": [ {"sContent": "No example", "sCn": "无例句"} ]}}
                i[ 'content' ][ 'word' ][ 'content' ].update ( fix_sentence )
        try:
            # 英标
            print ( i[ "content" ][ 'word' ][ 'content' ][ 'ukspeech' ] )
        except KeyError as e:
            e = str ( e )
            print ( "error:" + e )
            if e == '\'ukspeech\'':
                print ( '音标错误' )
                word = i[ 'headWord' ]
                fix_ukspeech = {'ukspeech': f"{word}&type=1"}
                i[ "content" ][ 'word' ][ 'content' ].update ( fix_ukspeech )


if __name__ == '__main__':
    '''
    有道词典的单词书可能会缺失键值：例句'sentences'与发音'ukspeech'，其中例句均填写为 "无例句"(18行)
    故写此文件给需要换单词书的朋友
    '''
    bug_book = 'wordbook.json'  # 缺失键值的单词书(已经过 turn_json.py 转化格式)
    fix_book = 'fix.json'  # 修复保存至fix.json
    with open ( bug_book, encoding='utf-8' ) as f:
        get_data = json.load ( f )
    fix ()  # 调用修复
    # 重新打印测试
    for i in get_data:
        # 例句
        print ( i[ 'content' ][ 'word' ][ 'content' ][ 'sentence' ][ 'sentences' ][ 0 ] )
        # 英标
        print ( i[ "content" ][ 'word' ][ 'content' ][ 'ukspeech' ] )

    # 一行一个写入fix.json文件中
    with open ( fix_book, 'w', encoding='utf-8' ) as write_f:
        write_f.write ( '[' )
        for oneData in get_data:
            js = json.dumps ( oneData, ensure_ascii=False )
            write_f.write ( js )
            write_f.write ( ',' + '\n' )
        write_f.write ( ']' )
