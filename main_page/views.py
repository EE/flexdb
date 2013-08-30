from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings
from flexdb.utils import get_config


class Index(TemplateView):
    template_name = "flexdb/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['apps'] = settings.FLEXDB_APPS
        context['js'] = []
        context['css'] = []
        context['templates'] = {}
        context['permissions'] = {}
        for x in context['apps']:
            config = get_config(x)
            context['js'] += config.js()
            context['css'] += config.css()
            context['templates'][config.app_name] = config.templates()
        return context


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class ModalError(TemplateView):
    template_name = "flexdb/modalerror.html"
