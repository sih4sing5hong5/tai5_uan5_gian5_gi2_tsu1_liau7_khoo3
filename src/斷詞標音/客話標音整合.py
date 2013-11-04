
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 斷詞標音.型音辭典 import 型音辭典
from 斷詞標音.動態規劃斷詞標音 import 動態規劃斷詞標音
from 字詞組集句章.基本元素.公用變數 import 分詞符號
from 字詞組集句章.基本元素.公用變數 import 分字符號
from 斷詞標音.辭典條目 import 辭典條目

class 客話標音整合:
	腔口 = '漢語族客家方言四縣腔'
	條目 = 辭典條目()
	文讀層 = None
	白話層 = None
	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	辭典 = None
	斷詞標音 = 動態規劃斷詞標音()
	def __init__(self, 腔口, 辭典):
		self.文讀層 = self.條目.文讀層
		self.白話層 = self.條目.白話層
		self.腔口 = 腔口
		self.文讀字 = set()
		[self.文讀字.add(字詞[0]) for 字詞 in self.條目.揣言語層的字詞(self.腔口, self.文讀層)]
		self.白話字 = set()
		[self.白話字.add(字詞[0]) for 字詞 in self.條目.揣言語層的字詞(self.腔口, self.白話層)]
		self.辭典 = 辭典(4)

		for 流水號, 型體, 音標 in self.條目.揣腔口字詞資料(腔口):
			處理過的音標 = 音標.replace(分詞符號, 分字符號)
			詞物件 = self.分析器.產生對齊詞(型體, 處理過的音標)
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
	標音 = 客話標音整合('漢語族客家方言四縣腔', 型音辭典)
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
	音 = 標音.語句斷詞標音('冤仇', 標音.文讀層)
	print(音)
	音 = 標音.語句斷詞標音('好好鱟刣甲屎那流,', 標音.文讀層)
	print(音)
	音 = 標音.語句斷詞標音('好好鱟,刣甲屎那流', 標音.白話層)
	print(音)

