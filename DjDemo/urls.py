from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.index'),
    url(r'^login', 'core.views.login'),
    url(r'^detail', 'core.views.detail'),
    url(r'^demo', 'core.views.demo'),
    url(r'^logout', 'core.views.logout'),
    url(r'^blogs', 'core.views.blogs'),
    url(r'^new_blog', 'core.views.new_blog'),
) 

# if settings.DEBUG:
urlpatterns += patterns('',
                             url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': '../static'}),
                             )
