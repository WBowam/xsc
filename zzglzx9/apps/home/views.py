# -*- coding: utf-8 -*-
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
	W=W_Tab.objects.all()[0:2]
	#E=E_Tab.objects.filter(category='gztd')[0:3]
	F=F_Tab.objects.filter(category='gzdt')[0:2]
	WS=WS_Tab.objects.filter(category='gzdt')[0:2]
	M=M_Tab.objects.filter(category='gzdt')[0:2]
	C=C_Tab.objects.filter(category='gzdt')[0:2]
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
def tian(request):
	t=W_Tab(title='武汉大学医疗保险及公费报销领款名单',content='以下同学在近期内凭身份证和学生证到学生资助中心(工学部团委一楼)领取到账款项。如他人带领，请同时携带领取人的身份证。详情请咨询学生资助管理中心68772014.经济与管理学院   05级    王  峮新闻与传播学院   05级    孙  欣数学与统计学院   05级    邢周华水利水电学院     05级    李文娟电子信息学院     05级    文  舰    如有同学认识以上同学，请麻烦转告')
	t.save()
	return render(request,'index.html')
'''


















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