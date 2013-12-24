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

s = """var _username = ';
var _user_logo = 'http://file25.mafengwo.net/M00/11/E4/wKgB4lKoFuWAFxRrAAA6n70ASWg64.head.w16.jpeg';
var _poi_center = {
    lat : parseFloat("40.7509596"),
    lng : parseFloat("-73.9903932"),
    zoom : parseInt(17)
};
var _add_score_info = '';

"""

lat = re.compile(r'lng : parseFloat\(\"(-{1}\d+.\d+)\"\)',re.S).search(s)
print lat.groups()
