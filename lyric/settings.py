# Scrapy settings for lyric project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'lyric'

SPIDER_MODULES = ['lyric.spiders']
NEWSPIDER_MODULE = 'lyric.spiders'


MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "mydb"
MONGODB_COLLECTION = "song"
ITEM_PIPELINES = ['lyric.pipelines.LyricPipeline',]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lyric (+http://www.yourdomain.com)'
