from django.shortcuts import render
from PIL import Image

from models import EducationLoans
def list(request,name):
	if name=='all':
		li=EducationLoans.objects.all()
	else:
		li=EducationLoans.objects.filter(category=name)

	return render(request,'educationLoans_list.html',{'li':li})



def detail(request,id):
	item=EducationLoans.objects.get(id=id)
	return render(request,'educationLoans_detail.html',{'item':item})