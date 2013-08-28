from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=30)

    def __unicode__(self):
        return self.status


class Vacation(models.Model):
    user = models.ForeignKey('custom_user.CustomUser')
    fromdate = models.DateField()

    todate = models.DateField()
    #who will take place....
    reason = models.TextField()
    status = models.ManyToManyField(Status)

    def __unicode__(self):
        return "from {0} to {1} status {2}".format(self.fromdate, self.todate, self.user)

