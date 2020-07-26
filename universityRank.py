# codeing=utf-8
# author:jone yang
# date:2020/7/11
# describe:利用requests，bs4.beautifulSoup库进行一个定向网络爬虫，并整理出大学排名

import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        html=requests.get(url)
        html.encoding=html.apparent_encoding
        html.raise_for_status()
        return html.text
    except:
        print("爬取失败")
        return ''


def fillUnivList(ulist,urlText,num=20):
    if(urlText==None):
        return False

    soup=BeautifulSoup(urlText,"html.parser")
    for i in range(1,num+1):
        start=soup.find('td',string=i)
        infoList=list(start.next_siblings)
        rank=i
        univName=infoList[1].string
        score=infoList[7].string
        ulist.append([rank,univName,score])


def printUnivList(nlist):
    for num in nlist:
        print("{0:{3}^10}\t{1:{3}^10}\t{2:{3}^10}".format(num[0],num[1],num[2],chr(12288)))


def main():
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html'
    ulist=[['名次','学校','总分'],]
    html=getHTMLText(url)
    fillUnivList(ulist,html)
    printUnivList(ulist)

if __name__=='__main__':
    main()