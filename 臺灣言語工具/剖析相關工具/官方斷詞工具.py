"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import re

class 官方斷詞工具:
	檢查結果 = re.compile('<result>(.*)</result>')
	分句 = re.compile('<sentence>(.*?)</sentence>')
	分詞性 = re.compile('(.*)\((.*)\)')
	回傳狀況 = re.compile('<processstatus code="\d">(.*?)</processstatus>')
	def 斷詞(self, 語句, 主機='140.109.19.104', 連接埠=1501, 帳號='ihcaoe', 密碼='aip1614'):
		連線 = socket(
			AF_INET, SOCK_STREAM)
		連線.connect((主機, 連接埠))
		
		資料 = self.傳去格式頭前.format('UTF-8', 帳號, 密碼).replace('\n', '').encode('UTF-8')\
			+ 語句.encode('UTF-8')\
			+ self.傳去格式後壁.encode('UTF-8')
# 		資料 = self.傳去格式.format('UTF-8',帳號, 密碼,語句).replace('\n', '').encode('UTF-8')

		已經送出去 = 0
		while 已經送出去 < len(資料):
			這擺送出去 = 連線.send(資料[已經送出去:])
			if 這擺送出去 == 0:
				raise RuntimeError("連線出問題")
			已經送出去 += 這擺送出去

		全部收著資料 = b''
		走 = True
		while 走:
			這擺收著資料 = 連線.recv(1024)
			if 這擺收著資料 == b'':
				raise RuntimeError("連線出問題")
			全部收著資料 = 全部收著資料 + 這擺收著資料
# 			print(re.search(b'</wordsegmentation>' ,全部收著資料))
			if b'</wordsegmentation>' in 全部收著資料:
				走 = False
		連線.close()
		全部收著字串 = 全部收著資料.decode('UTF-8')
		收著結果 = self.檢查結果.search(全部收著字串)
		結果 = []
		if 收著結果 != None:
			逐逝 = self.分句.split(收著結果.group(1))[1::2]
			for 一逝 in 逐逝:
				逝結果 = []
				for 詞 in 一逝.split('　'):
					if 詞 == '':
						continue
					字, 性 = self.分詞性.split(詞)[1:3]
					逝結果.append((字, 性))
				結果.append(逝結果)
			return 結果
		狀況 = self.回傳狀況.split(全部收著字串)
		if 狀況 != None:
# 			<processstatus code="1">Service internal error</processstatus>
# 			<processstatus code="2">XML format error</processstatus>
# 			<processstatus code="3">Authentication failed</processstatus> 
			raise RuntimeError(狀況[1])
		raise RuntimeError('回傳的資料有問題！！')
	傳去格式頭前 = '''
<?xml version="1.0" ?>
<wordsegmentation version="0.1" charsetcode='{}' >
<option showcategory="1" />
<authentication username="{}" password="{}" />
<text>'''
	傳去格式後壁 = '''</text>
</wordsegmentation>
'''
	傳去格式 = '''
<?xml version="1.0" ?>
<wordsegmentation version="0.1" charsetcode='{}' >
<option showcategory="1" />
<authentication username="{}" password="{}" />
<text>{}</text>
</wordsegmentation>
'''

if __name__ == '__main__':
	斷詞工具 = 官方斷詞工具()
	print(斷詞工具.斷詞('我想吃飯。我想吃很多飯。'))
	print(斷詞工具.斷詞('我想吃飯。我想吃很多飯>。'))
	print(斷詞工具.斷詞('我想) :>'))
