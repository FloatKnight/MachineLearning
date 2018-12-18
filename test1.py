import urllib.request

response = urllib.request.urlopen('https://www.baidu.com')

#查看返回的类型
print( type(response) )  #response 是一个对象

#response 是一个 HTTPResponse类型的对象，包含read(),readinto(),getheader(name) getheaders(),
#还有  msg，version ，status,reason, degublevel, closed等属性

print('http相应状态码:',response.status)
print('http响应的http信息',response.getheaders())
print('开始')
print(response.getheaders('Server'))
print('结束')