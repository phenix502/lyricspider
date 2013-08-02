#!/usr/bin/python
#-*-coding:utf-8-*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


from scrapy.selector import HtmlXPathSelector
from lyric.items import LyricItem






class Lyric_Spider(CrawlSpider):
	name = "Lyric"
	allowed_domains = ["cnlyric.com"]
	start_urls = ["http://www.cnlyric.com/singerlist_a.html"]
	rules = (

                # 限制爬虫进入下一个链接的地方
		Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class="center"]//a/@href'))),
		Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class="navi"]//a/@href'))),

                # 允许爬虫进入对geshou,geci这样的链接
		Rule(SgmlLinkExtractor(allow=[r'geshou/\d+'])),
		Rule(SgmlLinkExtractor(allow=[r'geci/\d+/\d+']),
			callback = 'parse_lyric'),

		Rule(SgmlLinkExtractor(allow=[r'singerlist_[b-z]']))
		
	)

        
	def parse_lyric(self, response):
		hxs = HtmlXPathSelector(response)

		item = LyricItem()
		item['singerName'] = hxs.select('//tt/a[3]/text()').extract()
		item['songLyric'] = hxs.select('//div[@class="stxt"]/text()').extract()
		item['songName'] = hxs.select('//tt/text()[4]').extract()

		return item

		 
