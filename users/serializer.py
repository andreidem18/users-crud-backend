from rest_framework.serializers import ModelSerializer
from occupations.models import Occupation
from occupations.serializer import OccupationSerializer

from phones.models import Phone
from .models import User

class PhoneSerializer(ModelSerializer):
    class Meta: 
        model = Phone
        fields = ('id', 'phone', 'type')
        

class UserSerializer(ModelSerializer):
    phones = PhoneSerializer(read_only=True, many=True)
    occupation = OccupationSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'birthday', 'occupation', 'phones')
        
        
# class CreateUserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'first_name', 'last_name', 'birthday', 'occupation', 'phones')
        