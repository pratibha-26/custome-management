from rest_framework import serializers
from .models import User, Activityperiod


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activityperiod
        fields = ['start_time', 'end_time']
