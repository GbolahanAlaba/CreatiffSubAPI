from rest_framework import serializers
from .models import *

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['id', 'Name', 'Email'] 