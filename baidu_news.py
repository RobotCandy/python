# coding: utf-8
import  bs4
from bs4 import BeautifulSoup as soup
import urllib2

def news():
    my_url = "http://news.baidu.com/"
    url = urllib2.Request(my_url)
    Client = urllib2.urlopen(url)

    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, 'lxml')
    # 头6条新闻
    for i in range(0,6):
        news_list = soup_page.findAll("li",{"class":"hdline%d" %i})
        for news in news_list:
            news_a = news.find('a')
            print news_a.text
            print news_a['href']
    # 醒目的新闻
    #news_list = soup_page.findAll("li",{"class":"bold-item"})
    #for news in news_list:
    #    news_a = news.find('a')
    #    print news_a.text
    #    print news_a['href']
    #for news in news_list:
    #    print(news.title.text)
    #    print(news.link.text)
    #    print(news.pubDate.text)
    #    print("-"*150)

news()
