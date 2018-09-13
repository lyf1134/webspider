import urllib.request
import urllib.parse
import random
import hashlib
from gtk import *

def __translate(lin, lout, fy, text):
	if text == '':
		return ''
	if fy == 'Baidu':
		lin = list_b2[lin]
		lout = list_b2[lout]
		url = 'http://fanyi.baidu.com/transapi'
		data = {"query": text, 'from': lin, 'to': lout}
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'method': 'POST'}
		data = urllib.parse.urlencode(data).encode('utf-8')
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		html = response.read().decode('utf-8')
	elif fy == 'Google':
		lin = list_g2[lin]
		lout = list_g2[lout]
		url = 'https://translate.google.cn/translate_a/single'
		data = {"q": text}
		params = {'client': 't', 'sl': lin, 'tl': lout, 'hl': 'en','dt': 'at', 'dt': 'bd', 'dt': 'ex', 'dt': 'ld', 'dt': 'md','dt': 'qca', 'dt': 'rw', 'dt': 'rm', 'dt': 'ss', 'dt': 't','ie': 'UTF-8', 'oe': 'UTF-8', 'source': 'bh', 'ssel': '0','tsel': '0', 'kc': '1', 'tk': ''}
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36','Referer': 'https://translate.google.cn/'}
		params['tk'] = TK.get_tk(text)
		#data = urllib.parse.urlencode(data).encode('utf-8')
		res = requests.post(url, headers = headers, data = data, params = params)
		#res.raise_for_status()
		html = res.text
		print(html)
	else: 
		lin = list_y2[lin]
		lout = list_y2[lout]
		#print(lin,lout)
		url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
		# 发送给有道服务器的数据
		u = 'fanyideskweb'
		f = str(int(time.time()*1000) + random.randint(1,10))
		c = 'ebSeFb%=XZ%T[KZ)c(sy!'
		sign = hashlib.md5((u + text + f + c).encode('utf-8')).hexdigest()
		data = {'i': text,'from':lin,'to':lout,'salt': f, 'sign': sign,'client': u, 'doctype': 'json','keyfrom': 'fanyi.web'}
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'method': 'POST','Referer': 'http://fanyi.youdao.com/',}
		data = urllib.parse.urlencode(data).encode('utf-8')
		req = urllib.request.Request(url, data, headers)	
		response = urllib.request.urlopen(req)
		html = response.read().decode('utf-8')
	if fy == 'Baidu':
		return json.loads(html)['data'][0]['dst']
	elif fy == 'Google':
		return json.loads(html)[0][0][0]
	else: 
		#print(json.loads(html))
		return json.loads(html)['translateResult'][0][0]['tgt']
		
TK = CalcTk()

list_b1 =['中文','英语','粤语','文言文','日语','韩语','法语','西班牙语','泰语','阿拉伯语',
'俄语','葡萄牙语','德语','意大利语','希腊语','荷兰语','波兰语','保加利亚语','爱沙尼亚语','丹麦语','芬兰语',
'捷克语','罗马尼亚语','斯洛语尼亚语','瑞典语','匈牙利语','繁体中文','越南语']

list_b2 = {'auto':'auto','中文':'zh','英语':'en','粤语':'yue','文言文':'wyw','日语':'jp','韩语':'kor','法语':'fra','西班牙语':'spa','泰语':'th','阿拉伯语':'ara',
'俄语':'ru','葡萄牙语':'pt','德语':'de','意大利语':'it','希腊语':'el','荷兰语':'nl','波兰语':'pl','保加利亚语':'bul','爱沙尼亚语':'est',
'丹麦语':'dan','芬兰语':'fin','捷克语':'cs','罗马尼亚语':'rom','斯洛语尼亚语':'slo','瑞典语':'swe','匈牙利语':'hu','繁体中文':'cht','越南语':'vie'}

list_y1 = ['中文','日语','英语','韩语','法语','阿拉伯语','波兰语','丹麦语','德语','俄语','芬兰语',
'荷兰语','捷克语','罗马尼亚语','挪威语','葡萄牙语','瑞典语','斯洛伐克语','西班牙语','印地语',
'印度尼西亚语','意大利语','泰语','土耳其语','希腊语','匈牙利语']

