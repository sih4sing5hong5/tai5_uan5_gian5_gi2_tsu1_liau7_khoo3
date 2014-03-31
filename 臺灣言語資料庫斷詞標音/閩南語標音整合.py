/# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
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
from 臺灣言語工具.字詞組集句章.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.斷詞.型音辭典 import 型音辭典
from 臺灣言語工具.字詞組集句章.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語資料庫.欄位資訊 import 文讀層
from 臺灣言語資料庫.欄位資訊 import 白話層
from 臺灣言語資料庫斷詞標音.揣辭典條目 import 揣辭典條目
from 臺灣言語工具.斷詞.動態規劃斷詞 import 動態規劃斷詞
from 臺灣言語工具.標音.語句連詞 import 語句連詞
from 臺灣言語工具.標音.動態規劃標音 import 動態規劃標音

class 閩南語標音整合:
	腔口 = '漢語族閩方言閩南語偏漳優勢音'
	條目 = 揣辭典條目()
	文讀層 = None
	白話層 = None
	粗胚 = 文章粗胚()
	分析器 = 拆文分析器()
	家私 = 轉物件音家私()
	教羅音標 = 教會羅馬字音標
	音標工具 = 臺灣閩南語羅馬字拼音

	辭條上大長度 = 4
	空 = '空'
	辭典 = None
	斷詞 = 動態規劃斷詞()
	連詞 = None
	標音 = 動態規劃標音()
	def __init__(self, 腔口, 辭典型態):
		self.腔口 = 腔口
		self.文讀字 = self.條目.揣言語層的字詞(self.腔口, 文讀層)
		self.白話字 = self.條目.揣言語層的字詞(self.腔口, 白話層)
		self.辭典 = 辭典型態(self.辭條上大長度)
		self.辭典.空 = self.空
		self.連詞 = 語句連詞(3)
		全部資料 = {}
		for 資料 in self.條目.揣腔口資料(腔口)[:]:
			# 處理減號
			文字資料 = 資料.文字.first()
			處理過的音標 = self.粗胚.建立物件語句前處理減號(self.音標工具, 文字資料.音標)
			# 愛加詞組無
			if 處理過的音標.strip() == '-':
				continue
			對齊組 = self.分析器.產生對齊組(文字資料.型體, 處理過的音標)
			組物件 = self.家私.轉做標準音標(self.音標工具, 對齊組)
			全部資料[資料.流水號] = (組物件, 資料.結果)
		for 流水號, 內容 in 全部資料.items():
			組物件, 結果 = 內容
			for 詞物件 in 組物件.內底詞:
				詞物件.屬性 = {'流水號':流水號}
				if 資料.流水號 in self.文讀字:
					詞物件.屬性[文讀層] = 1
				elif 資料.流水號 in self.白話字:
					詞物件.屬性[白話層] = 1
				if 結果 == None:
					self.辭典.加詞(詞物件)
			if 結果 == None:
				self.連詞.看(組物件)

	def 語句斷詞(self, 語句):
		處理過的語句 = self.粗胚.建立物件語句前處理減號(self.音標工具, 語句)
		章物件 = self.分析器.建立章物件(處理過的語句)
		return self.物件斷詞(章物件)

	def 物件斷詞(self, 物件):
# 		轉教羅物件 = self.家私.轉做標準音標(self.教羅音標, 物件)
		正規物件 = self.家私.轉做標準音標(self.音標工具, 物件)
		斷詞了物件 = self.斷詞.斷詞(self.辭典, 正規物件)
		return 斷詞了物件

	def 語句斷詞標音(self, 語句):
		處理過的語句 = self.粗胚.建立物件語句前處理減號(self.音標工具, 語句)
		章物件 = self.分析器.建立章物件(處理過的語句)
		return self.物件斷詞標音(章物件)

	def 物件斷詞標音(self, 物件):
# 		轉教羅物件 = self.家私.轉做標準音標(self.教羅音標, 物件)
		正規物件 = self.家私.轉做標準音標(self.音標工具, 物件)
		斷詞了物件 = self.斷詞.斷詞(self.辭典, 正規物件)
		標音了物件 = self.標音.標音(self.連詞, 斷詞了物件)[0]
		return 標音了物件

if __name__ == '__main__':
	標音 = 閩南語標音整合('漢語族閩方言閩南語偏漳腔', 型音辭典)
	音 = 標音.語句斷詞標音('台語字')
	print(音)
	音 = 標音.語句斷詞標音('台語字')
	print(音)
	音 = 標音.語句斷詞標音('台語字')
	print(音)
	音 = 標音.語句斷詞標音('白日依山盡')
	print(音)
	音 = 標音.語句斷詞標音('點仔膠')
	print(音)
	音 = 標音.語句斷詞標音('好好鱟刣甲屎那流。')
	print(音)
	音 = 標音.語句斷詞標音('好好鱟刣甲屎那流,')
	print(音)
	音 = 標音.語句斷詞標音('好好鱟,刣甲屎那流')
	print(音)
	音 = 標音.語句斷詞標音('好好鱟13245刣甲屎0800-092000那流')
	print(音)

