from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

# Create your models here.
class Profile(models.Model):
  pic = models.ImageField(default = 'download.jpg',upload_to = 'profiles/')
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  bio = models.CharField(max_length=255, null=True)
  nickname = models.CharField(max_length=45,null=True)
  email = models.EmailField(max_length=255,null =True)

  def __str__(self):
    return self.nickname if self.nickname else self.user.username
  
  def save(self):
    super().save()

    img = Image.open(self.pic.path)

    if img.height > 300 or img.width > 300:
      output_size = (300,300)
      img.thumbnail(output_size)
      img.save(self.pic.path)