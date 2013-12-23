#coding:utf-8
import MySQLdb
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import re
import time

jingdian_poi_urls = []
jingdian_url = 'http://www.mafengwo.cn/poi/%s.html'
conn=MySQLdb.connect(host='54.201.192.244',user='qyer',passwd='qyer',db='mafengwo',port=3306,charset='utf8')
cur=conn.cursor()
cur.execute('select poi_id from poinfo where poi_id IS NOT NULL  and poi_type = "美食"')
result = cur.fetchall()
jingdian_poi_urls = [jingdian_url % i for i in result]
print jingdian_poi_urls
#判断有无重复
print len(jingdian_poi_urls)
print len(list(set(jingdian_poi_urls)))
#cur.close()
#conn.close()
#从db读取城市列表拼装景点url
class ProvinceSpider(BaseSpider):
    name = "poi_meishi_content"
    allowed_domains = ["www.mafengwo.cn"]
    start_urls = jingdian_poi_urls

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        lat = re.compile(r'\"lat\" : parseFloat\(\'(\d+.\d+)',re.S).search(response.body)
        lng = re.compile(r'\"lng\" : parseFloat\(\'(\d+.\d+)',re.S).search(response.body)
        poi_latitude = lat.groups()[0]
        poi_longitude =  lng.groups()[0]
        poi_fen = hxs.select('//span[@class="score"]/em/text()').extract()[0]
        poi_mustgo = hxs.select('//div[@class="star"]/span/text()').extract()[0]
        poi_pj_count = hxs.select('//div[@class="num"]/em/text()').extract()[0]
        poi_quguo_percent = hxs.select('//dl[@class="item-extra"]/dt[2]/span[@class="num"]/text()').extract()[0]
        poi_pic = hxs.select('//div[@class="album"]/a/img/@src').extract()[0]
        #        poi_longitude = hxs.select('//div[@class="bd"]/span/meta[1]/@content').extract()[0]
        #        poi_latitude = hxs.select('//div[@class="bd"]/span/meta[2]/@content').extract()[0]
        poi_info = hxs.select('//div[@class="poi-intro"]').extract()[0]

        print poi_fen,poi_mustgo,poi_latitude,poi_longitude,poi_pj_count,poi_quguo_percent,poi_pic
        sql = 'update  poinfo set poi_fen=%s,poi_mustgo=%s,poi_pj_count=%s,poi_quguo_percent=%s,poi_pic=%s,poi_longitude=%s,\
        poi_latitude=%s,poi_info=%s  where poi_id = %s'
        poi_id = re.search('\d+',response.url).group()
        params = (poi_fen,poi_mustgo,poi_pj_count,poi_quguo_percent,poi_pic,poi_longitude,poi_latitude,poi_info,poi_id)
        n = cur.execute(sql,params)
        conn.commit()
        print 'success'
