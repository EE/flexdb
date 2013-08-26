from django.conf.urls import patterns, include, url
from main_page.views import Index, logout_view, ModalError


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view()),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^error/$', ModalError.as_view()),
    # url(r'^flexdb/', include('flexdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
