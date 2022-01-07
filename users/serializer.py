from rest_framework.serializers import ModelSerializer, JSONField
from occupations.models import Occupation
from drf_yasg import openapi
from occupations.serializer import OccupationSerializer
from .models import User
        

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'birthday')
        