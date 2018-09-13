import urllib.request
import urllib.parse
import json
import time
from trans import __translate
'''
list = ['af	南非语 ar	阿拉伯语 az	阿塞拜疆语',
'be	比利时语 bg	保加利亚语 ',
'ca	加泰隆语 cs	捷克语 cy	威尔士语 ',
'da	丹麦语 de	德语 dv	第维埃语 ',
'el	希腊语 en	英语 eo	世界语 es	西班牙语 et	爱沙尼亚语 eu	巴士克语 ',
'fa	法斯语 fi	芬兰语 fo	法罗语 fr	法语 ',
'gl	加里西亚语 gu	古吉拉特语 ',
'he	希伯来语 hi	印地语 hr	克罗地亚语 hu	匈牙利语 hy	亚美尼亚语 ',
'id	印度尼西亚语 is	冰岛语 it	意大利语 ',
'ja	日语 ',
'ka	格鲁吉亚语 kk	哈萨克语 kn	卡纳拉语 ko	朝鲜语 kok	孔卡尼语 ky	吉尔吉斯语 ',
'lt	立陶宛语 lv	拉脱维亚语 ',
'mi	毛利语 mk	马其顿语 mn	蒙古语 mr	马拉地语 ms	马来语 mt	马耳他语 ',
'nb	挪威语(伯克梅尔) nl	荷兰语 ns	北梭托语 ',
'pa	旁遮普语 pl	波兰语 pt	葡萄牙语 qu	克丘亚语 ',
'ro	罗马尼亚语 ru	俄语 ',
'sa	梵文 se	北萨摩斯语 sk	斯洛伐克语 sl	斯洛文尼亚语 sq	阿尔巴尼亚语 sv	瑞典语 sw	斯瓦希里语 syr	叙利亚语 ',
'ta	泰米尔语 te	泰卢固语 th	泰语 tl	塔加路语 tn	茨瓦纳语 tr	土耳其语 ts	宗加语 tt	鞑靼语 ',
'uk	乌克兰语 ur  乌都语 uz	乌兹别克语 ',
'vi	越南语 ',
'xh	班图语 ',
'zh-CN	中文(简体) zh-TW	中文(繁体) zu	祖鲁语 ']
'''
list =['auto 自动检测   zh 中文	 en 英语','yue  粤语	   wyw 文言文	jp 日语	kor 韩语','fra  法语	   spa 西班牙语   th 泰语	ara 阿拉伯语',
'ru   俄语	   pt 葡萄牙语	de 德语	it 意大利语','el   希腊语	 nl 荷兰语	pl 波兰语	bul 保加利亚语','est  爱沙尼亚语 dan 丹麦语   fin 芬兰语',
'cs   捷克语	 rom 罗马尼亚语	slo 斯洛文尼亚语','swe  瑞典语	 hu 匈牙利语	cht 繁体中文	vie 越南语']
'''
list2 = ['af','ar','az','be','bg','ca','cs','cy','da','de','dv','el','en','eo','es','et','eu','fa','fi','fo','fr','gl','gu','he','hi','hr','hu','hy',
'id','is','it','ja','ka','kk','kn','ko','kok','ky','lt','lv','mi','mk','mn','mr','ms','mt','nb','nl','ns','pa','pl','pt','qu','ro','ru',
'sa','se','sk','sl','sq','sv','sw','syr','ta','te','th','tl','tn','tr','ts','tt','uk','ur','uz','vi','xh','zh-CN','zh-TW','zu']
'''
list2 = ['auto','zh','en','yue','wyw','jp','kor','fra','spa','th','ara','ru','pt','de','it','el','nl','pl',
'bul','est','dan','fin','cs','rom','slo','swe','hu','cht','vie']
def show_list():
	for x in list:
		print(x)
def check(code):
	if code in list2:
		return True
	else :
		return False
	
while True:
	flog = False
	show_list()
	print('\n-----translate from baidu!-----\n')
	print('请按列表选择要翻译的语言代码：')
	while not flog:
		lin = input('从：(auto为自动)')
		flog = check(lin)
		if not flog:
			print('请输入正确的代码！')
	flog = False
	while not flog:
		lout = input('翻译到：')
		flog = check(lout)
		if not flog:
			print('请输入正确的代码！')
	else:
		print('-----文本处输入/q退出-----')
		print('-----输入/t退回选择语言-----')
	while True:
		text = input('\n请输入需要翻译的文本:')
		if text == r'/q':
			print('程序将在5s后关闭')
			for x in range(1,5):
				time.sleep(1)
				print('%s s'% str(5-x))
			time.sleep(1)
			exit()
		elif text == r'/t':
			break
		#print(text)
		fy = 'Baidu'
		results = __translate(lin, lout, fy,text)
		#print(html)
		print('\n翻译结果：')
		print(results)
		
		
	
