##coding:utf-8
#import  MySQLdb
#fp1 = open('/Users/yuwendy/mafengwo/poi','r').read()
#city_list = eval(fp1)
#conn=MySQLdb.connect(host="54.201.192.244",user="qyer",passwd="qyer",db="mafengwo",charset="utf8")
#cursor = conn.cursor()
#sql = "insert into poinfo(province_id,province_name,city_id,city_name) values(%s,%s,%s,%s)"
#
#for k,v in city_list.iteritems():
#    for i in v:
#        fp = open('/Users/yuwendy/mafengwo/province.html','r')
#        for line in fp.readlines():
#            print k,line
#            if k in line.split(',')[1]:
#                for k1,v1 in i.iteritems():
#                    param = (k,line.split(',')[0],k1,v1)
#                    print param
#                    n = cursor.execute(sql,param)
#                    conn.commit()
#conn.close()