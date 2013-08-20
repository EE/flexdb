from django.views.generic import TemplateView, View
from django.http import HttpResponse
from custom_user.models import CustomUser
from django.test.client import Client
import json


class Index(TemplateView):
    template_name = "flexdb/index.html"
