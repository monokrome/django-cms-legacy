from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

# A few settings that we can use to override the index page
index_view = getattr(settings, 'INDEX_VIEW', 'news.views.index')
index_args = getattr(settings, 'INDEX_ARGS', {})

urlpatterns = patterns('',
    url(r'^$', index_view, index_args, name='site-index'),

    url(r'^news/', include('news.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

