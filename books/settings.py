BOT_NAME = 'books'

SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'books (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'books.pipelines.MongoDBPipeline': 300}
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = "books"
MONGO_COLLECTION = 'titles'