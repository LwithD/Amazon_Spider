import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Amazon_Spider.items import AmazonSpiderItem
from scrapy_redis.spiders import RedisCrawlSpider
import re

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    # allowed_domains = ['https://www.amazon.com/',
    #         'https://aax-us-east.amazon-adsystem.com/']
    # start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_72%3A1250224011&dc&qid=1620543950&rnid=1250219011&ref=lp_1000_nr_p_72_3']

    redis_key = 'amazon'

    link_list = LinkExtractor(allow = r'ref=sr_pg_\d+')
    link_detail = LinkExtractor(allow=r'ref=sr_\d+_\d+')#&ref=sr_\d+_\d+

    rules = (
        Rule(link_list,follow=True),#callback = 'parsesss',
        Rule(link_detail, callback='parse_item', follow=False),
    )

    # def parsesss(self,response):
    #     item = AmazonSpiderItem()
    #     item['name'] = response.text
    #     yield item

    def parse_item(self, response):
        item = AmazonSpiderItem()
        name = response.xpath('//*[@id="productTitle"]/text()').extract_first()
        if isinstance(name, list):
            name = ''.join(name)
        name = name.replace('\n', '')
        item['name'] = name
        item['author'] = response.xpath('//*[@id="bylineInfo"]/span/span[1]/a[1]/text()').extract_first()
        rating = response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract_first()
        rating = re.findall('(\d?\.?\d+) out of',rating)[0]
        item['rating'] = rating
        rating_num_response= response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract_first()
        if ',' in rating_num_response:
            rating_num = int(re.findall(r'(\d.?),',rating_num_response)[0])*1000+int(re.findall(r',(\d+) ratings',rating_num_response)[0])
        else:
            rating_num = int(re.findall(r'(\d+) ratings',rating_num_response)[0])
        item['rating_num'] = rating_num
        li_list = response.xpath('//*[@id="tmmSwatches"]/ul/li')
        for li in li_list:     #/span/span[1]/span/a/span[2]/text()
            price = li.xpath('./span/span[1]/span[1]/a/span[2]//text()').extract()
            price = ''.join(price)
            price = re.findall('\$(\d+\.?\d+)',price)
            if price == []:
                continue
            else:
                price = float(price[0])
            s = li.xpath('./span/span/span/a/span[1]/text()').extract_first()
            if 'Kindle' in s or 'kindle' in s:
                item['price_kindle']=price
            elif 'Paperback' in s:
                item['price_paper'] = price
            elif 'Hardcover' in s:
                item['price_hard'] = price
            elif 'Audio CD' in s:
                item['price_audioCD'] = price
        print(item)
        yield item
