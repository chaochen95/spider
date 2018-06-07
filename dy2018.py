# -*- coding: UTF-8 -*-
import urllib2
import urllib
import random
import re
from lxml import etree

def user_agent():
    #反爬虫
    user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", 
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",  
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",  
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",  
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",  
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", 
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", 
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", 
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", 
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",  
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",  
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"  
           ]
    user_agent = random.choice(user_agent_list)
    return user_agent

class Spiderdy2018(object):
    """docstring for Spiderdy2018"""
    def __init__(self):
        super(Spiderdy2018, self).__init__()
        #self.arg = arg

    def load_page(self, page):
        if page == 1:
            url = "http://www.dy2018.com/html/gndy/dyzz/index.html"
        else:
            url = "http://www.dy2018.com/html/gndy/dyzz/index_" + str(page) + ".html"

        request = urllib2.Request(url)
        request.add_header("User-Agent", user_agent())
        response = urllib2.urlopen(request)
        html = response.read()
        html = html.decode('GB2312', errors='ignore').encode('utf-8')
        #html = html.encode("utf8")
        #print(html)
        return html

    def deal_page(self, html):
        pattern = re.compile('<b>(.*?)</b>', re.S)
        m = pattern.findall(html)
        #print(m[0])
        for x in m:
            #print(x)
            pattern = re.compile('href="(.*?)"', re.S)
            pattern2 = re.compile('>(.*?)<', re.S)
            m2 = pattern.findall(x)
            m3 = pattern2.findall(x)
            m2 = "http://www.dy2018.com" + ''.join(m2)
            m3 = ''.join(m3)

            #提取下载地址
            url = m2
            request = urllib2.Request(url)
            request.add_header("User-Agent", user_agent())
            response = urllib2.urlopen(request)
            html = response.read().decode('GB2312', errors='ignore').encode('utf-8')            
            content = etree.HTML(html)
            link_list = content.xpath('//a[@target="_self"]/@thunderhref')
            

            
            list1 = [m3, m2]
            list2 = list1.extend(link_list)
            for x in list1:
                print(x)
            print("-"*30)
            #m3.append(m2)
            #print(m3)
            #print (json.dumps.(m3).decode("unicode-escape"))
            #dic = zip(m3, m2)
            #print(dic)
    def start(self, page):
        html = self.load_page(page)
        self.deal_page(html)

def main():
    spider = Spiderdy2018()
    page = input("需要爬取的页码：")
    spider.start(page)

if __name__ == '__main__':
    main()