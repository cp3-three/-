"""
coding=utf-8
author yang
data 2020/7/12
desc 一个进行爬取淘宝商品的定向爬虫，爬出价格
"""
import requests
import re

def getHTMLText(url,headers):

    try:
        HTML=requests.get(url,headers=headers)
        HTML.raise_for_status()
        HTML.encoding=HTML.apparent_encoding
        return HTML.text
    except:
        print("爬取失败！")
        return ''

def getPriceList(priceList,HTML):
    plt = re.findall(r'\"view_price\":\"[\d\.]*\"', HTML)
    nlt=re.findall(r'\"raw_title\":\".*?\"', HTML)
    length=len(priceList)
    for i in range(len(plt)):
        price=eval(plt[i].split(':')[1])
        name=eval(nlt[i].split(':')[1])
        priceList.append([i+length,price,name])

def printGoodPrice(priceList):

    for i in range(len(priceList)):
        good=priceList[i]
        print("{0:^10}\t{1:^10}\t{2:{3}^20}".format(good[0],good[1],good[2],chr(12288)))



def main():
    goods="书包"      #表示爬取的商品名
    path="https://s.taobao.com/search?q="
    url=path+goods+'&s='
    priceList=[['次序','价格','商品名'],]      #用于存储商品名与价格
    HTMLNum=3       #表示要爬取的网页数量
    #由于淘宝自身的认证机制，故在爬虫必须带上Cookie，Cookie可先使用浏览器登录，然后搜索商品后，在搜索页面按F12打开开发者模式
    #在开发者模式中的网络（network）->s所有（all）-》点击第一条连接，其中的cookie选项就是，但应该显示原始数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "cna=idflFK+5zUECAWoGekxcEi3r; tg=0; miid=1260983732869087931; enc=otJjm53g9eF%2B0xnr5%2FzycA4H52mLZo7Oa1wUq45Bko5KlhgbCwBGsoLF0SPzOVoGONa3GL2yOXs0iFL3DCxNNA%3D%3D; thw=cn; t=1eda68531bebfb4d9021c181bf7b7fce; isg=BEREO5Erxz0GB3KZ7JFt7XfrFsI2XWjHntGxyF7kRo_SieRThm6UV3xrzaFRiqAf; l=eBI013MgQ5AeAZ0CBO5CFurza77t3Id44kPzaNbMiInca1uhNFstxNQq_L8Mldtfgt1LOety1OZeedLHR3fDjyLKQ3h2q_Jinxf..; cookie2=5dd0f6844e96bdc6fd898b5b3def52f1; _tb_token_=73b5533330e7a; hng=CN%7Czh-CN%7CCNY%7C156; _samesite_flag_=true; JSESSIONID=175CD852B8D340786E65E278017FDC63; tfstk=cdDNBOxu8dpZb528IRwVCnD4ceeOZT40P9rzsbE_z3seEWFhiNbYxN54YorqK5f..; sgcookie=EcoBK7xPjq6UJYfj13khC; unb=2635803528; uc1=pas=0&cookie14=UoTV6OSHa%2FXIuA%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&existShop=false&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D; uc3=lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dBxGPqAAN2i6THaS4%3D&nk2=2%2BHdVGhwJCY%3D&id2=UU6iea8QYh04bg%3D%3D; csg=5ff11556; lgc=%5Cu560E%5Cu560E%5Cu673A55; cookie17=UU6iea8QYh04bg%3D%3D; dnk=%5Cu560E%5Cu560E%5Cu673A55; skt=904edbf6ec704d5d; existShop=MTU5NDU0MDcyMA%3D%3D; uc4=nk4=0%402Y%2B%2FOzA3vJOtciBeaQrRCtunHQ%3D%3D&id4=0%40U2xvLYHmNEIrnpN%2F7CR8zVAKNPiw; tracknick=%5Cu560E%5Cu560E%5Cu673A55; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=58a; _nk_=%5Cu560E%5Cu560E%5Cu673A55; cookie1=BxoE1usZEhDaXKmgF2dZY1OEbcmeHw%2B09W1T3hQHF38%3D; alitrackid=login.taobao.com; lastalitrackid=login.taobao.com; mt=ci=35_1;v=0"
    }
    for i in range(HTMLNum):
        HTML=getHTMLText(url+str(i*44),headers)
        if(HTML==None):
            return -1
        getPriceList(priceList,HTML)

    printGoodPrice(priceList)

    return 0

if __name__=="__main__":
    main()

