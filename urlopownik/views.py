from django.http import HttpResponse
from django.shortcuts import render_to_response


def urlopownik(request):
    return render_to_response(
        'urlopownik/index.html'
    )
