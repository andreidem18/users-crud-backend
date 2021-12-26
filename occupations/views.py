from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import OccupationSerializer
from .models import Occupation

@api_view(['GET'])
def occupations(request):
    occupations = Occupation.objects.all()
    serialized = OccupationSerializer(occupations, many = True)
    return Response(serialized.data)
