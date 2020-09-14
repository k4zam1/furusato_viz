import scrapy
from satofuru.items import City

class NamesSpider(scrapy.Spider):
    """
    市町村名を取得する
    """
    name = 'names'
    allowed_domains = ['https://www.satofull.jp/products/list.php?s5=1&cnt=60&p=1']
    start_urls = ['https://www.satofull.jp/products/list.php?s5=1&cnt=60&p=1/']

    def parse(self, response):
        item = City()
        for t in response.css(".SideBox__tree")[3].css("a::text"):
            city = t.get()
            city_split = city.split("（")
            city = city_split[0]
            item["name"] = city
            yield item