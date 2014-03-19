from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zzglzx.views.home', name='home'),
    # url(r'^zzglzx/', include('zzglzx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^workingTrends/', include('apps.workingTrends.urls')),
	url(r'^educationLoans/', include('apps.educationLoans.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
)

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += patterns('',
    	url(r"^media/(?P<path>.*)$","django.views.static.serve",{"document_root": settings.MEDIA_ROOT,}),
)