# Scrapy settings for mafengwo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mafengwo'

SPIDER_MODULES = ['mafengwo.spiders']
NEWSPIDER_MODULE = 'mafengwo.spiders'
DOWNLOAD_DELAY = 1
