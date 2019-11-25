from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

# Create your models here.
class Profile(models.Model):
  pic = models.ImageField(upload_to = 'profiles/')
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  bio = models.CharField(max_length=255, null=True)
  nickname = models.CharField(max_length=45,null=True)
  email = models.EmailField(max_length=255)

  def __str__(self):
    return self.nickname
  
  def save(self):
    super().save()

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
      output_size = (300,300)
      img.tumbnail(output_size)
      img.save(self.image.path)