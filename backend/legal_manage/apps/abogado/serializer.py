from django.contrib.auth.models import User
from .models.abogado import Abogado
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    abogado = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'abogado', ]