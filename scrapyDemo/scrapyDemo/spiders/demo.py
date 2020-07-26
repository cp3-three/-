"""
爬虫的入口文件
输入爬虫所要爬取的网站地址
"""
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['scrapyDemo']
    def start_requests(self):
        urls = ['http://python123.io/ws/demo.html',]       #所要爬取的网站集
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        #对爬取回来的内容进行解析
        fname=response.url.split('/')[-1]
        with open(fname,'wb') as f:
            f.write(response.body)
        self.log("save file %s."%fname)

