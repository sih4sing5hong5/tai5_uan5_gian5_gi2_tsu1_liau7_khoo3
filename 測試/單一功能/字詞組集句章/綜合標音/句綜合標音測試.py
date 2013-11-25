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
import unittest
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.綜合標音.句綜合標音 import 句綜合標音
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 字詞組集句章.綜合標音.集綜合標音 import 集綜合標音
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.綜合標音.詞組綜合標音 import 詞組綜合標音

class 句綜合標音測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.初胚工具 = 文章初胚工具()
	def tearDown(self):
		pass
	def test_基本測試(self):
		我 = self.分析器.產生對齊集('我', 'gua2')
		愛 = self.分析器.產生對齊集('愛', 'ai3')
		媠某 = self.分析器.產生對齊組('美女', 'sui2-boo2')
		美女 = self.分析器.產生對齊組('美女', 'mi2-lu2')
		莉 = 集([媠某, 美女])
		句物件 = 句([我, 愛, 莉])
		標音句 = 句綜合標音(閩南語字綜合標音, 句物件)
		self.assertEqual(len(標音句.綜合集), 3)
		self.assertEqual(len(標音句.綜合集[0].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[1].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[2].綜合詞組), 2)
		self.assertEqual(len(標音句.綜合集), 3)
		self.assertEqual(標音句.綜合集[0], 集綜合標音(閩南語字綜合標音, 我))
		self.assertEqual(標音句.綜合集[1], 集綜合標音(閩南語字綜合標音, 愛))
		self.assertEqual(標音句.綜合集[2], 集綜合標音(閩南語字綜合標音, 莉))
		self.assertEqual(標音句.轉json格式(),
			[[{'詞組綜合標音': [
				{"型體":"我", "臺羅數字調":"gua2", "臺羅閏號調":"guá", "通用數字調":"ghua4", "吳守禮方音":"⿳⿳⿳ㆣㄨㄚˋ"}],
			"連字音":"gua2"}],
			[{"詞組綜合標音":[
				{"型體":"愛", "臺羅數字調":"ai3", "臺羅閏號調":"ài", "通用數字調":"ai3", "吳守禮方音":"⿳ㄞ˪"}],
			"連字音":"ai3"}],
			[{"詞組綜合標音":[
				{"型體":"美", "臺羅數字調":"sui2", "臺羅閏號調":"suí", "通用數字調":"sui4", "吳守禮方音":"⿳⿳⿳ㄙㄨㄧˋ"},
				{"型體":"女", "臺羅數字調":"boo2", "臺羅閏號調":"bóo", "通用數字調":"bho4", "吳守禮方音":"⿳⿳ㆠㆦˋ"}],
			"連字音":"sui2-boo2"},
			{"詞組綜合標音":[
				{"型體":"美", "臺羅數字調":"mi2", "臺羅閏號調":"mí", "通用數字調":"mi4", "吳守禮方音":"⿳⿳ㄇㄧˋ"},
				{"型體":"女", "臺羅數字調":"lu2", "臺羅閏號調":"lú", "通用數字調":"lu4", "吳守禮方音":"⿳⿳ㄌㄨˋ"}],
			"連字音":"mi2-lu2"}],
			]
			)


	def test_一句無連字轉json格式(self):
		句物件 = self.分析器.產生對齊句('點仔膠，黏著跤，', 'tiam2 a2 ka1, liam5 tioh8 kha1,')
		標音句 = 句綜合標音(閩南語字綜合標音, 句物件)
		self.assertEqual(標音句.轉json格式(), [[{'詞組綜合標音': [
			{'通用數字調': 'diam4', '吳守禮方音': '⿳⿳⿳ㄉㄧㆰˋ', '臺羅閏號調': 'tiám', '臺羅數字調': 'tiam2', '型體': '點'},
			{'通用數字調': 'a4', '吳守禮方音': '⿳ㄚˋ', '臺羅閏號調': 'á', '臺羅數字調': 'a2', '型體': '仔'},
			{'通用數字調': 'ga1', '吳守禮方音': '⿳ㄍㄚ', '臺羅閏號調': 'ka', '臺羅數字調': 'ka1', '型體': '膠'},
			{'通用數字調': ',', '吳守禮方音': '', '臺羅閏號調': ',', '臺羅數字調': ',', '型體': '，'},
			{'通用數字調': 'liam5', '吳守禮方音': '⿳⿳⿳ㄌㄧㆰˊ', '臺羅閏號調': 'liâm', '臺羅數字調': 'liam5', '型體': '黏'},
			{'通用數字調': 'diorh6', '吳守禮方音': '⿳⿳⿳⿳ㄉㄧㄜ㆐ㆷ', '臺羅閏號調': 'tio̍h', '臺羅數字調': 'tioh8', '型體': '著'},
			{'通用數字調': 'ka1', '吳守禮方音': '⿳ㄎㄚ', '臺羅閏號調': 'kha', '臺羅數字調': 'kha1', '型體': '跤'},
			{'通用數字調': ',', '吳守禮方音': '', '臺羅閏號調': ',', '臺羅數字調': ',', '型體': '，'}
			], '連字音': 'tiam2 a2 ka1 , liam5 tioh8 kha1 ,'}]])

	def test_一句連字轉json格式(self):
		句物件 = self.分析器.產生對齊句('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
		標音句 = 句綜合標音(閩南語字綜合標音, 句物件)
		self.assertEqual(標音句.轉json格式(), [[{'詞組綜合標音': [
			{'通用數字調': 'diam4', '吳守禮方音': '⿳⿳⿳ㄉㄧㆰˋ', '臺羅閏號調': 'tiám', '臺羅數字調': 'tiam2', '型體': '點'},
			{'通用數字調': 'a4', '吳守禮方音': '⿳ㄚˋ', '臺羅閏號調': 'á', '臺羅數字調': 'a2', '型體': '仔'},
			{'通用數字調': 'ga1', '吳守禮方音': '⿳ㄍㄚ', '臺羅閏號調': 'ka', '臺羅數字調': 'ka1', '型體': '膠'},
			{'通用數字調': ',', '吳守禮方音': '', '臺羅閏號調': ',', '臺羅數字調': ',', '型體': '，'},
			{'通用數字調': 'liam5', '吳守禮方音': '⿳⿳⿳ㄌㄧㆰˊ', '臺羅閏號調': 'liâm', '臺羅數字調': 'liam5', '型體': '黏'},
			{'通用數字調': 'diorh6', '吳守禮方音': '⿳⿳⿳⿳ㄉㄧㄜ㆐ㆷ', '臺羅閏號調': 'tio̍h', '臺羅數字調': 'tioh8', '型體': '著'},
			{'通用數字調': 'ka1', '吳守禮方音': '⿳ㄎㄚ', '臺羅閏號調': 'kha', '臺羅數字調': 'kha1', '型體': '跤'},
			{'通用數字調': ',', '吳守禮方音': '', '臺羅閏號調': ',', '臺羅數字調': ',', '型體': '，'}
			], '連字音': 'tiam2-a2-ka1 , liam5-tioh8 kha1 ,'}]])

	def test_一句濟詞無連字轉json格式(self):
		句物件 = 句([
			self.分析器.產生對齊集('點', 'tiam2'),
			self.分析器.產生對齊集('仔', 'a2'),
			self.分析器.產生對齊集('膠', 'ka1'),
			self.分析器.產生對齊集('，', ','),
			self.分析器.產生對齊集('黏', 'liam5'),
			self.分析器.產生對齊集('著', 'tioh8'),
			self.分析器.產生對齊集('跤', 'kha1'),
			self.分析器.產生對齊集('，', ',')])
		標音句 = 句綜合標音(閩南語字綜合標音, 句物件)
		self.assertEqual(標音句.轉json格式(), [
			[{"詞組綜合標音":[
				{"型體":"點", "臺羅數字調":"tiam2", "臺羅閏號調":"tiám", "通用數字調":"diam4", "吳守禮方音":"⿳⿳⿳ㄉㄧㆰˋ"}],
			"連字音":"tiam2"}],
			[{"詞組綜合標音":[
				{"型體":"仔", "臺羅數字調":"a2", "臺羅閏號調":"á", "通用數字調":"a4", "吳守禮方音":"⿳ㄚˋ"}],
			"連字音":"a2"}],
			[{"詞組綜合標音":[
				{"型體":"膠", "臺羅數字調":"ka1", "臺羅閏號調":"ka", "通用數字調":"ga1", "吳守禮方音":"⿳ㄍㄚ"}],
			"連字音":"ka1"}],
			[{"詞組綜合標音":[
				{"型體":"，", "臺羅數字調":",", "臺羅閏號調":",", "通用數字調":",", "吳守禮方音":""}],
			"連字音":","}],
			[{"詞組綜合標音":[
				{"型體":"黏", "臺羅數字調":"liam5", "臺羅閏號調":"liâm", "通用數字調":"liam5", "吳守禮方音":"⿳⿳⿳ㄌㄧㆰˊ"}],
			"連字音":"liam5"}],
			[{"詞組綜合標音":[
				{"型體":"著", "臺羅數字調":"tioh8", "臺羅閏號調":"tio̍h", "通用數字調":"diorh6", "吳守禮方音":"⿳⿳⿳⿳ㄉㄧㄜ㆐ㆷ"}],
			"連字音":"tioh8"}],
			[{"詞組綜合標音":[
				{"型體":"跤", "臺羅數字調":"kha1", "臺羅閏號調":"kha", "通用數字調":"ka1", "吳守禮方音":"⿳ㄎㄚ"}],
			"連字音":"kha1"}],
			[{"詞組綜合標音":[
				{"型體":"，", "臺羅數字調":",", "臺羅閏號調":",", "通用數字調":",", "吳守禮方音":""}],
			"連字音":","}]
			])

	def test_一句濟詞連字轉json格式(self):
		句物件 = 句([
			self.分析器.產生對齊集('點仔膠', 'tiam2-a2-ka1'),
			self.分析器.產生對齊集('，', ','),
			self.分析器.產生對齊集('黏著', 'liam5-tioh8'),
			self.分析器.產生對齊集('跤', 'kha1'),
			self.分析器.產生對齊集('，', ',')
			])
		標音句 = 句綜合標音(閩南語字綜合標音, 句物件)
		self.assertEqual(標音句.轉json格式(), [
			[{"詞組綜合標音":[
				{"型體":"點", "臺羅數字調":"tiam2", "臺羅閏號調":"tiám", "通用數字調":"diam4", "吳守禮方音":"⿳⿳⿳ㄉㄧㆰˋ"},
				{"型體":"仔", "臺羅數字調":"a2", "臺羅閏號調":"á", "通用數字調":"a4", "吳守禮方音":"⿳ㄚˋ"},
				{"型體":"膠", "臺羅數字調":"ka1", "臺羅閏號調":"ka", "通用數字調":"ga1", "吳守禮方音":"⿳ㄍㄚ"}
				],
			"連字音":"tiam2-a2-ka1"}],
			[{"詞組綜合標音":[
				{"型體":"，", "臺羅數字調":",", "臺羅閏號調":",", "通用數字調":",", "吳守禮方音":""}],
			"連字音":","}],
			[{"詞組綜合標音":[
				{"型體":"黏", "臺羅數字調":"liam5", "臺羅閏號調":"liâm", "通用數字調":"liam5", "吳守禮方音":"⿳⿳⿳ㄌㄧㆰˊ"},
				{"型體":"著", "臺羅數字調":"tioh8", "臺羅閏號調":"tio̍h", "通用數字調":"diorh6", "吳守禮方音":"⿳⿳⿳⿳ㄉㄧㄜ㆐ㆷ"}
				],
			"連字音":"liam5-tioh8"}],
			[{"詞組綜合標音":[
				{"型體":"跤", "臺羅數字調":"kha1", "臺羅閏號調":"kha", "通用數字調":"ka1", "吳守禮方音":"⿳ㄎㄚ"}],
			"連字音":"kha1"}],
			[{"詞組綜合標音":[
				{"型體":"，", "臺羅數字調":",", "臺羅閏號調":",", "通用數字調":",", "吳守禮方音":""}],
			"連字音":","}]
			])
	def test_食章物件(self):
		章物件 = self.分析器.產生對齊章('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
		標音句 = 句綜合標音(閩南語字綜合標音, 章物件)
		self.assertEqual(標音句.轉json格式(), [
			[{'詞組綜合標音': [
				{'通用數字調': 'diam4', '吳守禮方音': '⿳⿳⿳ㄉㄧㆰˋ', '臺羅閏號調': 'tiám', '臺羅數字調': 'tiam2', '型體': '點'},
				{'通用數字調': 'a4', '吳守禮方音': '⿳ㄚˋ', '臺羅閏號調': 'á', '臺羅數字調': 'a2', '型體': '仔'},
				{'通用數字調': 'ga1', '吳守禮方音': '⿳ㄍㄚ', '臺羅閏號調': 'ka', '臺羅數字調': 'ka1', '型體': '膠'},
				{'通用數字調': ',', '吳守禮方音': '', '臺羅閏號調': ',', '臺羅數字調': ',', '型體': '，'}
			], '連字音': 'tiam2-a2-ka1 ,'}],
			[{'詞組綜合標音': [
				{'通用數字調': 'liam5', '吳守禮方音': '⿳⿳⿳ㄌㄧㆰˊ', '臺羅閏號調': 'liâm', '臺羅數字調': 'liam5', '型體': '黏'},
				{'通用數字調': 'diorh6', '吳守禮方音': '⿳⿳⿳⿳ㄉㄧㄜ㆐ㆷ', '臺羅閏號調': 'tio̍h', '臺羅數字調': 'tioh8', '型體': '著'},
				{'通用數字調': 'ka1', '吳守禮方音': '⿳ㄎㄚ', '臺羅閏號調': 'kha', '臺羅數字調': 'kha1', '型體': '跤'},
				{'通用數字調': ',', '吳守禮方音': '', '臺羅閏號調': ',', '臺羅數字調': ',', '型體': '，'}
			], '連字音': 'liam5-tioh8 kha1 ,'}]])

	def test_複雜章物件(self):
		我 = self.分析器.產生對齊集('我', 'gua2')
		愛 = self.分析器.產生對齊集('愛', 'ai3')
		媠某 = self.分析器.產生對齊組('美女', 'sui2-boo2')
		美女 = self.分析器.產生對齊組('美女', 'mi2-lu2')
		莉 = 集([媠某, 美女])
		句物件 = 句([我, 愛, 莉])
		章物件 = 章([句物件, 句物件])
		標音句 = 句綜合標音(閩南語字綜合標音, 章物件)
		self.assertEqual(len(標音句.綜合集), 6)
		self.assertEqual(len(標音句.綜合集[0].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[1].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[2].綜合詞組), 2)
		self.assertEqual(len(標音句.綜合集[3].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[4].綜合詞組), 1)
		self.assertEqual(len(標音句.綜合集[5].綜合詞組), 2)
		self.assertEqual(標音句.綜合集[0], 集綜合標音(閩南語字綜合標音, 我))
		self.assertEqual(標音句.綜合集[1], 集綜合標音(閩南語字綜合標音, 愛))
		self.assertEqual(標音句.綜合集[2], 集綜合標音(閩南語字綜合標音, 莉))
		self.assertEqual(標音句.綜合集[3], 集綜合標音(閩南語字綜合標音, 我))
		self.assertEqual(標音句.綜合集[4], 集綜合標音(閩南語字綜合標音, 愛))
		self.assertEqual(標音句.綜合集[5], 集綜合標音(閩南語字綜合標音, 莉))
		self.assertEqual(標音句.轉json格式(), [
			[{'詞組綜合標音': [
				{"型體":"我", "臺羅數字調":"gua2", "臺羅閏號調":"guá", "通用數字調":"ghua4", "吳守禮方音":"⿳⿳⿳ㆣㄨㄚˋ"}],
			"連字音":"gua2"}],
			[{"詞組綜合標音":[
				{"型體":"愛", "臺羅數字調":"ai3", "臺羅閏號調":"ài", "通用數字調":"ai3", "吳守禮方音":"⿳ㄞ˪"}],
			"連字音":"ai3"}],
			[{"詞組綜合標音":[
				{"型體":"美", "臺羅數字調":"sui2", "臺羅閏號調":"suí", "通用數字調":"sui4", "吳守禮方音":"⿳⿳⿳ㄙㄨㄧˋ"},
				{"型體":"女", "臺羅數字調":"boo2", "臺羅閏號調":"bóo", "通用數字調":"bho4", "吳守禮方音":"⿳⿳ㆠㆦˋ"}],
			"連字音":"sui2-boo2"},
			{"詞組綜合標音":[
				{"型體":"美", "臺羅數字調":"mi2", "臺羅閏號調":"mí", "通用數字調":"mi4", "吳守禮方音":"⿳⿳ㄇㄧˋ"},
				{"型體":"女", "臺羅數字調":"lu2", "臺羅閏號調":"lú", "通用數字調":"lu4", "吳守禮方音":"⿳⿳ㄌㄨˋ"}],
			"連字音":"mi2-lu2"}], [{'詞組綜合標音': [
				{"型體":"我", "臺羅數字調":"gua2", "臺羅閏號調":"guá", "通用數字調":"ghua4", "吳守禮方音":"⿳⿳⿳ㆣㄨㄚˋ"}],
			"連字音":"gua2"}],
			[{"詞組綜合標音":[
				{"型體":"愛", "臺羅數字調":"ai3", "臺羅閏號調":"ài", "通用數字調":"ai3", "吳守禮方音":"⿳ㄞ˪"}],
			"連字音":"ai3"}],
			[{"詞組綜合標音":[
				{"型體":"美", "臺羅數字調":"sui2", "臺羅閏號調":"suí", "通用數字調":"sui4", "吳守禮方音":"⿳⿳⿳ㄙㄨㄧˋ"},
				{"型體":"女", "臺羅數字調":"boo2", "臺羅閏號調":"bóo", "通用數字調":"bho4", "吳守禮方音":"⿳⿳ㆠㆦˋ"}],
			"連字音":"sui2-boo2"},
			{"詞組綜合標音":[
				{"型體":"美", "臺羅數字調":"mi2", "臺羅閏號調":"mí", "通用數字調":"mi4", "吳守禮方音":"⿳⿳ㄇㄧˋ"},
				{"型體":"女", "臺羅數字調":"lu2", "臺羅閏號調":"lú", "通用數字調":"lu4", "吳守禮方音":"⿳⿳ㄌㄨˋ"}],
			"連字音":"mi2-lu2"}],
			])

	def test_烏白傳(self):
		self.assertRaises(型態錯誤, 句綜合標音, 閩南語字綜合標音, ' ')
		章物件 = self.分析器.產生對齊章('點仔膠，黏著跤，', 'tiam2-a2-ka1, liam5-tioh8 kha1,')
		self.assertRaises(型態錯誤, 句綜合標音, ' ', 章物件)
		self.assertRaises(型態錯誤, 句綜合標音, 詞組綜合標音, 章物件)
		self.assertRaises(型態錯誤, 句綜合標音, None, None)

if __name__ == '__main__':
	unittest.main()
