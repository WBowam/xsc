from django.contrib import admin
from apps.educationLoans.models import EducationLoans




class EducationAdmin(admin.ModelAdmin):
	search_fields=('title','category','content')
	list_display = ('id','title', "category",  "upTime")
	list_display_links = ("id",'title', "category",  "upTime")
	ordering = ("-upTime",)

admin.site.register(EducationLoans,EducationAdmin)


