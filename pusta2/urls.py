from django.conf.urls import patterns, url
from pusta2.views import view2


urlpatterns = patterns('',
    url(r'^', view2, name='view2'),
)
