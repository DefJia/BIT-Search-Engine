import sqlite3, re
from bs4 import BeautifulSoup
from configparser import ConfigParser


cfg = ConfigParser()
cfg.read("config.ini")

def analyze(cid):
    conn = sqlite3.connect("%sse.db" % cfg.get("Others", "dbpath"))
    c = conn.cursor()
    cursor = c.execute('select linkId, page FROM Webpage_info where id_=?', (cid, ))
    try:
        for row in cursor:
            lid = row[0]
            page = row[1]
    except:
        return 0
    else:
        soup = BeautifulSoup(page, 'html5lib')
        try: title = soup.title.string
        except: title = ''
        try: content = soup.get_text()  # 包含了一堆js， 很烦
        except: content = ''

        i = 0
        cursor = c.execute("SELECT count(*) from Hash_table");
        for row in cursor:
            length = row[0]
        c.execute("BEGIN")
        for link in soup.find_all('a'):
            a = link.get('href')
            if type(a) == str and a[:4] == 'http':
                print(cid, i, a)
                include = 0b1 << (length + i)
                include += 1
                try:c.execute('INSERT into Hash_table (link, include) values (?, ?)', (a, str(include)))
                except: pass
                i += 1
        content = " ".join(re.findall(u"[\u4e00-\u9fa5]+", content))
        c.execute('UPDATE Webpage_info SET title=?, content=? where id_=?', (title, content, cid))
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
        analyze(i + 1)