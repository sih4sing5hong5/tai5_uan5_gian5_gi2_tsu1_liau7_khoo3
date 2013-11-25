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
from 資料庫.資料庫連線 import 資料庫連線

class 辭典條目:
	文讀層 = '文讀層'
	白話層 = '白話層'
	
	揣言語層的字詞 = lambda self, 腔口, 語言層:資料庫連線.prepare('SELECT ' + 
		'DISTINCT "乙流水號" FROM "言語"."關係" ' + 
		'WHERE "乙對甲的關係類型"=$1 AND "關係性質"=$2 '
		'ORDER BY "乙流水號"')('仝字，用佇無仝言語層', 語言層)
	
	揣腔口資料 = lambda self, 腔口:資料庫連線.prepare('SELECT ' + 
		'"子"."流水號","子"."型體","子"."音標" ' + 
		'FROM "言語"."文字" AS "子" ' + 
		# ' WHERE "子"."腔口" LIKE $1 ' + 
		' WHERE "子"."腔口"=$1 ' + 
		' AND "子"."種類"=\'字詞\' ' + 
		'ORDER BY "子"."流水號"')(腔口)
		
	揣腔口字詞資料 = lambda self, 腔口:資料庫連線.prepare('SELECT ' + 
		'"子"."流水號","子"."型體","子"."音標" ' + 
		'FROM "言語"."文字" AS "子" ' + 
		# ' WHERE "子"."腔口" LIKE $1 ' + 
		' WHERE "子"."腔口"=$1 ' + 
		'ORDER BY "子"."流水號"')(腔口)
	
# 	揣腔口型體資料 = lambda self,腔口, 型態:資料庫連線.prepare('SELECT ' +
# 		'"子"."流水號","子"."型體","子"."音標" ' +
# 		'FROM "言語"."文字" AS "子" ' +
# 		' WHERE "子"."腔口" LIKE $1 AND "子"."型體"=$2 '+
# 		' AND "子"."流水號"<1164335'+#莫拆字結果
# 		'ORDER BY "子"."流水號"')(腔口+'%', 型態)
