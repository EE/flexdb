from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s " % self.status


class Vacation(models.Model):
    user = models.ForeignKey('custom_user.CustomUser')
    fromdate = models.DateField()

    todate = models.DateField()
    #who will take place....
    reason = models.TextField()
    status = models.ManyToManyField(Status)

    def __unicode__(self):
        return "from %s to %s status %s" % (self.fromdate, self.todate, self.user)

