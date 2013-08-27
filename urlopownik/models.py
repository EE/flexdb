from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=30)


class Vacation(models.Model):
    user = models.ForeignKey('custom_user.CustomUser')
    fromdate = models.DateField()
    todate = models.DateField()
    #who will take place....
    reason = models.TextField()
    status = models.ManyToManyField(Status)
