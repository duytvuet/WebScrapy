import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    in_stock = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()