import scrapy
import re
import logging
from satofuru.items import Gift

class GiftSpider(scrapy.Spider):
    name = 'gift'
    allowed_domains = ['https://www.satofull.jp/']
    start_urls = ['https://www.satofull.jp/products/list.php?s5=1&cnt=60&p=1/']

    def start_requests(self):
        logging.basicConfig(level=logging.INFO)
        #urls = response.css('.SideBox__tree')[3].css('a::attr("href")').extract()
        urls = [
            "https://www.satofull.jp/products/list.php?s5=1&cnt=60&p=", # 北海道
            "https://www.satofull.jp/products/list.php?s5=2&cnt=60&p=", # 東北地方
            "https://www.satofull.jp/products/list.php?s5=3&cnt=60&p=", # 関東地方
            "https://www.satofull.jp/products/list.php?s5=4&cnt=60&p=", # 中部地方
            "https://www.satofull.jp/products/list.php?s5=5&cnt=60&p=", # 近畿地方
            "https://www.satofull.jp/products/list.php?s5=6&cnt=60&p=", # 中国地方
            "https://www.satofull.jp/products/list.php?s5=7&cnt=60&p=", # 四国地方
            "https://www.satofull.jp/products/list.php?s5=8&cnt=60&p=", # 九州地方
        ]
        for url in urls :
            for i in range(1,167):
                logging.info(r'processing {}...'.format(url))
                yield scrapy.Request(url+str(i))

    def parse(self,response):
        item = Gift()
        item_citys = response.css(".ItemList")[0].css(".ItemList__city").css('p::text')
        item_links = response.css(".ItemList")[0].css(".ItemList__link").css('a::attr("href")')
        item_names = response.css(".ItemList")[0].css(".ItemList__name").css("p::text")
        item_prices = response.css(".ItemList")[0].css(".ItemList__price").css('span::text')
        item_descs = response.css(".ItemList")[0].css(".ItemList__description").css('p::text')
        item_star = response.css(".ItemList")[0].css(".ItemList__review").css('img::attr("src")')
        item_review_num = response.css(".ItemList")[0].css(".ItemList__review::text")[1::2]
        item_img = response.css(".ItemList")[0].css(".ItemList__picture").css('img::attr("src")')

        if len(item_citys) == 0:
            return

        items = {
            "city":item_citys,
            "link":item_links,
            "name":item_names,
            "price":item_prices,
            "desc":item_descs,
            "star":item_star,
            "review":item_review_num,
            "img":item_img
        }
        
        base_addr = "https://www.satofull.jp"
        num = re.compile('\d+') # 数字を抽出する正規表現

        for i in range(len(items)+1):
            item["city"] = items["city"][i].get()
            item["link"] = base_addr + items["link"][i].get()
            item["name"] = items["name"][i].get()
            item["price"] = items["price"][i].get()
            item["desc"] = items["desc"][i].get()
            item["star"] = num.findall(items["star"][i].get())[0]
            item["review"] = num.findall(items["review"][i].get())[0]
            item["img"] = base_addr + items["img"][i].get()
            yield item
