import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class LyricPipeline(object):
  def __init__(self):
    self.conn = MySQLdb.connect(user='root', '123', 'testChi', 'localhost', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

def process_item(self, item, spider):    
    try:
        self.cursor.execute("INSERT INTO lyric (singerName, songName, songLyric)  VALUES (%s, %s, %s)", 
                       (item['singerName'].encode('utf-8'), 
                        item['songName'].encode('utf-8'),
                        item['songLyric'].encode('utf-8')))

        self.conn.commit()


    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


    return item