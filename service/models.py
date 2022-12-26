from django.db import models

# Create your models here.
# class Artist(models.Model):
#     artist_img = models.CharField(max_length=50)
#     artist_name = models.

class Service(models.Model):
    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    service_desc = models.TextField()

