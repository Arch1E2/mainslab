from django.db import models


class Bill(models.Model):
    client_name = models.CharField(max_length=100, blank=True, null=True)
    client_org = models.CharField(max_length=100, blank=True, null=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    sum = models.FloatField(null=True, blank=True)
    service = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.number} {self.date}'