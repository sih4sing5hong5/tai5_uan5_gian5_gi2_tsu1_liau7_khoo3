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
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣反義詞的詞音
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣近義詞的詞音
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣詞別音
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 俗音記號
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 合音記號
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣詞合音
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣詞俗音
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 教育部閩南語辭典空白符號
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣字方言差
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 字方言差欄位
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣詞方言差
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 詞方言差欄位
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 教育部閩南語辭典隔開符號
from 臺灣言語工具.字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 臺灣言語工具.字詞組集句章.解析整理工具.文章粗胚工具 import 文章粗胚工具
from 臺灣言語工具.字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 教育部閩南語辭典地區
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 教育部閩南語辭典年代
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 教育部閩南語辭典名
from 臺灣言語工具.字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語常用詞辭典 import 揣主條目
from 整理教育部臺灣閩南語常用詞辭典.教育部閩南語辭典工具 import 教育部閩南語辭典工具
from 臺灣言語資料庫.腔口資訊 import 偏漳優勢音腔口
from 臺灣言語資料庫.腔口資訊 import 偏泉優勢音腔口
from 臺灣言語資料庫.腔口資訊 import 混合優勢音腔口
from 臺灣言語資料庫.欄位資訊 import 會當替換
from 臺灣言語資料庫.欄位資訊 import 近義
from 臺灣言語資料庫.模型 import 文字
from 臺灣言語資料庫.模型 import 演化
from 臺灣言語資料庫.模型 import 關係
from 整理教育部臺灣閩南語常用詞辭典.模型 import 教育部臺灣閩南語常用詞辭典來源
from 整理教育部臺灣閩南語常用詞辭典.整合釋義佮例句 import 整合釋義佮例句
from 臺灣言語資料庫.欄位資訊 import 合音
from 臺灣言語資料庫.欄位資訊 import 俗音

class 整合到文字():
	加入文字 = True
	例句會當變動符號 = False
	def __init__(self):
		辭典工具 = 教育部閩南語辭典工具()
		
		粗胚工具 = 文章粗胚工具()
		分析器 = 拆文分析器()
		轉音家私 = 轉物件音家私()
		譀鏡 = 物件譀鏡()
		釋義佮例句 = 整合釋義佮例句()

		# {'--tsi̍t-kuá'}
		# 13602因
		音空 = {''}
		for 主編號, 屬性, 漢字, 音標, 方言差 in 揣主條目(1):
# 			print('主編號',主編號)
			try:
	# 			print('@'.join([str(主編號), str(屬性), 漢字, 音標]))
				if 屬性 == 25:
					種類 = '語句'
				else:
					種類 = '字詞'
				腔口集 = {}
				腔口集[偏漳優勢音腔口] = {}
				腔口集[偏泉優勢音腔口] = {}
				腔口集[混合優勢音腔口] = {}
				主音 = set()
				if 音標 != None:
					主音 |= {音標}
				主音 |= { 音[0] for 音 in 揣反義詞的詞音(主編號)} | { 音[0] for 音 in 揣近義詞的詞音(主編號)} | { 音[0] for 音 in 揣詞別音(主編號)}
				俗音音標 = { 音[0] + 俗音記號 for 音 in 揣詞俗音(主編號)}
				合音音標 = { 音[0] + 合音記號 for 音 in 揣詞合音(主編號)}
				主音 |= 俗音音標
				主音 |= 合音音標
				主音 -= 音空
				if 主音 == {'Si̍k-tsí(Si̍p-tsí)'}:
					主音 = {'Si̍k-tsí', 'Si̍p-tsí'}
				for 音 in 主音:
					if 漢字 not in 腔口集[偏漳優勢音腔口]:
						腔口集[偏漳優勢音腔口][漢字] = []
					if 漢字 not in 腔口集[偏泉優勢音腔口]:
						腔口集[偏泉優勢音腔口][漢字] = []
					if 漢字 not in 腔口集[混合優勢音腔口]:
						腔口集[混合優勢音腔口][漢字] = []
# 					if 音 == 'tsánn-tiū-á-bué/bé':
# 						音 = 'tsánn-tiū-á-bué/tsánn-tiū-á-bé'
					雙優勢音 = 音.split('/')
