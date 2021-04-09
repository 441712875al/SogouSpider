# encoding=utf-8
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
from Sogou.keywords import keywords
from scrapy.selector import Selector
from Sogou.items import SogouItem
from w3lib.html import remove_tags
import re
import time
import math
from urllib import quote

class SogouSpider(RedisSpider):
    name = 'sogou'
    host = "https://weixin.sogou.com"
    base_url = "https://weixin.sogou.com/weixin?query={}&type=2&page={}&ie=utf8&p=01030402&dp=1"

    def start_requests(self):
        for keyword in keywords:
            print(self.base_url.format(quote(keyword),1))
            yield Request(url=self.base_url.format(quote(keyword),1),
                          meta={"keyword":keyword},
                          callback=self.parse_page)

    def parse_page(self,response):
        """获取页数"""
        keyword = response.meta['keyword']
        selector = Selector(response)
        num = selector.xpath("//div[@class='p-fy']/div[@class='mun']/text()").extract_first()
        num = int("".join(re.findall("\d", num)))
        page = int(math.ceil(num*1.0/10))
        for i in range(1,page+1):
            print(self.base_url.format(quote(keyword),i))
            yield Request(url=self.base_url.format(quote(keyword),i),meta={"keyword":keyword},callback=self.parse)

    def parse(self, response):
        keyword = response.meta['keyword']
        selector = Selector(response)
        tweets = selector.xpath("//ul[@class='news-list']/li")
        for tweet in tweets:
            sogouItem = SogouItem()
            sogouItem['topic'] = keyword
            sogouItem['_id'] = tweet.xpath("@d").extract_first().split('-')[2]
            sogouItem['title'] = remove_tags(tweet.xpath("div[@class='txt-box']/h3").extract_first()).strip()
            sogouItem['url'] = self.host+tweet.xpath("div[@class='txt-box']/h3/a/@href").extract_first()
            sogouItem['abstract'] = remove_tags(tweet.xpath("div[@class='txt-box']/p[@class='txt-info']").extract_first())
            sogouItem['source'] = remove_tags(tweet.xpath("div[@class='txt-box']/div[@class='s-p']/a[@class='account']/text()").extract_first())
            pubTime = remove_tags(tweet.xpath("div[@class='txt-box']/div[@class='s-p']/span").extract_first())
            pubTime = re.findall("timeConvert\(\'\d{10}", pubTime)
            if len(pubTime)>0:
                pubTime = pubTime[0]
                pubTime = int(pubTime.strip("timeConvert('"))
                timeArray = time.localtime(int(pubTime))
                otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
                sogouItem['pubTime'] = otherStyleTime
            yield sogouItem

        #翻页
        # next = selector.xpath("//div[@class='p-fy']/a[@id='sogou_next']/@href").extract_first()
        # if next:
        #     yield Request(url=self.host+"/weixin"+next,
        #                   meta={"keyword":keyword},
        #                   callback=self.parse)