# Scrapy settings for mafengwo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mafengwo'
USER_AGENT = 'googlebot'
SPIDER_MODULES = ['mafengwo.spiders']
NEWSPIDER_MODULE = 'mafengwo.spiders'
COOKIES_ENABLED = True
COOKIES_DEBUG = True
DOWNLOAD_DELAY = 15
RANDOMIZE_DOWNLOAD_DELAY = True
REDIRECT_MAX_METAREFRESH_DELAY = 100
