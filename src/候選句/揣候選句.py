from 剖析相關工具.剖析結構化工具 import 剖析結構化工具
from 剖析相關工具.剖析結構化工具 import 國閩單位翻譯
from 剖析相關工具.剖析工具 import 剖析工具
from 言語資料庫.公用資料 import 資料庫連線

class 揣候選句:
	def __init__(self):
		self.揣剖析資料 = 資料庫連線.prepare('SELECT ' +
			'"甲"."流水號","丁"."流水號","甲"."型體","甲"."音標","乙"."型體","丁"."型體","丁"."音標"' +
			'FROM "言語"."文字" AS "甲","言語"."斷詞暫時表" AS "乙","言語"."關係" AS "丙",' +
			'"言語"."文字" AS "丁" ' +
			'WHERE "甲"."流水號"="乙"."斷詞目標流水號" AND' +
			'"甲"."流水號"="丙"."乙流水號" AND "丙"."關係性質"=\'會當替換\' AND ' +
			'"丁"."流水號"="丙"."甲流水號" ' +
			'ORDER BY "甲"."流水號" DESC ' +
			'LIMIT 10000')()
# 		print(self.揣剖析資料)
	def 相似比較(self, 翻譯句, 候選句, 評分函式):
		候選句長度 = len(候選句)
		候選句位置 = 0
		攏總分數 = 1
		無法度直接換 = False
		for 一段剖析 in 翻譯句:
			無相仝 = True
			while 無相仝 and 候選句位置 < 候選句長度:
				if isinstance(一段剖析, list) and isinstance(候選句[候選句位置], list) and 一段剖析[0] == 候選句[候選句位置][0]:
					攏總分數 += self.相似比較(一段剖析, 候選句[候選句位置], 評分函式)
					無相仝 = False
				elif isinstance(一段剖析, tuple) and isinstance(候選句[候選句位置], tuple) and 一段剖析[1] == 候選句[候選句位置][1]:
					攏總分數 += 100
					if 一段剖析[0] == 候選句[候選句位置][0]:
						攏總分數 += 100
						if len(一段剖析) >= 3 and len(候選句[候選句位置]) >= 3 and 一段剖析[2] == 候選句[候選句位置][2]:
							攏總分數 += 100
					無相仝 = False
				elif isinstance(一段剖析, str):
					無相仝 = False

				候選句位置 += 1
# 				print(攏總分數)
# 			print(無相仝)
			if 無相仝:
				無法度直接換 = True
		if 無法度直接換:
			攏總分數 = -1
# 				print(一段剖析)
# 				print(候選句位置)
		return 攏總分數
	def 相似換新(self, 翻譯句, 候選句, 對應句, 評分函式):
		候選句長度 = len(候選句)
		候選句位置 = 0
		攏總分數 = 1
		無法度直接換 = False
		結果句 = []
		for 一段剖析 in 翻譯句:
			無相仝 = True
			while 無相仝 and 候選句位置 < 候選句長度:
# 				print(一段剖析)
# 				print(type(一段剖析))
				if isinstance(一段剖析, list) and isinstance(候選句[候選句位置], list) and 一段剖析[0] == 候選句[候選句位置][0]:
					結果句.append(self.相似換新(一段剖析, 候選句[候選句位置], 對應句, 評分函式))
					無相仝 = False
				elif isinstance(一段剖析, tuple) and isinstance(候選句[候選句位置], tuple) and 一段剖析[1] == 候選句[候選句位置][1]:
					攏總分數 += 100
					結果詞 = 國閩單位翻譯(一段剖析)
					對照詞 = 國閩單位翻譯(候選句[候選句位置])
					結果句.append((結果詞, 一段剖析, 對照詞, 候選句[候選句位置],))
					if 一段剖析[0] == 候選句[候選句位置][0]:
						攏總分數 += 100
						print(對照詞, end = '')
						print(" 免變")
						if len(一段剖析) >= 3 and len(候選句[候選句位置]) >= 3 and 一段剖析[2] == 候選句[候選句位置][2]:
							攏總分數 += 100
					else:
						print(對照詞, end = '')
						print(" ----> ", end = '')
						print(結果詞)
					無相仝 = False
				elif isinstance(一段剖析, str):
					結果句.append(一段剖析)
					無相仝 = False
				else:
					print(候選句[候選句位置], end = '')
					print('擲掉')
				候選句位置 += 1
# 				print(攏總分數)
# 			print(無相仝)
			if 無相仝:
				無法度直接換 = True
		if 無法度直接換:
			攏總分數 = -1
			print(候選句, end = '')
			print('規句愛換')