list_y2 ={'auto':'auto','中文':'zh-CHS','日语':'ja','英语':'EN','韩语':'ko','法语':'fr','阿拉伯语':'ar','波兰语':'pl','丹麦语':'da','德语':'de','俄语':'ru','芬兰语':'fi',
'荷兰语':'nl','捷克语':'cs','罗马尼亚语':'ro','挪威语':'no','葡萄牙语':'pt','瑞典语':'sv','斯洛伐克语':'sk','西班牙语':'es','印地语':'hi',
'印度尼西亚语':'id','意大利语':'it','泰语':'th','土耳其语':'tr','希腊语':'el','匈牙利语':'hu'}

list_g1 = ['中文','中文(简体)','中文(繁体)','英语','南非语','俄语','法语','阿拉伯语','意大利语','日语','丹麦语','德语',
'希腊语','世界语','西班牙语','爱沙尼亚语','巴士克语','法斯语','芬兰语','法罗语','加里西亚语','古吉拉特语','阿塞拜疆语','比利时语','保加利亚语','加泰隆语','捷克语',
'希伯来语','印地语','克罗地亚语','匈牙利语','亚美尼亚语','印度尼西亚语','冰岛语','格鲁吉亚语','哈萨克语','卡纳拉语','朝鲜语','孔卡尼语','吉尔吉斯语',
'立陶宛语','拉脱维亚语','毛利语','马其顿语','蒙古语','马拉地语','马来语','马耳他语','挪威语','荷兰语','北梭托语','威尔士语','第维埃语',
'旁遮普语','波兰语','葡萄牙语','克丘亚语','罗马尼亚语','梵文','北萨摩斯语','斯洛伐克语','斯洛文尼亚语','阿尔巴尼亚语','瑞典语','斯瓦希里语','叙利亚语',
'泰米尔语','泰卢固语','泰语','塔加路语','茨瓦纳语','土耳其语','宗加语','鞑靼语','乌克兰语','乌都语','乌兹别克语','越南语',
'班图语','祖鲁语']
list_g2 = {'auto':'auto','南非语':'af','阿拉伯语':'ar','阿塞拜疆语':'az','比利时语':'be','保加利亚语':'bg','加泰隆语':'ca','捷克语':'cs','威尔士语':'cy','丹麦语':'da','德语':'de','第维埃语':'dv',
'希腊语':'el','英语':'en','世界语':'eo','西班牙语':'es','爱沙尼亚语':'et','巴士克语':'eu','法斯语':'fa','芬兰语':'fi','法罗语':'fo','法语':'fr','加里西亚语':'gl','古吉拉特语':'gu',
'希伯来语':'he','印地语':'hi','克罗地亚语':'hr','匈牙利语':'hu','亚美尼亚语':'hy','印度尼西亚语':'id','冰岛语':'is','意大利语':'it','日语':'ja','格鲁吉亚语':'ka','哈萨克语':'kk','卡纳拉语':'kn','朝鲜语':'ko','孔卡尼语':'kok','吉尔吉斯语':'ky',
'立陶宛语':'lt','拉脱维亚语':'lv','毛利语':'mi','马其顿语':'mk','蒙古语':'mn','马拉地语':'mr','马来语':'ms','马耳他语':'mt','挪威语':'nb','荷兰语':'nl','北梭托语':'ns',
'旁遮普语':'pa','波兰语':'pl','葡萄牙语':'pt','克丘亚语':'qu','罗马尼亚语':'ro','俄语':'ru','梵文':'sa','北萨摩斯语':'se','斯洛伐克语':'sk','斯洛文尼亚语':'sl','阿尔巴尼亚语':'sq','瑞典语':'sv','斯瓦希里语':'sw','叙利亚语':'syr',
'泰米尔语':'ta','泰卢固语':'te','泰语':'th','塔加路语':'tl','茨瓦纳语':'tn','土耳其语':'tr','宗加语':'ts','鞑靼语':'tt','乌克兰语':'uk','乌都语':'ur','乌兹别克语':'uz','越南语':'vi',
'班图语':'xh','中文':'zh','中文(简体)':'zh-CN','中文(繁体)':'zh-TW','祖鲁语':'zu'}
