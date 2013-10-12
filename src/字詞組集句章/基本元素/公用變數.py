
# 瀏覽器希望無音愛有空白，但是處理標音時希望是佮好認的
無音 = ''  # '　'
# sui1 koo1-niu5 =>　媠　姑娘
分字符號 = '-'
分詞符號 = ' '
# 句中是為著加速標音
句中標點符號 = {'、', '﹑', '-', '—', '~', '～',
	'·', '‧',  # 外國人名中間
	'＇', '"', '\‘', '’', '“', '”', '〝', '〞', '′', '‵',
	'「', '」', '『', '』', '【', '】', '《', '》', '（', '）', '＜', '＞', '(', ')',
	'+', '*', '/', '=', '^', '＋', '－', '＊', '／', '＝', '$', '#', '#',
	 ':', '：', '﹕', ';', '；', '—', '―', '｜', '︱',
	}
# 斷句是考慮著翻譯，閣有語音合成愛做的正規化
斷句標點符號 = {',', '，', '。', '．', '！', '？', '…', } | { ',', '.', '!', '?', } | {'﹐', '﹒', '﹗', '﹖'}

標點符號 = 句中標點符號 | 斷句標點符號

組字式符號 = '⿰⿱⿳⿴⿻'

# Ll　小寫， Lu　大寫， Md　數字，Lo　其他, So 組字式符號…
統一碼羅馬字類 = {'Ll', 'Lu'}
統一碼數字類 = {'Nd'}
統一碼漢字佮組字式類 = {'Lo', 'So'}
統一碼音標類 = 統一碼羅馬字類 | 統一碼數字類