# 					if 音 == 'ke/kue-tshíng' and 主編號 == 12744 and len(主音) > 1:
# 						continue
					if 音 == 'Jû/Lû/Jî':
						腔口集[偏漳優勢音腔口][漢字].append(雙優勢音[2])
						腔口集[偏泉優勢音腔口][漢字].append(雙優勢音[0])
						腔口集[偏泉優勢音腔口][漢字].append(雙優勢音[1])
						continue
					if len(雙優勢音) == 1:
						雙優勢音.append(雙優勢音[0])
					偏漳優勢音, 偏泉優勢音 = [優勢音.strip(教育部閩南語辭典空白符號) \
						for 優勢音 in 雙優勢音]
					混合優勢音 = None
					if 偏漳優勢音 == 偏泉優勢音:
						混合優勢音 = 偏漳優勢音
					if 漢字 == '竿(菅)蓁林':
						腔口集[偏漳優勢音腔口]['竿蓁林'] = [偏漳優勢音]
						腔口集[偏泉優勢音腔口]['竿蓁林'] = [偏泉優勢音]
						腔口集[偏漳優勢音腔口]['菅蓁林'] = [偏漳優勢音]
						腔口集[偏泉優勢音腔口]['菅蓁林'] = [偏泉優勢音]
						if 混合優勢音 != None:
							腔口集[混合優勢音腔口]['竿蓁林'] = [混合優勢音]
							腔口集[混合優勢音腔口]['菅蓁林'] = [混合優勢音]
						漢字 = '竿蓁林'
					elif 漢字 == '苓仔寮、能雅寮':
						腔口集[偏漳優勢音腔口]['苓仔寮'] = [偏漳優勢音]
						腔口集[偏泉優勢音腔口]['苓仔寮'] = [偏泉優勢音]
						腔口集[偏漳優勢音腔口]['能雅寮'] = [偏漳優勢音]
						腔口集[偏泉優勢音腔口]['能雅寮'] = [偏泉優勢音]
						if 混合優勢音 != None:
							腔口集[混合優勢音腔口]['苓仔寮'] = [混合優勢音]
							腔口集[混合優勢音腔口]['能雅寮'] = [混合優勢音]
						漢字 = '苓仔寮'
					elif 漢字 == '那卡西' and 音標 == 'ながし':
						腔口集[偏漳優勢音腔口]['那卡西'] = ['1na1-1ka7-1si3']
						腔口集[偏漳優勢音腔口]['ながし'] = ['1na1-1ka7-1si3']
						腔口集[偏泉優勢音腔口]['那卡西'] = ['1na1-1ka7-1si3']
						腔口集[偏泉優勢音腔口]['ながし'] = ['1na1-1ka7-1si3']
						腔口集[混合優勢音腔口]['那卡西'] = ['1na1-1ka7-1si3']
						腔口集[混合優勢音腔口]['ながし'] = ['1na1-1ka7-1si3']
					else:
						腔口集[偏漳優勢音腔口][漢字].append(偏漳優勢音)
						腔口集[偏泉優勢音腔口][漢字].append(偏泉優勢音)
						if 混合優勢音 != None:
							腔口集[混合優勢音腔口][漢字].append(混合優勢音)
	
				if len(方言差) == 6:
					# "主編號"=12239
					字方言差 = list(揣字方言差(方言差)[0])[3:]
					for i in range(len(字方言差欄位)):
						字方言差[i] = 字方言差[i].strip()
						if 字方言差[i] != 'x' and 字方言差[i] != '暫無資料':
	# 						print(字方言差[i])
# 							if 字方言差[i] == 'tshiòr/tshiònn':
# 								字方言差[i] = 'tshiòr;tshiònn'
							腔口集[字方言差欄位[i]] = {}
							腔口集[字方言差欄位[i]][漢字] = [ 方言.strip(教育部閩南語辭典空白符號) for 方言 in 字方言差[i].split(';')]
				elif len(方言差) == 8:
					# "主編號"=4368
					詞方言差 = list(揣詞方言差(方言差)[0])[3:]
					for i in range(len(詞方言差欄位)):
						詞方言差[i] = 詞方言差[i].strip()
						if 詞方言差[i] != 'x' and 詞方言差[i] != '暫無資料':
	# 						print(詞方言差[i])
