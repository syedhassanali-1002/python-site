from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_tag = models.CharField(max_length=100)
    artist_img = models.FileField(upload_to="artist/", max_length=250,null=True,default=None)
# Create your models here.
