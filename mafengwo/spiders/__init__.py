# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
#import os
#print os.path.realpath(__file__)

import re
#s = '$#222'
#print  re.findall(r'[2|#|$)]',s)

#var poiCenter = {
#    "lat" : parseFloat('39.947187'),
#    "lng" : parseFloat('116.420531'),
#    "zoom" : 15 //parseInt('8')
#};

s = """var _poi_center = {
    lat : parseFloat("0"),
    lng : parseFloat("-105.69899749756"),
    zoom : parseInt(16)
};

"""

lat = re.compile(r'lng : parseFloat\(\"(-{0,1}\d{0,10}.{0,1}\d+)\"\)',re.S).search(s)
print lat.groups()
