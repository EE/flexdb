from urlopownik.views import urlopownik
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^', urlopownik, name='urlopownik'),
)
