from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^flexdb/', include('flexdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('main_page.urls')),
    url(r'^accounts/', include('custom_user.urls')),
    url(r'', include('social_auth.urls')),
)

for x in settings.FLEXDB_APPS:
    urlpatterns += patterns('',
        url(r'^'+x+'/', include(x+'.urls')),
    )
