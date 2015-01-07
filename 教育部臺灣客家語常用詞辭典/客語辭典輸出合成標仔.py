# -*- coding: utf-8 -*-
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
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 教育部臺灣客家語常用詞辭典.客話辭典正規化 import 客話辭典正規化
from 教育部臺灣客家語常用詞辭典.調號處理 import 調號處理
from 臺灣言語工具.基本元素.公用變數 import 分詞符號

class 客語辭典整理腔調資料():
	辭典正規化 = 客話辭典正規化()
	_分析器 = 拆文分析器()
	_轉音家私 = 轉物件音家私()
	_譀鏡 = 物件譀鏡()
	def 轉(self, 詞目, 四縣音, 海陸音, 大埔音, 饒平音, 詔安音):
		調號 = 調號處理()
		def 初使音標(self, 音):
			self.音 = 音
		def 標準音標(self):
			return 調號.數字轉調號(self.音, self.腔)
		結果={}
		for 音標, 腔 in [(四縣音, '四縣腔'),
				 (海陸音, '海陸腔'), (大埔音, '大埔腔'),  # 粵臺片
				(饒平音, '饒平腔'), (詔安音, '詔安腔')
				]:
			新音 = self.辭典正規化.處理音標頭前字佮加空白(音標)
			if 新音!='':
				新詞目, 新音 = self.辭典正規化.調整錯誤的詞條(詞目, 新音)
# 				print(新詞目, 新音)
# 				句物件 = self._分析器.產生對齊句(新詞目, 新音) #愛去校對辭典
				句物件 = self._分析器.產生對齊句(新音, 新音)
				腔型 = type('腔', (object,), {'__init__' : 初使音標, '腔':腔, '標準音標' :標準音標})
				新句物件 = self._轉音家私.轉音(腔型, 句物件)
				型 = self._譀鏡.看型(新句物件)
				音 = self._譀鏡.看音(新句物件, 物件分字符號=分詞符號)
# 				print(型, 音)
				結果[腔+'型']=型
				結果[腔+'音']=音
		return 結果
