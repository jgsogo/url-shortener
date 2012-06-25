from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'shortener.views.index'),
    (r'^submit/$', 'shortener.views.submit'),
    (r'^(?P<base62_id>\w+)$', 'shortener.views.follow'),
    (r'^info/(?P<base62_id>\w+)$', 'shortener.views.info'),

)
