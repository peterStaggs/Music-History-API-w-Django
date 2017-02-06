from rest_framework import serializers
from music.models import *

# Use Hyperlinked serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        # Include 'url' for a clickable Detail view of specific items in the browser GUI
        fields = ('id', 'url', 'Name',)

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'url', 'Name', 'Label', 'Year_Released', 'artist',)

class GenreSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Genre 
        fields = ('id', 'url', 'Name',) 

class SongSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Song
        fields = ('id', 'url', 'Title', 'artist', 'album', 'genre',) 