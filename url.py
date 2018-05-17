# -*- coding: UTF-8 -*-
import urllib2

url="http://www.baidu.com"
ua_headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}

#通过urllib2.Request()方法构造一个请求对象
request = urllib2.Request(url,headers = ua_headers)

#向指定的url地址发送请求，并发布会服务器响应的类文件对象
page = urllib2.urlopen(request)
#读取文件内容返回字符串
html=page.read()

#返回服务器响应码
print(page.getcode())



#print(html)