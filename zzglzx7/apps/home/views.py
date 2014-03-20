from django.shortcuts import render
from PIL import Image

from models import Tab
##importing models
from apps.WorkingTrends.models import Tab as W_Tab
from apps.EducationLoans.models import Tab as E_Tab
from apps.FundedProjects.models import Tab as F_Tab
from apps.WorkStudy.models import Tab as WS_Tab
from apps.MedicalInsurance.models import Tab as M_Tab
##models end


def home(request):
	Working_Trends=WorkingTrends_all(request)
	return render(request,'index.html',{' workingtrends':Working_trends})

#from  WorkingTrends,EducationLoans,FundedProjects,WorkStudy,MedicalInsurance
def WorkingTrends_all(request):
	list_all=[
	W_Tab.objects.all(),
	E_Tab.objects.all(),
	F_Tab.objects.all(),
	WS_Tab.objects.all(),
	M_Tab.objects.all()
	]
	one=one(list_all)
	return one

def one(list_all):
	for query in list_all:
		one=two(query)

def two(list_all):
	pass

























'''

def list(request,name):
	if name=='all':
		li=Tab.objects.all()
	else:
		li=Tab.objects.filter(category=name)

	return render(request,'EducationLoans/templates/list.html',{'li':li})



def detail(request,id):
	item=Tab.objects.get(id=id)
	return render(request,'EducationLoans/templates/detail.html',{'item':item})


	'''