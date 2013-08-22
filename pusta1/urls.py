from django.conf.urls import patterns, url
from pusta1.views import view1


urlpatterns = patterns('',
    url(r'^', view1, name='view1'),
)
