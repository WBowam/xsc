from django.shortcuts import render
#from PIL import Image

##importing models
from apps.WorkingTrends.models import Tab as W_Tab
from apps.EducationLoans.models import Tab as E_Tab
from apps.FundedProjects.models import Tab as F_Tab
from apps.WorkStudy.models import Tab as WS_Tab
from apps.MedicalInsurance.models import Tab as M_Tab
from apps.Compensation.models import Tab as C_Tab
from apps.OnlineQ.models import Tab as O_Tab
##models end


def home(request):
	###WorkingTrends
	W=W_Tab.objects.all()[0:3]
	E=E_Tab.objects.filter(category='gztd')[0:2]
	F=F_Tab.objects.filter(category='gzdt')[0:1]
	WS=WS_Tab.objects.filter(category='gzdt')[0:1]
	M=M_Tab.objects.filter(category='gzdt')[0:1]
	C=C_Tab.objects.filter(category='gzdt')[0:1]
	###Work guide
	F2=F_Tab.objects.filter(category='bszn')[0:4]
	WS2=WS_Tab.objects.filter(category='bszn')[0:3]
	C2=C_Tab.objects.filter(category='bszn')[0:3]

	F3=F_Tab.objects.filter(category='zzzc')[0:4]
	WS3=WS_Tab.objects.filter(category='zzzc')[0:3]
	C3=C_Tab.objects.filter(category='zzzc')[0:3]


	F4=F_Tab.objects.filter(category='xggg')[0:3]
	WS4=WS_Tab.objects.filter(category='xggg')[0:3]
	C4=C_Tab.objects.filter(category='xggg')[0:2]
	M4=M_Tab.objects.filter(category='xggg')[0:2]

	F5=F_Tab.objects.filter(category='wdxz')[0:3]
	WS5=WS_Tab.objects.filter(category='wdxz')[0:2]
	C5=C_Tab.objects.filter(category='wdxz')[0:3]
	M5=M_Tab.objects.filter(category='wdxz')[0:2]

	O6=O_Tab.objects.all()[0:10]
	dic={
		'W':W,
		'E':E,
		'F':F,
		'WS':WS,
		'M':M,
		'C':C,
		'F2':F2,
		'WS2':WS2,
		'C2':C2,
		'F3':F3,
		'WS3':WS3,
		'C3':C3,
		'C4':C4,
		'F4':F4,
		'WS4':WS4,
		'M4':M4,
		'C5':C5,
		'F5':F5,
		'WS5':WS5,
		'M5':M5,
		'O6':O6
		}
	return render(
		request,'index.html',dic
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