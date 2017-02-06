from django.db import models 

# Build model, which creates a table with specified fields.  

class Artist(models.Model): 
	Name = models.CharField(max_length=50, default='')

	class Meta:
		ordering = ('Name',)

# Return fields as objects using .format
	def __str__(self):
		return '{}'.format(self.Name)


class Album(models.Model): 
	Name = models.CharField(max_length=50, default='') 
	Label = models.CharField(max_length=50, default='')
	Year_Released = models.CharField(max_length=4, default='')
	# bring in FK from Artist like so:
	artist = models.ForeignKey(Artist, null=True)

	class Meta: 
		ordering = ('Name', 'Label', 'Year_Released', 'artist')

	def __str__(self):
		return '{} {} {} {}'.format(self.Name, self.Label, self.Year_Released, self.artist)


class Genre(models.Model): 
	Name = models.CharField(max_length=25, default='') 

	class Meta: 
		ordering = ('Name',) 

	def __str__(self):
		return '{}'.format(self.Name)

class Song(models.Model): 
	Title = models.CharField(max_length=70, default='') 
	artist = models.ForeignKey(Artist, null=True)
	album = models.ForeignKey(Album, null=True)
	genre = models.ForeignKey(Genre, null=True)

	class Meta: 
		ordering = ('Title', 'artist', 'album', 'genre')

	def __str__(self):
		return '{} {} {} {}'.format(self.Title, self.artist, self.album, self.genre)








