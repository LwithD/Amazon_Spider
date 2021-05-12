# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class AmazonSpiderPipeline:

    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp = open('./amazon.txt','a',encoding='utf-8')

    def process_item(self, item, spider):
        # name = item['name']
        # author = item['author']
        # rating = item['rating']
        # rating_num = item['rating_num']
        # price_kindle = str(item['price_kindle'])
        # price_paper = item['price_paper']
        # price_hard = item['price_hard']
        # price_audio = item['price_audioCD']
        output = ''
        for key in item:
            output= output+key+':'+str(item[f'{key}'])+'\n'
        self.fp.write(output)
        # self.fp.write(name)
        return item

    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()


class AmazonMysqlPipeline:
    
    conn = None
    cursor = None
    list = ['name','author','rating','rating_num','price_kindle','price_hard','price_paper','price_audioCD']
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password = 'password',db ='amazon')
    
    
    def process_item(self,item, spider):
        self.cursor = self.conn.cursor()
        try:
            #sql命令
            sql = 'insert into books(id,name,author,rating,rating_num,price_kindle,price_hard,price_paper,price_audioCD) values(0,'
            i = 0   #list下标
            for key in item:
                if self.list[i] == key:
                    sql= sql+'"'+str(item[f'{key}'])+'",'
                else:
                    sql = sql+'null,'
                i+=1
            sql = sql[:-1]
            sql = sql+')'
            print(sql)
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

        return item
    
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()