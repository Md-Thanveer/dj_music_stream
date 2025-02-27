from django.contrib import admin
from django.utils.html import format_html

from backend.models import Genre, Company, Song

# Register your models here.
admin.site.register(Genre)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name','image_tag')

    def image_tag(self,obj):
        return format_html('<img src="{}" width="150" height="150"'.format(obj.image_path.url))
admin.site.register(Company,CompanyAdmin)

admin.site.register(Song)