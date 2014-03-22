# -*- coding: utf-8 -*-
from django.shortcuts import render
from PIL import Image

from models import Tab

def list(request,name):
	if name=='all':
		li=Tab.objects.all()
	else:
		li=Tab.objects.filter(category=name)
	c={'all':u'所有','xggg':'相关公告','gzdt':'工作动态','zzzc':'资助政策','bszn':'办事指南','zpxx':'招聘信息','qgzx':'勤工助学','wdxz':'文档下载','other':'其他'}
	tag=c[name]
	return render(request,'WorkStudy/templates/list.html',{'li':li,'tag':tag})



def detail(request,id):
	item=Tab.objects.get(id=id)
	return render(request,'WorkStudy/templates/detail.html',{'item':item})