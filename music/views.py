from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Songs
from rest_framework import status
from .serializers import SongSerializer
from music import serializers

@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        music = Songs.objects.all()
        serializer = SongSerializer(music, many=True)
        return Response(serializer.data)

# Create your views here.