# 							if 詞方言差[i] == '菅芒　kuann-bang, kuann-bâng':
# 								詞方言差[i] = '菅芒　kuann-bang; kuann-bâng'
# 							elif 主編號 == 2876:
# 								詞方言差[i] = 詞方言差[i].replace('tuē', 'tuē; tueh')
# 							elif 詞方言差[i] == '秤砣　tshìn-thô(tô)':
# 								詞方言差[i] = '秤砣　tshìn-thô;tshìn-tô'
	
							字音集 = [一組字音.split(教育部閩南語辭典隔開符號, 1) for 一組字音 in 詞方言差[i].split(',')]
							字音對照 = {}
							for 字, 音 in 字音集:
								字音對照[字.strip(教育部閩南語辭典空白符號)] = [資料.strip(教育部閩南語辭典空白符號) for 資料 in 音.split(';')]
							腔口集[詞方言差欄位[i]] = 字音對照
	
				編修物件集 = []
				for 腔口, 字音 in 腔口集.items():
					for 字, 音集 in 字音.items():
						原本音流水號集 = []
						俗音流水號集 = []
						合音流水號集 = []
						組字式型體 = 辭典工具.共造字換做統一碼表示法(字)
						# 資料型體 = 粗胚工具.符號邊仔加空白(資料型體).strip()
						for 音 in 音集:
							#有人會改，愛備份
							資料型體=組字式型體
							
							是俗音 = False
							是合音 = False
# 							if 資料型體 == '熟' and 音 == 'tînn-kha-puānn-tshiú':
# 								continue
							if 音 == 'iang35-ua55-ua55':
								continue
							資料型體, 音 = self.語句調整(主編號, 資料型體, 音)
							
							型替換 = {'收瀾收予焦，予你生一个有':'收瀾收予焦，予你生一个有𡳞脬。'
								}
							if 資料型體 in 型替換:
								資料型體 = 型替換[資料型體]
								
							if 音.endswith(俗音記號):
								是俗音 = True
								音 = 音[:-len(俗音記號)]
							elif 音.endswith(合音記號):
								音 = 音[:-len(合音記號)]
							合音字表 = {('下昏暗', 'ing-àm'), ('下昏暗時', 'ing-àm-sî'), ('下昏時', 'ing-sî'),
								('下昏', 'i̋ng'), ('這陣', 'tsín'), ('這陣', 'tsún'),
								('佗位', 'tuē'), ('佗位', 'tueh'), ('嘿啦', 'hiàu'),
								('查某𡢃', 'tsőo-kán'), ('查某𡢃仔', 'tsőo-kán-á'),
								('查某囡仔', 'tsa̋-gín-á'), ('查某囡仔', 'tsa̋u-gín-á'),
								('查某孫', 'tsa̋u-sun'),
								('啥物人', 'siàng-n̂g'), ('啥物人', 'sáng-n̂g'), }
							if  (資料型體 in 腔口集[偏漳優勢音腔口] and (音 + 合音記號) in 腔口集[偏漳優勢音腔口][資料型體]) or \
								((資料型體, 音) in 合音字表):
								是合音 = True
							if 是合音:
								if 主編號 == 9440:  # 嫁查甫囝
									資料型體 = 資料型體[:1] + '⿰' + 資料型體[1:]
								elif 主編號 == 8331 and '-' not in 音:  # tsua̋n
									資料型體 = '⿰⿰' + 資料型體
								elif 主編號 == 5923 and '-' not in 音:  # tsha̋u
									資料型體 = '⿰⿰' + 資料型體
								else:
									資料型體 = '⿰' + 資料型體
							第二三字組合 = {('硩落去', 'teh--loih'), ('硩落去', 'teh--loì'),
								('嫁查某囝', 'kè-tsőo-kiánn'), ('嫁查某囝', 'kè-tsa̋u-kiánn'),
								('嫁查某囝', 'kè-tsőo-kiánn'), ('嫁查某囝', 'kè-tsa̋u-kánn'),
								}
							if ((資料型體, 音) in 第二三字組合):
								資料型體 = 資料型體[:1] + '⿰' + 資料型體[1:]
							if (資料型體, 音) in {('阮厝的查某人', 'gún-tshù-ê-tsa̋u-lâng')}:
								資料型體 = 資料型體.replace('查某', '⿰查某')
								
							資料型體, 音 = self.日語處理(主編號, 資料型體, 音)
								
							音 = 粗胚工具.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 音)
							音 = 粗胚工具.符號邊仔加空白(音).strip()
							地區對應 = {'鹿港':偏泉優勢音腔口, '三峽':偏泉優勢音腔口, '臺北':偏泉優勢音腔口,
								'宜蘭':偏漳優勢音腔口, '臺南':混合優勢音腔口, '高雄':混合優勢音腔口, '金門':偏泉優勢音腔口,
								'馬公':偏泉優勢音腔口, '新竹':偏泉優勢音腔口, '臺中':偏漳優勢音腔口, }
							所在地區 = 教育部閩南語辭典地區
							for 對應地區, 對應腔口 in 地區對應.items():
								if 對應地區 in 腔口:
									腔口 = 對應腔口
									所在地區 = 對應地區
							if 腔口 not in {偏泉優勢音腔口, 偏漳優勢音腔口, 混合優勢音腔口}:
								raise RuntimeError('腔口無著！！{0}'.format(腔口))
	# 						if True:
							try:
								原音句物件 = 分析器.產生對齊句(資料型體, 音)
								上尾句物件 = 轉音家私.轉做標準音標(臺灣閩南語羅馬字拼音, 原音句物件)
								if self.加入文字:
									文字物件 = 文字.objects.create(來源=教育部閩南語辭典名,
										種類=種類, 腔口=腔口, 地區=所在地區, 年代=教育部閩南語辭典年代,
										型體=譀鏡.看型(上尾句物件), 音標=譀鏡.看音(上尾句物件))
									編修物件 = 文字物件.流水號
									編修物件集.append(編修物件)
									教育部臺灣閩南語常用詞辭典來源.objects.create(
										流水號=編修物件, 主編號=主編號)
									if 是俗音:
										俗音流水號集.append(編修物件)
									elif 是合音:
										合音流水號集.append(編修物件)
									else:
										原本音流水號集.append(編修物件)
							except Exception as 錯誤:
								print('主編號', 主編號, 譀鏡.看型(上尾句物件), 譀鏡.看音(上尾句物件), 錯誤)
								raise 錯誤
				if self.加入文字:
					# 5923 and 4000
					for 原本音流水號 in 原本音流水號集:
						for 俗音流水號 in 俗音流水號集:
							演化.objects.create(
								甲流水號=原本音流水號, 乙流水號=俗音流水號,
								乙對甲的演化類型=俗音)
					for 原本音流水號 in 原本音流水號集:
						for 合音流水號 in 合音流水號集:
							演化.objects.create(
								甲流水號=原本音流水號, 乙流水號=合音流水號,
								乙對甲的演化類型=合音)
					try:
						釋義佮例句.建立釋義(主編號, 編修物件集, self.例句會當變動符號)
					except Exception as 錯誤:
						print(主編號, 漢字, 錯誤)
					while len(編修物件集) > 0:
						頭前流水號, *編修物件集 = 編修物件集
						for 後壁流水號 in 編修物件集:
							關係.objects.create(
								甲流水號=頭前流水號, 乙流水號=後壁流水號,
								乙對甲的關係類型=近義, 關係性質=會當替換)
							關係.objects.create(
								甲流水號=後壁流水號, 乙流水號=頭前流水號,
								乙對甲的關係類型=近義, 關係性質=會當替換)
			except Exception as 錯誤:
				print(主編號, 漢字, 錯誤)
