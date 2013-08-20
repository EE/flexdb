from django.views.generic import TemplateView, View
from django.http import HttpResponse
from custom_user.models import CustomUser
from django.test.client import Client
import json


class Index(TemplateView):
    template_name = "flexdb/index.html"


class GetUserDataView(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated():

            data = {'userid': self.request.user.id,
                    'Logged': True}
        else:
            data = {'Logged': False}

        data = json.dumps(data)
        return HttpResponse(data)
