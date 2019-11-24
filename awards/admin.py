from django.contrib import admin
from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  filter_horizontal = ('technologies', 'categories')


admin.site.register(Project)
admin.site.register(categories)
admin.site.register(technologies)
admin.site.register(Profile)


