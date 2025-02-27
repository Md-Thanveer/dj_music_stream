from django.db import models

class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100, unique=True)
    image_path = models.ImageField(upload_to='media/company', null=True, blank=True, default='no_image_available.png')

    def __str__(self):
        return self.company_name


class Song(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    image_path = models.ImageField(upload_to='media/song_cover', null=True, blank=True, default='no_image_available.png')
    song_path = models.FileField(upload_to='media/song', null=True, blank=True, default='no_image_available.png')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
