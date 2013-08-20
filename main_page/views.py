from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import logout



class Index(TemplateView):
    template_name = "flexdb/index.html"

def logout_view(request):
    logout(request)
    return HttpResponse('ok')
