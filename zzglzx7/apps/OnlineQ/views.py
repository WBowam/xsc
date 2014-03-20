from django.shortcuts import render
from django.http import HttpResponseRedirect
from PIL import Image
from forms import *
from models import Tab

def list(request,name):
	if name=='all':
		li=Tab.objects.all()
	else:
		li=Tab.objects.filter(category=name)

	return render(request,'OnlineQ/templates/list.html',{'li':li})



def detail(request,id):
	item=Tab.objects.get(id=id)
	return render(request,'OnlineQ/templates/detail.html',{'item':item})




def question(request):
#    a=Author.objects.get(pk=1)
#    form=AuthorForm(instance=a)
    form=TabForm()
    if request.method=='POST':
        form=TabForm(request.POST)
        if form.is_valid():
            form.save()
            message='thanks'
            return HttpResponseRedirect('/onlineq/list/all')
    return render(request,'OnlineQ/templates/question.html',{'form':form})