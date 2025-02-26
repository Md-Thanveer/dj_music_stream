from django.contrib import admin

from backend.models import Genre, Company, Song

# Register your models here.
admin.site.register(Genre)
admin.site.register(Company)

admin.site.register(Song)