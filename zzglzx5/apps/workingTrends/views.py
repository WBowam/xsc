from django.shortcuts import render
from PIL import Image

from models import WorkingTrends
def list(request,name='all'):
	if name=='all':
		li=WorkingTrends.objects.all()
	else:
		li=WorkingTrends.objects.filter(category=name)
	return render(request,'workingTrends_list.html',{'li':li,'name':name})



def detail(request,id):
	item=WorkingTrends.objects.get(id=id)
	return render(request,'workingTrends_detail.html',{'item':item})