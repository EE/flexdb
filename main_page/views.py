from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings
import json


class Index(TemplateView):
    template_name = "flexdb/index.html"


class LoadAjaxApplication(View):
    def get(self, request):
        data = {'apps': settings.ADDITIONAL_APPS}
        return HttpResponse(json.dumps(data), content_type="application/json")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
