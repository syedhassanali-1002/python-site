from django.db import models

class Enquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    description = models.TextField()

# Create your models here.
