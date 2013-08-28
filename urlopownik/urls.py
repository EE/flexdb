from urlopownik.views import Urlopownik, UrlopownikAdd, UrlopownikWatch
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', Urlopownik.as_view()),
    url(r'^add/$', UrlopownikAdd.as_view()),
    url(r'^watch/$', UrlopownikWatch.as_view()),
)

