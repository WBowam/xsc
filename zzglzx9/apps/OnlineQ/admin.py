from django.contrib import admin
from models import Tab




class TabAdmin(admin.ModelAdmin):
	search_fields=('question','category','content')
	list_display = ('id','question', "category",  "upTime",'edittime','publish')
	list_display_links = ("id",'question', "category",  "upTime",'edittime','publish')
	ordering = ("-upTime",)

admin.site.register(Tab,TabAdmin)