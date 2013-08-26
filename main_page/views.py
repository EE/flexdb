from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings
import json


class Index(TemplateView):
    template_name = "flexdb/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['apps'] = settings.FLEXDB_APPS
        return context


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class ModalError(TemplateView):
    template_name = "flexdb/modalerror.html"
