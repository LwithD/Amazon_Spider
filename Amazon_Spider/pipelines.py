# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazonSpiderPipeline:

    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp = open('./amazon.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        name = item['name']
        # author = item['author']
        # rating = item['rating']
        # rating_num = item['rating_num']
        # price_kindle = item['price_kindle']
        # price_paper = item['price_paper']
        # price_hard = item['price_hard']
        # price_audio = item['price_audioCD']
        # self.fp.write(name+'\n'+author+'\n'+rating+'\n'+rating_num+'\n'+price_kindle+'\n'
        #     +price_paper+'\n'+price_hard+'\n'+price_audio)
        self.fp.write(name)
        return item

    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()