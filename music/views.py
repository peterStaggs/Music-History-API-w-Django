from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import viewsets

class JSONResponse(HttpResponse):
    """
    purpose: An HttpResponse that renders its content into JSON.
    Methods: __init__
        purpose: initialize a new instnce of JSON response
        arguments: 
        self- reference to the class instance being created
        data- request data
        kwargs- setting contenty type to application/json
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all().order_by('Name')
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all().order_by('Name')
    serializer_class = AlbumSerializer

class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all().order_by('Name')
    serializer_class = GenreSerializer

class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all().order_by('Title')
    serializer_class = SongSerializer
