import urllib.request
import urllib.parse

'''
测试data参数，用于传递参数值到服务器，注意，他的请求方式不是GET方式，而是POST方式
'''


data = bytes( urllib.parse.urlopen({'word':'zy','name':'张影','age':'20'}),encoding='UTF-8' )


