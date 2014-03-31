/# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 臺灣言語資料庫服務.服務 import 服務

__服務=服務()
urlpatterns = patterns('',
	url(r'^自動標音/(?P<查詢腔口>[^/]+)/(?P<查詢語句>.+)$', __服務.自動標音, name='自動標音'),
	url(r'^語音合成/(?P<查詢腔口>[^/]+)/(?P<集選擇字串>[0-9,]+)/(?P<查詢語句>.+)$', __服務.語音合成, name='語音合成'),
	url(r'^翻譯國語/(?P<查詢腔口>[^/]+)/(?P<查詢語句>.+)$', __服務.翻譯國語, name='翻譯國語'),
	url(r'^翻譯合成/(?P<查詢腔口>[^/]+)/(?P<集選擇字串>[0-9,]+)/(?P<查詢語句>.+)$', __服務.翻譯合成, name='翻譯合成'),
)