# 				print(一段剖析)
# 				print(候選句位置)
		return 結果句
if __name__ == '__main__':
#  	print(剖析結果字串集)
	結構化工具 = 剖析結構化工具()
	揣候選句工具 = 揣候選句()
	翻譯句 = '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)'
	翻譯句='#1:1.[0] S(NP(Head:N:我)|Head:Vt:覺得|S(NP(Head:N:我)|Head:Vt:做|ASP:了|NP(DM:一個|V‧的(Vi:假|Head:T:的)|Head:N:作品)))#'
	
	翻譯句結構化結果 = 結構化工具.結構化剖析結果(翻譯句)
	印出 = lambda 型體佮詞性語意:print(型體佮詞性語意[0], end = ' ')
# 	print(國閩單位翻譯(('吃',)))

	for 剖析結果字串 in 揣候選句工具.揣剖析資料:
# 		print(剖析結果字串)
		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串[4])
		分數=揣候選句工具.相似比較(翻譯句結構化結果, 結構化結果, None)
		if 分數>100:
			print(翻譯句結構化結果)
			print(結構化結果)
			結構化工具.處理結構化結果(翻譯句結構化結果, 印出)
			print()
			結構化工具.處理結構化結果(結構化結果, 印出)
			print()
			print(分數)
			print(揣候選句工具.相似換新(翻譯句結構化結果, 結構化結果, 剖析結果字串[5], None))


	工具 = 剖析工具()
# 	剖析結果字串集=工具.剖析('我想吃飯，，，我想吃很多飯。假如我也用這種方式旅行。再想到蝴蝶會生滿屋的毛蟲。')
	剖析結果字串集 = ['#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#，(COMMACATEGORY)',
			'#2:1.[0] %()#，(COMMACATEGORY)',
			'#3:1.[0] %()#，(COMMACATEGORY)',
			'#4:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
			'#5:1.[0] S(C:假如|NP(Head:N:我)|ADV:也|PP(Head:P:用|NP(DM:這種|Head:N:方式))|Head:Vi:旅行)#。(PERIODCATEGORY)',
			'#6:1.[0] VP(ADV:再|Head:Vt:想到|NP(S‧的(head:S(NP(Head:N:蝴蝶)|ADV:會|Head:Vt:生|NP(Head:N:滿屋))|Head:T:的)|Head:N:毛蟲))#。(PERIODCATEGORY)',
			'#1:1.[0] VP(evaluation:Dbb:再|Head:VE2:想到|goal:NP(predication:S‧的(head:S(agent:NP(Head:Nab:蝴蝶)|epistemics:Dbaa:會|Head:VC31:生|theme:NP(Head:Na:滿屋))|Head:DE:的)|Head:Nab:毛蟲))#。(PERIODCATEGORY)',
			'#1:1.[0] S(NP(Head:N:我們)|ADV:要|Head:Vi:下班)#，(COMMACATEGORY)',
			'#2:1.[0] S(NP(Head:N:我)|PP(Head:P:和|NP(Head:N:他))|Head:Vt:想|VP(Head:Vi:回家))#，(COMMACATEGORY)',
			'#3:1.[0] S(NP(Head:N:你們)|DM:兩個|Head:Vt:想|VP(Head:Vi:睡覺))#。(PERIODCATEGORY)']
# 	for 剖析結果字串 in 剖析結果字串集:
# # 		print(剖析結果字串)
# 		結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串)
# 		print(翻譯句結構化結果)
# 		print(結構化結果)
# 		結構化工具.處理結構化結果(翻譯句結構化結果,印出)
# 		print()
# 		結構化工具.處理結構化結果(結構化結果,印出)
# 		print()
# 		print(揣候選句工具.相似比較(翻譯句結構化結果,結構化結果,None))
# 		print(揣候選句工具.相似換新(翻譯句結構化結果,結構化結果,'',None))
# # 		翻譯結果=結構化工具.處理結構化結果(結構化結果,國閩單位翻譯)
# # 		print(翻譯結果)
# # 		結構化工具.處理結構化結果(翻譯結果,印出)
# # 		print()
#
#
# # 	結構化結果 = 結構化工具.結構化剖析結果(剖析結果字串集[0])
# # 	結構化工具.處理結構化結果(翻譯句結構化結果,印出)
# # 	print()
# # 	結構化工具.處理結構化結果(結構化結果,印出)
# # 	print()
# # 	print(揣候選句工具.相似比較(翻譯句結構化結果,結構化結果,None))
# # 	print(揣候選句工具.相似換新(翻譯句結構化結果,結構化結果,'我想欲食飯',None))
# #
# # 	print(國閩單位翻譯(['回家']))
