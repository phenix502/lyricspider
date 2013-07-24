#!/usr/bin/env 
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from lyric.items import LyricItem

class Lyric_Spider(BaseSpider):
	name = "Lyric"
	allowed_domains = ["cnlyric.com"]
	start_urls = ["http://www.cnlyric.com/singerlist.html"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		singerlist = hxs.select('//ul/li')

		items = []
		for singer in singerlist:
			item = LyricItem()
			item['singerName'] = singer.select('a/text()').extract()
			item['singerLink'] = singer.select('a/@href').extract()
			items.append(item)
		return items
