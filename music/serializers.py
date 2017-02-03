from rest_framework import serializers
from music.models import *



class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'url', 'Name',)

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'url', 'Name', 'Label', 'Year_Released', 'artist_id',)

class GenreSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Genre 
        fields = ('id', 'url', 'Name',) 

class SongSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Song
        fields = ('id', 'url', 'Title', 'artist_id', 'album_id', 'genre_id',) 