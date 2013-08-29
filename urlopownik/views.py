from django.http import HttpResponse
from django.views.generic import View, TemplateView
import json
from urlopownik.models import Vacation, Status
from custom_user.models import CustomUser
from datetime import date


class Urlopownik(TemplateView):
    template_name = "urlopownik/index.html"


class UrlopownikAdd(View):
    def post(self, request, *args, **kwargs):
        ok = False
        if request.user.is_authenticated:
            ok = True
            data = json.loads(request.body)
            fromdate = date(int(data["fromyear"]), int(data["frommonth"]), int(data["fromday"]))
            todate = date(int(data["toyear"]), int(data["tomonth"]), int(data["today"]))
            user = CustomUser.objects.get(username=request.user.username)
            status = Status.objects.get(pk=1)
            add = Vacation(user=user, fromdate=fromdate, todate=todate, reason=data["reason"], status=status)
            add.save()

        return HttpResponse(
            json.dumps(dict(ok=ok)),
            content_type="application/json"
        )


class UrlopownikWatch(View):
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            user = CustomUser.objects.get(username=request.user.username)
            vacations = Vacation.objects.filter(user=user)

            return HttpResponse(
                json.dumps({
                    "reason": dict([(x, vacations[x].reason) for x in range(0, len(vacations))]),
                    "fromday": dict([(x, vacations[x].fromdate.day)
                                     for x in range(0, len(vacations))]),
                    "today": dict([(x, vacations[x].todate.day)
                                   for x in range(0, len(vacations))]),
                    "frommonth": dict([(x, vacations[x].fromdate.month)
                                       for x in range(0, len(vacations))]),
                    "tomonth": dict([(x, vacations[x].todate.month)
                                     for x in range(0, len(vacations))]),
                    "fromyear": dict([(x, vacations[x].fromdate.year)
                                      for x in range(0, len(vacations))]),
                    "toyear": dict([(x, vacations[x].todate.year)
                                    for x in range(0, len(vacations))]),
                    "length": len(vacations)
                }),
                content_type="application/json"
            )


