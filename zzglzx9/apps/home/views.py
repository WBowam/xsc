from django.shortcuts import render
#from PIL import Image

##importing models
from apps.WorkingTrends.models import Tab as W_Tab
from apps.EducationLoans.models import Tab as E_Tab
from apps.FundedProjects.models import Tab as F_Tab
from apps.WorkStudy.models import Tab as WS_Tab
from apps.MedicalInsurance.models import Tab as M_Tab
from apps.Compensation.models import Tab as C_Tab
##models end


def home(request):

	return render(
		request,'index.html',{
		'W':W_Tab.objects.all()[0:3],
		'E':E_Tab.objects.all()[0:2],
		'F':F_Tab.objects.all()[0:2],
		'WS':WS_Tab.objects.all()[0:1],
		'M':M_Tab.objects.all()[0:1],
		'C':C_Tab.objects.all()[0:1]}
		)

#from  WorkingTrends,EducationLoans,FundedProjects,WorkStudy,MedicalInsurance

























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