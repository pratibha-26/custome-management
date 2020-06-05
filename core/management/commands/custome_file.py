from core.models import User, Activityperiod
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Insert dummy data here"""
    help = 'Create random data'

    def handle(self, *args, **kwargs):
        """Insert dummy data here"""
        User.objects.create(id='W012HjMA3CDE', real_name='Egon Spengler', tz='America/LOS_Angeles').save()
        User.objects.create(id='W012AhMa3CDE', real_name='Spen Spengler', tz='America').save()
        Activityperiod.objects.create(start_time='2020-01-10', end_time='2019-01-11').save()
        Activityperiod.objects.create(start_time='2019-01-12', end_time='2019-01-10').save()
