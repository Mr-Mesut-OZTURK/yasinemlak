from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import EmlakKayit


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class EmlakSerializer(serializers.ModelSerializer):
    # images = serializers.ImageField()
    class Meta:
        model = EmlakKayit
        fields = "__all__"