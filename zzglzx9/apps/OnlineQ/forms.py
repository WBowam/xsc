from django.forms import ModelForm
from models import Tab



class TabForm(ModelForm):
    
    class Meta:
        model = Tab
        exclude = ["answer",'id', "category",  "upTime",'edittime','publish','photo','attachment']