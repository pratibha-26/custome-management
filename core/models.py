from django.db import models


class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    real_name = models.CharField(max_length=80)
    tz = models.CharField(max_length=80)


class Activityperiod(models.Model):
    start_time = models.DateField(blank=False)
    end_time = models.DateField(blank=False)
