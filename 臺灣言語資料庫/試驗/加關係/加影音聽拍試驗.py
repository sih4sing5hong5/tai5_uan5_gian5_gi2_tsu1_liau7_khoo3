# -*- coding: utf-8 -*-
from 臺灣言語資料庫.試驗.加關係.加關係試驗 import 加關係試驗
import json
from 臺灣言語資料庫.資料模型 import 影音表
from 臺灣言語資料庫.資料模型 import 聽拍表
from 臺灣言語資料庫.關係模型 import 影音聽拍表

class 加影音聽拍試驗(加關係試驗):
	def setUp(self):
		super(加影音聽拍試驗, self).setUp()
		self.原本資料表 = 影音表
		self.原本資料詞內容 = {
			'收錄者':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'來源':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'版權':'會使公開',
			'種類':'字詞',
			'語言腔口':'閩南語',
			'著作所在地':'花蓮',
			'著作年':'2014',
			'原始影音資料':self.詞檔案,
			}
		self.原本資料句內容 = {
			'收錄者':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'來源':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'版權':'袂使公開',
			'種類':'語句',
			'語言腔口':'四縣話',
			'著作所在地':'臺灣',
			'著作年':'195x',
			'原始影音資料':self.句檔案,
			}
		self.中研院聽拍資料庫 = 聽拍規範表.objects.create(
			規範名='中研院聽拍資料庫',
			範例='你好：li1 ho2',
			說明='記錄實際口說的聲調',
		)
		self.對應資料詞內容 = {
			'收錄者':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'來源':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'版權':'會使公開',
			'種類':'字詞',
			'語言腔口':'閩南語',
			'著作所在地':'花蓮',
			'著作年':'2014',
			'規範':'中研院聽拍資料庫',
			'聽拍資料':[
				{'語者':'阿宏', '內容':'li1', '開始時間':0.0, '結束時間':1.2},
				{'語者':'阿莉', '內容':'ho2', '開始時間':1.2, '結束時間':2.0},
			]
			}
		self.對應資料句內容 = {
			'收錄者':json.dumps({'名':'Dr. Pigu', '出世年':'1990', '出世地':'花蓮人'}),
			'來源':json.dumps({'名':'鄉民', '出世年':'1950', '出世地':'臺灣'}),
			'版權':'袂使公開',
			'種類':'語句',
			'語言腔口':'四縣話',
			'著作所在地':'臺灣',
			'著作年':'195x',
			'規範':'中研院聽拍資料庫',
			'聽拍資料':[
				{'內容':'請問車頭按怎行？'},
				{'內容':'直直行就到矣。'},
			]
			}
	def 加詞(self, 影音):
		原來影音資料數 = 影音表.objects.all().count()
		原來聽拍資料數 = 聽拍表.objects.all().count()
		原來影音聽拍數 = 影音聽拍表.objects.all().count()
		聽拍 = 影音.寫聽拍(self.對應資料詞內容)
		self.assertEqual(影音表.objects.all().count(), 原來影音資料數)
		self.assertEqual(聽拍表.objects.all().count(), 原來聽拍資料數 + 1)
		self.assertEqual(影音聽拍表.objects.all().count(), 原來影音聽拍數 + 1)
		self.assertIsInstance(影音.影音聽拍.get(聽拍=聽拍), 影音聽拍表)
		self.assertEqual(影音.影音聽拍.get(聽拍=聽拍).聽拍, 聽拍)
		self.assertEqual(聽拍.收錄者, self.臺灣人)
		self.assertEqual(聽拍.來源, self.花蓮人)
		self.assertEqual(聽拍.版權, self.會使公開)
		self.assertEqual(聽拍.種類, self.字詞)
		self.assertEqual(聽拍.語言腔口, self.閩南語)
		self.assertEqual(聽拍.著作所在地, self.花蓮)
		self.assertEqual(聽拍.著作年, self.二空一四)
		self.assertEqual(聽拍.屬性.count(), 0)
		self.assertEqual(聽拍.規範, self.中研院聽拍資料庫)
		self.assertEqual(json.loads(聽拍.聽拍資料), [
			{'語者':'阿宏', '內容':'li1', '開始時間':0.0, '結束時間':1.2},
			{'語者':'阿莉', '內容':'ho2', '開始時間':1.2, '結束時間':2.0},
		])
	def 加句(self, 影音):
		原來影音資料數 = 影音表.objects.all().count()
		原來聽拍資料數 = 聽拍表.objects.all().count()
		原來影音聽拍數 = 影音聽拍表.objects.all().count()
		聽拍 = 影音.寫聽拍(self.對應資料句內容)
		self.assertEqual(影音表.objects.all().count(), 原來影音資料數)
		self.assertEqual(聽拍表.objects.all().count(), 原來聽拍資料數 + 1)
		self.assertEqual(影音聽拍表.objects.all().count(), 原來影音聽拍數 + 1)
		self.assertIsInstance(影音.影音聽拍.get(聽拍=聽拍), 影音聽拍表)
		self.assertEqual(影音.影音聽拍.get(聽拍=聽拍).聽拍, 聽拍)
		self.assertEqual(聽拍.收錄者, self.花蓮人)
		self.assertEqual(聽拍.來源, self.臺灣人)
		self.assertEqual(聽拍.版權, self.袂使公開)
		self.assertEqual(聽拍.種類, self.語句)
		self.assertEqual(聽拍.語言腔口, self.四縣話)
		self.assertEqual(聽拍.著作所在地, self.臺灣)
		self.assertEqual(聽拍.著作年, self.一九五空年代)
		self.assertEqual(聽拍.屬性.count(), 0)
		self.assertEqual(聽拍.規範, self.中研院聽拍資料庫)
		self.assertEqual(json.loads(聽拍.聽拍資料),
			[
				{'內容':'請問車頭按怎行？'},
				{'內容':'直直行就到矣。'},
			]
		)
