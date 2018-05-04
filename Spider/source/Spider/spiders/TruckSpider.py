import util
import scrapy


# 按照类型爬取, 常规类型
class TruckSpider(scrapy.Spider):
    name = 'TruckSpider'

    mongo_client = ''
    redis_client = ''
    base_url = 'https://product.360che.com'
    truck_count = 0
    start_urls = [
        "https://product.360che.com/BrandList.html",
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.run_once = False
        self.mongo_client = util.MongoDB.client()
        self.redis_client = util.RedisDB.client()

    def parse(self, response):
        self.truck_count += 1

    def close(self, reason):
        # info = {'name': 'test'}
        # self.mongo_client.test.insert(info)
        # self.redis_client.set('name', 'leeeee')
        print('finished')
