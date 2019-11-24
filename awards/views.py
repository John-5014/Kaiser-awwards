from django.shortcuts import render,redirect
import datetime as dt
from django.http import HttpResponse,Http404
from .models import *
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import ProfileSerializer, ProjectSerializer
# from rest_framework import status
# from .permissions import IsAdminOrReadOnly


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  date = dt.date.today()
  awards = Project.objects.all()
  current_user = request.user
  projects = Project.objects.order_by('-overall').all()
  top = projects[0]
  runners=Project.objects.all()[:4]

  return render(request,'main/index.html',{"date":date,"awards":awards,})


def convert_dates(dates):

  # Function that gets the weekday number for the date.
  day_number = dt.date.weekday(dates)
  days = ['Monday','Tuesday','Wednesday','Thursday''Friday','Saturday',"Sunday"]
  # Returning the actual day of the week
  day = days[day_number]
  return day

def profile(request):
  current_user = request.user
  profile = Profile.objects.get(user=current_user)
  projects =  Project.objects.filter(user=current_user)
  my_profile = Profile.objects.get(user=current_user)
  return render(request,'profile.html',locals())

@login_required(login_url='/accounts/login')
def edit_profile(request):
  current_user = request.user
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      prof = form.save(commit=False)
      prof.user = current_user
      prof.save()
      return redirect('profile')
  else:
    form = ProfileForm()
  return render(request, 'edit_profile.html',{'form':form,'profile':profile})
    
