import scrapy
import re
from bs4 import BeautifulSoup

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    #allowed_domains = ['baidu.com']
    start_urls = ['https://quote.eastmoney.com/stock_list.html']
    def parse(self, response):
        for stockID in re.finditer(r'http://quote.eastmoney.com/(sh\d{6}).html', response.text):
            try:
                InfoUrl="https://xueqiu.com/S/"+stockID.group(1).upper()
                yield scrapy.Request(InfoUrl,callback=self.parse_stock)
            except:
                continue

    def parse_stock(self,response):
        infoDict={}
        if(response==''):
            exit()
        try:
            name=re.search(r'<div class="stock-name">(.*?)</div>',response.text)
            infoDict.update({'股票名称':name.group(1)})
            #print(response.text)
            tableHTML=re.search(r'"tableHtml":"(.*?)",',response.text)
            soupInfo=BeautifulSoup(tableHTML.group(0),"html.parser")
            table=soupInfo.table
            #print(table)
            for i in table.find_all('td'):
                line=i.text
                l=line.split('：')
                infoDict.update({l[0]:l[1]})
            yield infoDict
        except:
            print("error")

