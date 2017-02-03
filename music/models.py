from django.db import models

class Artist(models.Model): 
	Name = models.CharField(max_length=50, default='')

	class Meta:
		ordering = ('Name',)

	def __str__(self):
		return '{}'.format(self.Name)


class Album(models.Model): 
	Name = models.CharField(max_length=50, default='') 
	Label = models.CharField(max_length=50, default='')
	Year_Released = models.CharField(max_length=4, default='')
	artist_id = models.ForeignKey(Artist, null=True)

	class Meta: 
		ordering = ('Name', 'Label', 'Year_Released', 'artist_id')

	def __str__(self):
		return '{} {} {} {}'.format(self.Name, self.Label, self.Year_Released, self.artist_id)


class Genre(models.Model): 
	Name = models.CharField(max_length=25, default='') 

	class Meta: 
		ordering = ('Name',) 

	def __str__(self):
		return '{}'.format(self.Name)

class Song(models.Model): 
	Title = models.CharField(max_length=70, default='') 
	artist_id = models.ForeignKey(Artist, null=True)
	album_id = models.ForeignKey(Album, null=True)
	genre_id = models.ForeignKey(Genre, null=True)

	class Meta: 
		ordering = ('Title', 'artist_id', 'album_id', 'genre_id')

	def __str__(self):
		return '{} {} {} {}'.format(self.Title, self.artist_id, self.album_id, self.genre_id)








