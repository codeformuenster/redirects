from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^(?P<slug>\w+)/$', 'redirect.views.redirect', name='redirect'),
    #url(r'^(?P<slug>\w+)$', 'redirect.views.redirect', name='redirect'),
    # url(r'^blog/', include('blog.urls')),
)
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)