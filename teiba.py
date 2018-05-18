# -*- coding: UTF-8 -*-
import urllib2
import urllib
import random


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





def load_page(fullurl, file_name):
    '''
    进行页面操作
    fulluel:操作url
    file_name:需要保存的文件名
    '''
    print("正在下载 " + file_name)
    request = urllib2.Request(fullurl)
    request.add_header("User-Agent", user_agent())
    response = urllib2.urlopen(request)
    return response.read()

def save_page(html, file_name):
    '''
    保存爬取到的页面
    html:爬取的页面内容
    file_name:保存到的页面
    '''
    print("正在保存 " + file_name)
    with open(file_name, "w") as f:
        f.write(html)
    print("-" * 20)


def tieba_spider(url, key_word, sta_page, end_page):
    '''
    处理页面url
    url：url通用部分
    sta_page:起始页
    end_page:结束页

    '''
    for x in range(sta_page, end_page + 1):
        pn = str((x - 1) * 50)
        kw = urllib.urlencode({"kw":key_word})
        fullurl = url + "?" + kw + "&pn=" + pn
        print(fullurl)
        file_name = "第" + str(x) + "页.html"
        #print(file_name)
        html = load_page(fullurl, file_name)
        save_page(html, file_name)

def main():
    url = "http://tieba.baidu.com/f"
    key_word = raw_input("需要访问的贴吧：")
    start_page = int(raw_input("起始页："))
    end_page = int(raw_input("结束页："))
    tieba_spider(url, key_word, start_page, end_page)


if __name__ == '__main__':
    main()

