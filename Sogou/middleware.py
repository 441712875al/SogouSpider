# encoding=utf-8
import random
from Sogou.myCookies import cookies
from Sogou.user_agents import agents
import scrapy.http.request


class UserAgentMiddleware(object):
    """ 换User-Agent """
    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """
    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        request.cookies = cookie
