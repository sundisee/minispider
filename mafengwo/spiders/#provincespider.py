##coding:utf-8
#import json
#import urllib2
#from scrapy.selector import HtmlXPathSelector
#from scrapy.spider import BaseSpider
#
#class ProvinceSpider(BaseSpider):
#    name = "province"
#    allowed_domains = ["www.mafengwo.cn"]
#    start_urls = [
#        "http://www.mafengwo.cn/mdd/smap.php?mddid=10848"
#    ]
#
#    def parse(self, response):
#        hxs = HtmlXPathSelector(response)
#        sites = hxs.select('//div[@class="mdd_dh"]//div[@class="mdh_li"][2]')
#        for site in sites:
#            name = site.select('ul/li/a/text()').extract()
#            url = site.select('ul/li/a/@href').extract()
#            fp = open('province.html','wb')
#            for i in zip(name,url):
#                fp.write(i[0].encode('utf-8')+','+i[1].encode('utf-8')+'\n')
#            fp.close()
