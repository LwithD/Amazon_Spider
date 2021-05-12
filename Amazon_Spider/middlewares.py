# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

#proxy
from Amazon_Spider import settings
import random




class AmazonSpiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)








class AmazonSpiderDownloaderMiddleware:
    
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        request.headers['User-Agent'] = str(UserAgent().random)
    
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    # def __del__(self):
    #     self.browser.close()

    def spider_opened(self, spider):
        settings.refresh_pool()
        spider.logger.info('Spider opened: %s' % spider.name)
        





class ProxyMiddleWare(object):


    def process_request(self,request, spider):
        '''对request对象加上proxy'''
        proxy = random.choice(settings.PROXY_POOL)
        spider.logger.info("this is request ip:"+proxy)
        request.meta['proxy'] = proxy


    def process_response(self, request, response, spider):
        # 如果返回的response状态不是200，重新生成当前request对象
        # if response.status != 200:
        #     proxy = random.choice(PROXY_POOL)
        #     self.spider.logger.info("this is request ip:"+proxy)
        #     request.meta['proxy'] = proxy
        #     return request
        return response

    def process_exception(self, request, exception, spider):
        if 'proxy' not in request.meta:
            spider.logger.error("没代理错了,需要检查")
            return
        else:
            spider.logger.error("有代理也错了，刷新代理池")
            settings.refresh_pool()
            request.meta["exception"] = True
            spider.logger.info("重新获取ip")
            proxy = random.choice(settings.PROXY_POOL)
            spider.logger.info("this is request ip:"+proxy)
            request.meta['proxy'] = proxy
            return  request

        




# import os

# from scrapy.dupefilter import RFPDupeFilter

# class CustomFilter(RFPDupeFilter):
# """A dupe filter that considers specific ids in the url"""

#     def __getid(self, url):
#         mm = url.split("&refer")[0] #or something like that
#         return mm

#     def request_seen(self, request):
#         fp = self.__getid(request.url)
#         if fp in self.fingerprints:
#             return True
#         self.fingerprints.add(fp)
#         if self.file:
#             self.file.write(fp + os.linesep)