# 				raise 錯誤
# 				raise RuntimeError('{}{}{}'.format(主編號, 漢字, 錯誤))
	def 語句調整(self, 主編號, 資料型體, 音):
		if 音 == "sai-kong-á (面稱)":
			音 = "sai-kong-á"
		elif 音 == "sai-sun-á (背稱)":
			音 = "sai-sun-á"
		elif 音 == "khioh-gín-á(產婆語)":
			音 = "khioh-gín-á"
		elif 音 == "tshâ-se(大)":
			音 = "tshâ-se"
		elif 音 == "luai̍h-á(小)":
			音 = "luai̍h-á"
		elif 音 == "hông-hun(書)":
			音 = "hông-hun"
		elif 音 == 'tsînn(中間有孔)':
			音 = 'tsînn'  # 鐳　lui (無空的)
		elif 音 == 'tshâ-se(大)':
			音 = 'tshâ-se'
		elif 音 == 'luai̍h-á(小)':
			音 = 'luai̍h-á'
		elif 音 == 'guán(男)':
			音 = 'guán'
		elif 音 == 'gún(女)':
			音 = 'gún'
		if 資料型體 == "司孫(背稱)":
			資料型體 = "司孫"

		if 資料型體 == "竹圍" and 主編號 == 36014:
			資料型體 = "竹圍仔"
		elif 資料型體 == "石牌" and 主編號 == 36021:
			資料型體 = "石牌仔"
		elif 資料型體 == "拔林" and 主編號 == 34058:
			資料型體 = "拔仔林"
		elif 資料型體 == "蓮蕉花" and 音 == 'lân-tsiau' and 主編號 == 11353:
			資料型體 = "蓮蕉"
		elif 資料型體 == "圓山" and 主編號 == 36026:
			資料型體 = "圓山仔"
		elif 資料型體 == "三重" and 主編號 == 36124:
			資料型體 = "三重埔"
		elif 音 == 'Hè-sen-ná':  # 講毋是漢語，無愛變ian
			音 = 'Hè-sian-ná'
		elif 資料型體 == 'xx姊仔' and 音 == 'xxtsé--á':  # xx是會當換做名詞
			資料型體 = '姊仔'
			音 = 'tsé--á'
