from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','apps.home.views.home', name='home'),
    # url(r'^zzglzx/', include('zzglzx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^workingTrends/', include('apps.WorkingTrends.urls')),
    url(r'^compensation/', include('apps.Compensation.urls')),
	url(r'^educationLoans/', include('apps.EducationLoans.urls')),
    url(r'^fundedprojects/', include('apps.FundedProjects.urls')),
    url(r'^fundedprojects/', include('apps.WorkStudy.urls')),
    url(r'^medicalinsurance/', include('apps.MedicalInsurance.urls')),
    url(r'^onlineq/', include('apps.OnlineQ.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
)


#####media and static
from django.conf import settings


if settings.DEBUG:
    urlpatterns += patterns('',
    	url(r"^media/(?P<path>.*)$","django.views.static.serve",{"document_root": settings.MEDIA_ROOT,}),
)



urlpatterns += patterns((''),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT},name='static'
    ),
)