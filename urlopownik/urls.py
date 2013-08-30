from urlopownik.views import UrlopownikAdd, UrlopownikWatch, UrlopownikAcceptstatus
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^add/$', UrlopownikAdd.as_view()),
    url(r'^watch/$', UrlopownikWatch.as_view()),
    url(r'^acceptstatus/$', UrlopownikAcceptstatus.as_view()),
)

