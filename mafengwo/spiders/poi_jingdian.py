#coding:utf-8
import MySQLdb
from urlparse import urlparse
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import re
import time

jingdian_urls = []
jingdian_url = 'http://www.mafengwo.cn/jd/%s/'
conn=MySQLdb.connect(host='localhost',user='root',passwd='qyer',db='mafengwo',port=3306,charset='utf8')
cur=conn.cursor()
cur.execute('select city_id from poinfo')
result = cur.fetchall()
jingdian_urls = [jingdian_url % i for i in result if i]
#判断有无重复
print len(jingdian_urls)
print len(list(set(jingdian_urls)))
jingdian_urls = list(set(jingdian_urls))
#cur.close()
#conn.close()
#从db读取城市列表拼装景点url
class ProvinceSpider(BaseSpider):
    name = "poi_jingdian"
    allowed_domains = ["www.mafengwo.cn"]
    start_urls = jingdian_urls

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="shop-list"]')
        for site in sites:
            url = site.select('ul/li/div[2]/h3/a/@href').extract()
            name = site.select('ul/li/div[2]/h3/a/text()').extract()
            city_id = re.search('\d+',response.url).group()
            for i in zip(url,name):
                sql = 'update poinfo set city_id=%s,poi_id=%s,poi_name=%s,poi_type=%s where poi_id=%s'
                poi_id = re.search('\d+',i[0]).group()
                params = (city_id,poi_id,i[1],u'景点',poi_id)
                n = cur.execute(sql,params)
                conn.commit()
#                print i[0],i[1]
#            cur.close()
#            conn.close()
        last_page = hxs.select('//a[@class="last-page"]/@href').extract()
        if last_page:
            last_page =  int((last_page[0].split('-')[-1]).split('.')[0])
            page_url = response.url+'0-0-0-0-0-2.html'
            if int(last_page) > 1:
                yield Request(url=page_url,callback=self.parse_page_url,meta={'i':2,'last_page':last_page})
    def parse_page_url(self,response):
#        conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='mafengwo',port=3306,charset='utf8')
#        cur=conn.cursor()
        hxs = HtmlXPathSelector(response)
        i = response.meta['i']
        last_page = response.meta['last_page']
        sites = hxs.select('//div[@class="shop-list"]')
        city_id  = re.search('\d+',response.url).group()
        for site in sites:
            url = site.select('ul/li/div[2]/h3/a/@href').extract()
            name = site.select('ul/li/div[2]/h3/a/text()').extract()
            for un in zip(url,name):
                sql = 'update   poinfo set city_id=%s,poi_id=%s,poi_name=%s,poi_type=%s  where poi_id=%s'
                poi_id = re.search('\d+',un[0]).group()
                params = (city_id,poi_id,un[1],u'景点',poi_id)
                n = cur.execute(sql,params)
                print un[0],un[1]
        page_base_url = 'http://www.mafengwo.cn/jd/%s/0-0-0-0-0-%s.html'
        i = i+1
        page_url = page_base_url % (city_id, i)
        print last_page
        if i <= last_page:
            yield Request(url=page_url,callback=self.parse_page_url,meta={'i':i,'last_page':last_page})
