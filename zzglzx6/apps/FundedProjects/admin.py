from django.contrib import admin
from models import Tab




class TabAdmin(admin.ModelAdmin):
	search_fields=('title','category','content')
	list_display = ('id','title', "category",  "upTime",'visted')
	list_display_links = ("id",'title', "category",  "upTime",'visted')
	ordering = ("-upTime",)

admin.site.register(Tab,TabAdmin)