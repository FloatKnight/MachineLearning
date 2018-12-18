#封装
import requests
import json
from lxml import etree
import pymongo
from requests import exceptions

class Spider_Kit:
    '''
        爬虫工具:
        getProxy()  获取一个代理
        
    '''
    def __init__(self):
        '''
            Spider_Kit的构造方法
        '''
        self.__proxies = self.proxy_pool()


    def getProxy(self):
        '''
            获取一个代理
        '''
        return self.__proxies.__next__()

    def proxy_pool(self):
        '''
            通过.__next__()  可以获得一个proxy
        '''

        #设置请求头
        headers= {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
        #初始化代理
        proxies = None
        #根地址
        root_url = 'https://www.kuaidaili.com/free/inha/'
        #开始页面
        start_page = 1

        page = start_page  #初始化搜索页面
        datas = list()     #保存爬取到的数据

        while True:
            to_url = root_url+str(page)+'/'

            try:
                html = requests.request(method='GET',url=to_url,headers=headers,proxies=proxies,timeout = 3)
            except BaseException as e:
                #移除无用代理
                print(e)
                if len(datas) > 8:
                    del datas[7]
                elif len(datas) > 2:
                    del datas[0]
                proxies = datas[7] if len(datas)>7 else datas[0] if len(datas)>0 else None
                continue
            #已经爬到最后一页,重新从第一页开始爬
            if html.text == 'page error':
                page=start_page
                continue
            if html.status_code == 200:
                res = etree.HTML(html.text)

                ips = res.xpath('//*[@data-title="IP"]/text()')
                ports = res.xpath('//*[@data-title="PORT"]/text()')
                types = res.xpath('//*[@data-title="类型"]/text()')
                datas = [{item[2].lower():item[0]+':'+item[1]} for item in zip(ips,ports,types) ]

                #选择第七个作为代理继续爬取
                proxies = datas[7] if len(datas)>7 else datas[0] if len(datas)>0 else None
                page+=1
            #  generator 
            for i in datas:
                yield i
