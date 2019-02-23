from django.shortcuts import render

from django.http import HttpResponse

import requests
from pprint import pprint

# スクレイピングに必要なライブラリ
from bs4 import BeautifulSoup
#from urllib import request
import urllib.request
from lxml import html
import pandas as pd


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def girls_channel(request):
    
    # ヤフーのスクレイピング
    """
    r = requests.get('https://news.yahoo.co.jp')
    print(r.headers)
    print("--------")
    print(r.encoding)
    print(r.content)

    result = []
    #result.append(r.headers)
    #result.append(r.encoding)
    result.append(r.content)
    
    path_w = '/vagrant/feed_commenter_new/test_w.txt'

    #s = 'New file'

    for val in result:
        print(type(val))
        with open(path_w, mode='w') as f:
            f.write(val)

    """





    

    """
    with open(path_w) as f:
        print(f.read())
    """

    """
    html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"
    soup = BeautifulSoup(html, "html.parser")
    print(soup.select("h1"))
    """

    """
    r = requests.get("https://news.yahoo.co.jp/")
    soup = BeautifulSoup(r.content, "html.parser")
    
    
    with open("hoge.txt", "w") as f:
        pprint(soup, stream=f)

    result = {
        #'result1': soup.find("div",id="tpc_maj"),
        'result2': soup.find("div",id="tpc_maj").text,
    }
    """

    # beautifulsoupを使ってスクレイピング
    """
    girl_channel = requests.get("https://girlschannel.net/")
    girl_channel = BeautifulSoup(girl_channel.content, "html.parser")
    
    
    with open("hoge.txt", "w") as f:
        pprint(girl_channel, stream=f)
    """


    # Xpathで取得してみる
    test_url = "http://www.example.com/"
    girl_url = "https://girlschannel.net/"
    mixi_url = "https://news.mixi.jp/?from=l_navi"
    #req = request.Request(girl_url)
    req = urllib.request.Request(girl_url)
    with urllib.request.urlopen(req) as res:
        girl_html = res.read()

    req = urllib.request.Request(mixi_url)
    with urllib.request.urlopen(req) as res:
        mixi_html = res.read()

    #girl_channel = request.urlopen(req)
    #raw_html = girl_channel.read()
    
    dom_girlchan = html.fromstring(str(girl_html))
    path_string = '/*'
    path_string = '/html/head/title'
    #link = html_info.xpath("/html/body/div[1]/div[1]/div[1]/ul[1]/li[1]/a")
    link = dom_girlchan.xpath(path_string)


    print('path_string')
    pprint(path_string)
    print('dom_girlchan')
    pprint(dom_girlchan)
    print('link:')
    pprint(link)

    res_girl = []
    for o2 in dom_girlchan.xpath(path_string): #xxxの部分をテキスト指定でhrefを取得
        res_girl.append(o2) 

    print('res_girl:')
    pprint(res_girl)

    dom_mixi = html.fromstring(str(mixi_html))
    path_string = '/*'
    path_string = '//*[@id="bodyMainArea"]/div[4]/div[1]/div[2]/ul/li[6]/a'
    #link = html_info.xpath("/html/body/div[1]/div[1]/div[1]/ul[1]/li[1]/a")
    link = dom_mixi.xpath(path_string)


    print('path_string')
    pprint(path_string)
    print('dom_mixi')
    pprint(dom_mixi)
    print('link:')
    pprint(link)

    res_mixi = []
    for o2 in dom_mixi.xpath(path_string): #xxxの部分をテキスト指定でhrefを取得
        res_mixi.append(o2) 

    print('res_mixi:')
    pprint(res_mixi)


    df = pd.DataFrame({"res_mixi":res_mixi})
    print('dataframe:')
    pprint(df)

    print('window_info:link,html_info')

    result = {
        #'result1': soup.find("div",id="tpc_maj"),
        #'result2': girl_channel.find("div",id="tpc_maj").text,
        'result1': link,
        'result2': dom_mixi
    }

    #return HttpResponse('girlchannel_test')
    return render(request, 'index.html', result)


