from rest_framework.serializers import ModelSerializer
from .models import Occupation

class OccupationSerializer(ModelSerializer):
    class Meta:
        model = Occupation
        fields = ('id', 'occupation')
