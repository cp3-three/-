import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "


def getFundList(lst, fundURL,num):
    for i in range(1,num+1):
        url=fundURL+str(i)+",200"
        html = getHTMLText(url)
        lst.extend(re.findall(r'\d{6}',html))

def getFundInofo(lst, fundURL, fpath):
    count = 0
    for fund in lst:
        url = fundURL + fund + ".html"
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            fundInfo = soup.find('div', attrs={'class': "merchandiseDetail"})
            name = fundInfo.find_all(attrs={'class': "fundDetail-tit"})[0]
            infoDict.update({'基金名称': name.text.split()[0]})

            keyList = fundInfo.find_all("dt")
            valueList = fundInfo.find_all("dd")
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count=count+1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)),end="")   #\r可实现每次将打印移至行首开始
        except:
            traceback.print_exc()  # 获得错误信息
            print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst)), end="")
            continue


def main():
    fund_list_url = "https://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&page="
    num=2     #由于每页只有200个股票ID，故可设置页数
    fund_info_url = "https://fund.eastmoney.com/"
    output_file = r'C:\Users\杨忠如\Desktop\学习笔记\爬虫代码实例\Fundinfo.txt'
    slist = []
    getFundList(slist, fund_list_url,num)

    getFundInofo(slist, fund_info_url, output_file)


if __name__ == '__main__':
    main()