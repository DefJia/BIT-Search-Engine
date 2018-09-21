import sqlite3, jieba
from configparser import ConfigParser
import jieba.posseg as pseg


cfg = ConfigParser()
cfg.read("config.ini")
d = {'k': {'desc': ' ', 'ch': '后接成分'}, 'un': {'desc': 'hhh', 'ch': '未知词'}, 'a': {'desc': '取英语形容词 adjective的第1个字母。', 'ch': '形容词'}, 'r': {'desc': '取英语代词 pronoun的第2个字母,因p已用于介词。', 'ch': '代词'}, 'm': {'desc': '取英语 numeral的第3个字母，n，u已有他用。', 'ch': '数词'}, 'o': {'desc': '取英语拟声词 onomatopoeia的第1个字母。', 'ch': '拟声词'}, 'nt': {'desc': '“团”的声母为 t，名词代码n和t并在一起。', 'ch': '机构团体'}, 'g': {'desc': '绝大多数语素都能作为合成词的“词根”，取汉字“根”的声母。', 'ch': '语素'}, 'z': {'desc': '取汉字“状”的声母的前一个字母。', 'ch': '状态词'}, 'v': {'desc': '取英语动词 verb的第一个字母。', 'ch': '动词'}, 'dg': {'desc': '副词性语素。副词代码为 d，语素代码ｇ前面置以D。', 'ch': '副语素'}, 't': {'desc': '取英语 time的第1个字母。', 'ch': '时间词'}, 'nr': {'desc': '名词代码 n和“人(ren)”的声母并在一起。', 'ch': '人名'}, 'an': {'desc': '具有名词功能的形容词。形容词代码 a和名词代码n并在一起。', 'ch': '名形词'}, 'vg': {'desc': '动词性语素。动词代码为 v。在语素的代码g前面置以V。', 'ch': '动语素'}, 'h': {'desc': '取英语 head的第1个字母。', 'ch': '前接成分'}, 'ns': {'desc': '名词代码 n和处所词代码s并在一起。', 'ch': '地名'}, 'y': {'desc': '取汉字“语”的声母。', 'ch': '语气词'}, 'f': {'desc': '取汉字“方”', 'ch': '方位词'}, 'x': {'desc': '非语素字只是一个符号，字母 x通常用于代表未知数、符号。', 'ch': '非语素字'}, 'Ng': {'desc': '名词性语素。名词代码为 n，语素代码ｇ前面置以N。', 'ch': '名语素'}, 'd': {'desc': '取 adverb的第2个字母，因其第1个字母已用于形容词。', 'ch': '副词'}, 'ad': {'desc': '直接作状语的形容词。形容词代码 a和副词代码d并在一起。', 'ch': '副形词'}, 'n': {'desc': '取英语名词 noun的第1个字母。', 'ch': '名词'}, 'vd': {'desc': '直接作状语的动词。动词和副词的代码并在一起。', 'ch': '副动词'}, 'w': {'desc': ' ', 'ch': '标点符号'}, 'p': {'desc': '取英语介词 prepositional的第1个字母。', 'ch': '介词'}, 'j': {'desc': '取汉字“简”的声母。', 'ch': '简称略语'}, 'vn': {'desc': '指具有名词功能的动词。动词和名词的代码并在一起。', 'ch': '名动词'}, 'b': {'desc': '取汉字“别”的声母。', 'ch': '区别词'}, 'i': {'desc': '取英语成语 idiom的第1个字母。', 'ch': '成语'}, 'c': {'desc': '取英语连词 conjunction的第1个字母。', 'ch': '连词'}, 'Ag': {'desc': '形容词性语素。形容词代码为 a，语素代码ｇ前面置以A。', 'ch': '形语素'}, 'e': {'desc': '取英语叹词 exclamation的第1个字母。', 'ch': '叹词'}, 'u': {'desc': '取英语助词 auxiliary', 'ch': '助词'}, 'q': {'desc': '取英语 quantity的第1个字母。', 'ch': '量词'}, 'l': {'desc': '习用语尚未成为成语，有点“临时性”，取“临”的声母。', 'ch': '习用语'}, 'nz': {'desc': '“专”的声母的第 1个字母为z，名词代码n和z并在一起。', 'ch': '其他专名'}, 'tg': {'desc': '时间词性语素。时间词代码为 t,在语素的代码g前面置以T。', 'ch': '时语素'}, 's': {'desc': '取英语 space的第1个字母。', 'ch': '处所词'}}


def segment(cid):
    conn = sqlite3.connect("%sse.db" % cfg.get("Others", "dbpath"))
    c = conn.cursor()
    cursor = c.execute("SELECT content FROM Webpage_info where id_=?", (cid, ))
    for row in cursor:
        content = row[0]
    # lst = list(jieba.cut_for_search(content))
    words = pseg.cut(content)
    # 需要去重
    c.execute("BEGIN")
    for w in words:
        if w.word != '' and w.flag != 'x':
            try: c.execute('INSERT into word_list (word, part, index_, note) VALUES (?, ?, ?, ?)', (w.word, d[w.flag]['ch'], str(0b1 << cid), d[w.flag]['desc']))
            except: pass
    conn.commit()
    conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect("%sse.db" % cfg.get("Others", "dbpath"))
    c = conn.cursor()
    cursor = c.execute("SELECT count(*) from Webpage_info");
    for row in cursor:
        length = row[0]
    conn.close()
    for i in range(length):
        segment(i + 1)