import sqlite3, requests, datetime
from configparser import ConfigParser
import dns.resolver

cfg = ConfigParser()
cfg.read("config.ini")
conn = sqlite3.connect("%s/%s" % (cfg.get("Others", "db_path"), cfg.get("Others", "db_name")))
cid = cfg.getint("Crawl", "startid")


class Crawl:
    """
        Description
    """
    def __init__(self, cid):
        self.c = conn.cursor()
        self.cursor = self.c.execute("SELECT id_, link, rate, updateTime from Hash_table where id_ = ? and type >= 0", cid)
        for row in self.cursor:
            self.id_ = row[0]
            self.link = row[1]
            self.rate = row[2]
            self.u_time = row[3]

    @staticmethod
    def judge_url(url):
        """
        :param url:
        :return: 0 -> inner, 1 -> outer;
        """
        record = dns.resolver.query(url, 'A')
        tmp = record.response.answer[0].items[0]
        if hasattr(tmp, 'address') and tmp.address[:2] == '10':
            return 0
        else:
            return 1

    def judge(self):
        if self.judge_url(self.link) == 1:
            self.cursor = self.c.execute(
                "delete from Hash_table where id_=?", cid)
            return -1
        if self.u_time != '':
            u_datetime = datetime.datetime.strptime(self.u_time, "%Y-%m-%d %H:%M:%S")
            diff = cfg.getint("Others", "expire_time")
            if datetime.datetime.now() - u_datetime < datetime.timedelta(seconds=diff):
                # less than expire time.
                pass
            else:
                return self.crawl('update')
        else:
            return self.crawl('insert')

    def crawl(self, operation):
        try:
            timeout = cfg.getint("Others", "timeout")
            r = requests.get(self.link, timeout=timeout)
            r.encoding = 'utf-8'
            html = r.text
        except:
            return -1
        else:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if operation == 'update':
                self.c.execute('UPDATE Hash_table SET updateTime=datetime("now", "localtime") where id_=?', cid)
                self.c.execute('UPDATE Webpage_info SET page=? where linkId=?', (html, cid))
            else:
                self.c.execute('update Hash_table set updateTime=datetime("now", "localtime") where id_=?', cid)
                self.c.execute('INSERT into Webpage_info (linkId, page) values (?, ?)', (cid, r.text))
            conn.commit()
            print(format("succeed in %s, id: %d") % (self.link, cid))
            return Analyze(self.rate+1, html)

class Analyze:
    """
        Description.
    """
    def __init__(self, rate, html):
        self.c = conn.cursor()
        pass

    def analyze(self):
            try:
                for row in cursor:
                    lid = row[0]
                    page = row[1]
            except:
                return 0
            else:
                soup = BeautifulSoup(page, 'html5lib')
                try:
                    title = soup.title.string
                except:
                    title = ''
                try:
                    content = soup.get_text()  # 包含了一堆js， 很烦
                except:
                    content = ''

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
                        try:
                            c.execute('INSERT into Hash_table (link, include) values (?, ?)', (a, str(include)))
                        except:
                            pass
                        i += 1
                content = " ".join(re.findall(u"[\u4e00-\u9fa5]+", content))
                c.execute('UPDATE Webpage_info SET title=?, content=? where id_=?', (title, content, cid))
                conn.commit()
            conn.close()

if __name__ == '__main__':
    conn = sqlite3.connect("%sse.db" % cfg.get("Others", "dbpath"))
    c = conn.cursor()
    cursor = c.execute("SELECT count(*) from Hash_table");
    for row in cursor:
        length = row[0]
    conn.close()
    for i in range(length):
        main(i + 1)

if __name__ == '__main__':
    url = 'www.bitren.com'
    cur = Crawl
    a = cur.judge_url(url)
    conn.close()