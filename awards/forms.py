from django import forms
from .models import *


class UploadForm(forms.ModelForm):

  class Meta:

    model = Project
    exclude = ('design', 'usability', 'creativity','content', 'overall', 'posted', 'user' )




# class ProfileForm(forms.ModelForm):
#   class Meta:
#     model = Profile
#     fields = ('pic','bio', 'nickname','email')

# class RatingForm(forms.ModelForm):
#   class Meta:
#     model=Rating
#     exclude=['overall_score','profile','project']