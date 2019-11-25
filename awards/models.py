from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime as dt

# Create your models here.




class categories(models.Model):
  categories = models.CharField(max_length=70)

  def __str__(self):
    return self.categories

  def save_category(self):
    self.save()

  @classmethod
  def delete_category(cls,categories):
    cls.objects.filter(categories=categories).delete()

class technologies(models.Model):
  technologies = models.CharField(max_length=100)

  def __str__(self):

    return self.technologies

  def save_technology(self):
    self.save()

  @classmethod
  def delete_technology(cls,technologies):
    cls.objects.filter(technologies=technologies).delete()




class Project(models.Model):
  landing_page = models.ImageField(null=True, upload_to='landing/')
  title = models.CharField(max_length = 30)
  description =  models.TextField(max_length=400)
  country = CountryField(multiple=True)
  link = models.CharField(max_length=255)
  design = models.IntegerField(blank=True,default=0)
  usability = models.IntegerField(blank=True,default=0)
  creativity = models.IntegerField(blank=True,default=0)
  content = models.IntegerField(blank=True,default=0)
  overall = models.IntegerField(blank=True,default=0)
  categories = models.ManyToManyField(categories)
  technologies = models.ManyToManyField(technologies)
  posted  = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)



  def __str__(self):

    return self.title

  class Meta:
    ordering = ['title']

