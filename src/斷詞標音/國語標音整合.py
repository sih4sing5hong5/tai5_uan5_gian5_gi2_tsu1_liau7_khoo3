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
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 斷詞標音.動態規劃斷詞標音 import 動態規劃斷詞標音
from 字詞組集句章.基本元素.公用變數 import 分詞符號
from 字詞組集句章.基本元素.公用變數 import 分字符號
from 斷詞標音.資料庫揣辭典條目 import 資料庫揣辭典條目
from 資料庫.欄位資訊 import 國語臺員腔
from 斷詞標音.現掀辭典 import 現掀辭典
from 字詞組集句章.音標系統.國語.國語注音符號 import 國語注音符號
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私

class 國語標音整合:
	腔口 = 國語臺員腔
	條目 = 資料庫揣辭典條目()
	文讀層 = None
	白話層 = None
	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	家私 = 轉物件音家私()
	音標工具 = 國語注音符號

	辭典 = None
	斷詞標音 = 動態規劃斷詞標音()
	辭條上大長度 = 4
	def __init__(self, 腔口, 辭典):
		self.文讀層 = self.條目.文讀層
		self.白話層 = self.條目.白話層
		self.腔口 = 腔口
		self.文讀字 = set()
		[self.文讀字.add(字詞[0]) for 字詞 in self.條目.揣言語層的字詞(self.腔口, self.文讀層)]
		self.白話字 = set()
		[self.白話字.add(字詞[0]) for 字詞 in self.條目.揣言語層的字詞(self.腔口, self.白話層)]
		self.辭典 = 辭典(self.辭條上大長度)

		for 流水號, 型體, 音標 in self.條目.揣腔口字詞資料(腔口):
			# 目前為著臺語佮客話會當斷詞，予國語無音標的入來
			if 型體 == None or len(型體) > self.辭條上大長度 or len(型體) == 0:  # or 音標 == None:
				continue
			if 音標 != None:
				處理過的音標 = 音標.replace(分詞符號, 分字符號)
				詞物件 = self.分析器.產生對齊詞(型體, 處理過的音標)
			else:
				詞物件 = self.分析器.建立詞物件(型體)
			詞物件.屬性 = {'流水號':流水號}
			if 流水號 in self.文讀字:
				詞物件.屬性[self.文讀層] = 1
			elif 流水號 in self.白話字:
				詞物件.屬性[self.白話層] = 1
			self.辭典.加詞(詞物件)

	def 語句斷詞標音(self, 語句):
		處理過的語句 = self.初胚工具.建立物件語句前減號變標點符號(語句)
		章物件 = self.分析器.建立章物件(處理過的語句)
		return self.斷詞標音.斷詞標音(self.辭典, 章物件)

	def 物件斷詞標音(self, 物件):
		return self.斷詞標音.斷詞標音(self.辭典, 物件)

if __name__ == '__main__':
	標音 = 國語標音整合(國語臺員腔, 現掀辭典)
	音 = 標音.語句斷詞標音('台語字', 標音.文讀層)
	print(音)
	音 = 標音.語句斷詞標音('台語字', 標音.白話層)
	print(音)
	音 = 標音.語句斷詞標音('台語字', 標音.全部)
	print(音)
	音 = 標音.語句斷詞標音('白日依山盡', 標音.文讀層)
	print(音)
	音 = 標音.語句斷詞標音('點仔膠', 標音.文讀層)
	print(音)
	音 = 標音.語句斷詞標音('好好鱟刣甲屎那流。', 標音.文讀層)
	print(音)
	音 = 標音.語句斷詞標音('好好鱟刣甲屎那流,', 標音.文讀層)
	print(音)
	音 = 標音.語句斷詞標音('朝鮮', 標音.白話層)
	print(音)

