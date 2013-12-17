# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MafengwoItem(Item):
    # define the fields for your item here like:
    url = Field()
    name = Field()
    description = Field()
    size = Field()
