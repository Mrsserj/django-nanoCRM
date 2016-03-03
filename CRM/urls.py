from django.conf.urls import patterns, include, url
from views import *
#import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('CRM.views',
    # Examples:
    # url(r'^$', 'benzin.views.home', name='home'),
    # url(r'^benzin/', include('benzin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', 'start', name='start'),
    url(r'^calendar/$', 'calendar', name='calendar'),
    url(r'^calendar/(?P<year>\d+)/(?P<month>\d+)/$', 'calendar', name='calendar'),
    url(r'^event/$', 'event_edit', name='event'),
    url(r'^customer/$', 'customer_edit', name='customer'),
    url(r'^customer/(?P<customer_pk>\d+)/$', 'customer_edit', name='customer'),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/login/' }, name='logout'),
)

urlpatterns += staticfiles_urlpatterns()