from django.shortcuts import render
from PIL import Image

from models import Tab

def list(request,name):
	if name=='all':
		li=Tab.objects.all()
	else:
		li=Tab.objects.filter(category=name)

	return render(request,'FundedProjects/templates/list.html',{'li':li})



def detail(request,id):
	item=Tab.objects.get(id=id)
	return render(request,'FundedProjects/templates/detail.html',{'item':item})