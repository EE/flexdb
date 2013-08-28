from django.contrib import admin
from urlopownik.models import Status, Vacation


class StatusAdmin(admin.ModelAdmin):
    model = Status


class VacationAdmin(admin.ModelAdmin):
    model = Vacation


admin.site.register(Vacation, VacationAdmin)
admin.site.register(Status, StatusAdmin)
