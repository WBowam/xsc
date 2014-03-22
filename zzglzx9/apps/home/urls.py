from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zzglzx.views.home', name='home'),
    # url(r'^zzglzx/', include('zzglzx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	#url(r'^admin/', include(admin.site.urls)),
	url(r'^list/(?P<name>[^/]+)/$',list, name='list'),
	url(r'detail/(?P<id>[^/]+)/$',detail,name='detail'),
	url(r'tian/$',tian,name='tian'),
)
