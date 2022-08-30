'''
    有道原词典需要转换一下json格式
'''
import json

youdao_book = 'YouDao.json'  # 有道源文件
turn_book = 'wordbook.json.json'  # 转化格式保存至wordbook.json

# 格式转换(win如果提示编码错误或音标ukphone乱码，用linux转)
with open ( youdao_book, 'r' ) as f1, open ( turn_book, 'a+' ) as f2:
    f2.writelines ( '[' )
    for line in f1:
        f2.writelines ( line + ',' )
    f2.writelines ( ']' )

# 转完格式后，手动删除一下最后一行”，“。注释10~14，解注释17~33，遍历一遍例句和读音，如果甩错，查看 fix_keys.py 纠正错误
# with open ( turn_book, encoding='utf-8' ) as f:
#     get_data = json.load ( f )
#
# for i in get_data:
#     # 单词序号
#     print ( i[ 'wordRank' ] )
#     # 单词
#     print ( i[ 'headWord' ] )
#     # 词义
#     print ( i[ "content" ][ 'word' ][ 'content' ][ 'trans' ] )
#     # 例句
#     print ( i[ 'content' ][ 'word' ][ 'content' ][ 'sentence' ][ 'sentences' ][ 0 ] )
#     # 英标
#     print ( i[ 'content' ][ 'word' ][ 'content' ][ 'ukphone' ] )
#     # 读音
#     print ( i[ "content" ][ 'word' ][ 'content' ][ 'ukspeech' ] )
