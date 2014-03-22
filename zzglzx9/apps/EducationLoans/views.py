# -*- coding: utf-8 -*-
from django.shortcuts import render
from PIL import Image

from models import Tab

def list(request,name):
	if name=='all':
		li=Tab.objects.all()
	else:
		li=Tab.objects.filter(category=name)
	c={'all':u'所有','zzgl':'资助管理','qgzx':'勤工助学','zxdk':'助学贷款','ylbx':'医疗保险','bcdc':'补偿贷偿','other':'其他'}
	tag=c[name]
	return render(request,'EducationLoans/templates/list.html',{'li':li,'tag':tag})

def detail(request,id):
	item=Tab.objects.get(id=id)
	return render(request,'EducationLoans/templates/detail.html',{'item':item})