from django.shortcuts import render
from PIL import Image

from models import Tab

def list(request,name):
	if name=='all':
		li=Tab.objects.all()
	else:
		li=Tab.objects.filter(category=name)
	li2=Tab.objects.order_by('visted').all()[0:10]
	li3=Tab.objects.all()[0:10]
	return render(request,'WorkingTrends/templates/list.html',{'li':li,'li2':li2,'li3':li3})

def detail(request,id):
	item=Tab.objects.get(id=id)
	return render(request,'WorkingTrends/templates/detail.html',{'item':item})