# encoding=utf-8
BOT_NAME = 'Sogou'

SPIDER_MODULES = ['Sogou.spiders']
NEWSPIDER_MODULE = 'Sogou.spiders'

DOWNLOADER_MIDDLEWARES = {
    "Sogou.middleware.UserAgentMiddleware": 401,
    "Sogou.middleware.CookiesMiddleware": 402,
}

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'Sogou.pipelines.MongoDBPipleline': 300,
}

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

REDIS_HOST = '8.131.55.73'
# REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PARAMS = {'password': '123456al',}

# DOWNLOAD_DELAY = 10  # 间隔时间
# CONCURRENT_ITEMS = 1000
# CONCURRENT_REQUESTS = 100
# REDIRECT_ENABLED = False
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS_PER_IP = 0
# CONCURRENT_REQUESTS_PER_SPIDER=100
# DNSCACHE_ENABLED = True
LOG_LEVEL = 'INFO'    # 日志级别
# LOG_FILE = "/root/sogou_scrapy.log"
# CONCURRENT_REQUESTS = 70
