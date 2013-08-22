from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import logout
from flexdb import settings
import json


class Index(TemplateView):
    template_name = "flexdb/index.html"


class Ajax(TemplateView):
    def get(self, request):
        data={'apps': settings.INSTALLED_APPS}
        return HttpResponse(json.dumps(data),content_type="application/json")


def logout_view(request):
    logout(request)
    return HttpResponse('ok')
