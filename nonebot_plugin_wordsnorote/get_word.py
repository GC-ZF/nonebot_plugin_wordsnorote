import json
import os

# 本地单独调试文件内容
# filepath = os.path.dirname ( __file__ )
# file_name = os.path.join ( filepath, "Kaoyan.json" )

# 服务端调试 wordbook.json 为自定义单词本
file_name = 'data/wordsnorote/wordbook.json'
if not os.path.exists ( file_name ):
    filepath = os.path.dirname ( __file__ )
    file_name = os.path.join ( filepath, "Kaoyan.json" )


# 获取单词列表
def get_word(num_words, wordID):
    with open ( file_name, encoding='utf-8' ) as f:
        get_data = json.load ( f )

    # 打印5个测试
    # for i in range(5):
    #     print ( get_data[i] )
    trans_word = word_translate ( num_words, wordID )
    dic_word = [ ]
    for i in range ( num_words ):
        temp = {"单词序号": get_data[ i + wordID ][ "wordRank" ],
                "单词": get_data[ i + wordID ][ "headWord" ],
                "词义": trans_word[ i ][ f'{i + wordID + 1}' ],
                "例句1": get_data[ i + wordID ][ "content" ][ 'word' ][ 'content' ][ 'sentence' ][ 'sentences' ][ 0 ][
                    "sContent" ],
                "例句1翻译": get_data[ i + wordID ][ "content" ][ 'word' ][ 'content' ][ 'sentence' ][ 'sentences' ][ 0 ][
                    "sCn" ],
                "英标": get_data[ i + wordID ][ "content" ][ 'word' ][ 'content' ][ 'ukphone' ],
                "读音": 'https://dict.youdao.com/dictvoice?audio=' +
                      get_data[ i + wordID ][ "content" ][ 'word' ][ 'content' ][ 'ukspeech' ]
                }
        print ( temp )
        dic_word.append ( temp )
    return dic_word


def word_translate(num_words, wordID):
    '''
    词性+翻译放在列表中，每个单词tranCn数量不确定，不方便取
    [{'tranCn': '爆炸的， 爆发的；使人冲动的； 导致猛烈爆发的', 'descOther': '英释', 'pos': 'adj', 'descCn': '中释'},
     {'tranCn': '爆炸物， 炸药', 'descOther': '英释', 'pos': 'n', 'descCn': '中释'}]
    通过重建一个字典 translate_dic
    {'单词序号': 1, '词义': 'adj.爆炸的， 爆发的；使人冲动的； 导致猛烈爆发的n.爆炸物， 炸药'}
    '''
    with open ( file_name, encoding='utf-8' ) as f:
        get_data = json.load ( f )
    translate_dic = [ ]
    for i in range ( wordID, wordID + num_words ):
        trans = get_data[ i ][ "content" ][ 'word' ][ 'content' ][ 'trans' ]
        translate = ''
        for j in trans:
            temp = j[ 'pos' ] + '.' + j[ 'tranCn' ]  # 词性+中译
            translate = translate + temp + ' '
            word_id = get_data[ i ][ "wordRank" ]  # 获取单词序号
            temp_dic = {f'{word_id}': translate}
        translate_dic.append ( temp_dic )

    return translate_dic


'''
 搜”_3_单词id“
在"content":{后补充
 "sentence":{"sentences":[{"sContent":"No example","sCn":"无例句"}]},
 
 在"ukphone"后或"content":{后补充
 "ukspeech":"单词&type=1",
 有可能缺失一些键值，通过整个文件测试及报错信息手动修补
'''
# 整个文件测试
# word_list = get_word ( 3728, 0 )
