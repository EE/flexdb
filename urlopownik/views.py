from django.http import HttpResponse
from django.views.generic import View, TemplateView
import json
from urlopownik.models import Vacation, Status
from custom_user.models import CustomUser
from datetime import date


class UrlopownikAdd(View):
    def post(self, request):
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
    def get(self, request):

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


class UrlopownikAcceptstatus(View):
    def get(self, request):

        #TODO zamienic na uprawnienia accept a nie na logowanie, po merge Borysa
        if request.user.is_authenticated:
            status = Status.objects.all()
            statuses = []
            for x in status:
                statuses.append(x.status)
            return HttpResponse(
                json.dumps({
                    "status": statuses
                }),
                content_type="application/json"
            )


class UrlopownikAcceptfind(View):
    """
    Wyszukiwarka prosb o urlop

    """
    def post(self, request):

        #TODO zamienic na uprawnienia accept a nie na logowanie, po merge Borysa
        if request.user.is_authenticated:
            data = json.loads(request.body)
            status = Status.objects.filter(status=data['searchstatus'].split()[0])
            vacations = Vacation.objects.filter(status=status)

            return HttpResponse(
                json.dumps({
                    "reason": dict([(x, vacations[x].reason) for x in range(0, len(vacations))]),
                    "user": dict([(x, vacations[x].user.username) for x in range(0, len(vacations))]),
                    "pk": dict([(x, vacations[x].pk) for x in range(0, len(vacations))]),
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
                    "length": len(vacations),
                    "status": data['searchstatus'].split()[0]
                }),
                content_type="application/json"
            )


class UrlopownikChangeStatus(View):
    """
    Akceptowanie/lub odrzucanie prosb o urlop

    """
    def post(self, request):
        #TODO zamienic na uprawnienia accept a nie na logowanie, po merge Borysa
        if request.user.is_authenticated:
            data = json.loads(request.body)
            status = Status.objects.filter(status=data['status'].split()[0])
            vacations = Vacation.objects.get(pk=data['pk'])
            vacations.status = status[0]
            vacations.save()
            return HttpResponse(
                content_type="application/json"
            )

