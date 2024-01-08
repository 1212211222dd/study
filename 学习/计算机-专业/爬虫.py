# import urllib.request
# #1)获取响应对象
# response = urllib.request.urlopen('http://www.baidu.com/')
# #urlopen()向URL发请求,返回响应对象,,注意返回的是一个对象.
# print(response)
# #输出结果是:<http.client.HTTPResponse object at 0x032F0F90>
# #2)输出HTML信息
# html = response.read().decode('utf-8')
# #read方法用于提取HTML信息.该方法返回的结果是字符串类型(bytes),因此需要decode()转换为字符串
# print(html)
import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode()
print(html)