# 						elif 資料型體 == "瘦田" and 主編號 == 60344:
# 							資料型體 = "瘦田𠢕欶水。"
# 						elif 資料型體 == "䆀猴" and 主編號 == 60373:
# 							資料型體 = "䆀猴𠢕欠數。"
		# m7 tioh8
		# if 音 == "niàu-ka-tsiah hit- ki":
		# 	# love you~
		# 	音 = "niàu-ka-tsiah hit-ki"
		return 資料型體, 音
	def 日語處理(self, 主編號, 資料型體, 音):
		if (主編號, 資料型體) in self.日語替換:
			資料型體 = self.日語替換[(主編號, 資料型體)]
			音 = 音.replace('33', '7')
			音 = 音.replace('55', '1')
			音 = 音.replace('11', '3')
			音 = 音.replace('51', '2')
			音 = 音.replace('35', '5')
			音 = 音.replace('t5', 't8')
			音 = 音.replace('t3', 't4')
			音 = 音.replace('h5', 'h8')
			音 = 音.replace('h3', 'h4')
			音 = '1' + 音.replace('-', '-1')
		return 資料型體,音
	日語替換 = {
		(10740, 'ロ—ス'):'⿰ロ—ス',
		(1114, 'メンス'):'⿰メンス',
		(1632, 'はしか'):'はしか',
		(1736, 'ブラジゃ—'):'ブラ⿰⿰ジャ—',
		(1736, 'ブラジャ—'):'ブラ⿰⿰ジャ—',
		(2041, 'ステンレス'):'ス⿰テンレス',
		(2572, 'レコード'):'レ⿰コード',
		(2731, 'じどうしゃ'):'じ⿰どう⿰しゃ',
		(2993, 'じしゃく'):'じ⿰しゃく',
		(3085, 'おニンギョウ'):'お⿰ニン⿰⿰ギョウ',
		(3085, 'オニンギョウ'):'オ⿰ニン⿰⿰ギョウ',
		(3087, 'まんが'):'⿰まんが',
		(3436, 'ロ—ス'):'⿰ロ—ス',
		(3524, 'みそしる'):'みそしる',
		(3524, 'みそ'):'みそ',
		(4467, 'わさび'):'わさび',
		(4574, 'とうさん'):'⿰とう⿰さん',
		(5106, 'トマト'):'トマト',
		(5437, 'にんじん'):'⿰にん⿰じん',
		(6043, 'ホテル'):'ホテル',
		(6088, 'ホテル'):'ホテル',
		(6590, 'ガラ油'):'ガラ油',
		(6848, 'ミシン'):'ミ⿰シン',
		(7561, 'スリッパ'):'ス⿰リッパ',
		(7561, 'ぞうり仔'):'⿰ぞうり仔',
		(8124, 'ビル'):'ビル',
		(8124, 'ビ—ル'):'⿰ビ—ル',
		(8164, 'パチンコ'):'パ⿰チンコ',
		(8727, 'ガラ油'):'ガラ油',
		(9928, 'コレラ'):'コレラ',
		(10927, 'アルミ'):'アルミ',
		(10965, 'ネクタイ'):'ネク⿰タイ',
		(11252, 'ロ—ス'):'⿰ロ—ス',
		(11988, 'ステンレス'):'ス⿰テンレス',
		(12555, 'はしか'):'はしか',
		(13055, 'りんご'):'⿰りんご',
		(13091, 'パン'):'⿰パン',
		# (25750, 'ながし'):'ながし',
		(7906, '鳶'):'⿰とんび',
		}

if __name__=='__main__':
	整合到文字()
	