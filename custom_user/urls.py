from django.conf.urls import patterns, include, url
from rest_framework import routers
from custom_user import views


router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^useredit/$', views.userEditView),
)
