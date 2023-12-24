from django.db import models

# Create your models here.
class Edit_menu(models.Model):
    profile_picture = models.ImageField(default="",upload_to='profile_picture/')
    