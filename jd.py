import urllib.request
import urllib.parse
import json
import time

url = 'http://forecast.weather.com.cn/napi/h5map/city/101/jQuery1536389177899'

header =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'method': 'GET'}
req = urllib.request.Request(url, headers = header)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')[20:-1]
text = json.loads(html)
result = text['result']
print(result['北京'])
time.sleep(20)
