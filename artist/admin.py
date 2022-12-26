from django.contrib import admin
from artist.models import Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display=('artist_name','artist_tag','artist_img')

admin.site.register(Artist,ArtistAdmin)