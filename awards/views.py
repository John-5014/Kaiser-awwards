from django.shortcuts import render,redirect
import datetime as dt
from django.http import HttpResponse,Http404
from .models import *
# from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UploadForm
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import ProfileSerializer, ProjectSerializer
# from rest_framework import status
# from .permissions import IsAdminOrReadOnly


# Create your views here.
# @login_required(login_url='/accounts/login/')
@login_required
def index(request):
  date = dt.date.today()
  awards = Project.objects.all()
  # current_user = request.user
  # projects = Project.objects.order_by('-overall').all()
  

  return render(request,'main/index.html',{"date":date,"awards":awards,})

def post(request):
  current_user = request.user
  project = Project.objects.all()
  if request.method == 'POST':

    form = UploadForm(request.POST, request.FILES)

    if form.is_valid():
      pic = form.save(commit=False)
      pic.user = current_user
      pic.save()
      return redirect('index')

  else:
    
    form = UploadForm()
    return render(request, 'new_project.html',{'form':form,'project':project})
        


def convert_dates(dates):
# Function that gets the weekday number for the date.
  day_number = dt.date.weekday(dates)
  days = ['Monday','Tuesday','Wednesday','Thursday''Friday','Saturday',"Sunday"]
  # Returning the actual day of the week
  day = days[day_number]
  return day



def project(request,project_id):
  projo = Project.objects.all()
  try:
    project = Project.objects.get(id = project_id)
  except DoesNotExist:
    raise Http404()
  return render(request,"main/project_detail.html",{"project":project})

def search_results(request):
  if 'search' in request.GET and request.GET["search"]:
    search_term = request.GET.get("search")
    searched_project = Project.search_project(search_term)
    message = f"Search results for: {search_term}"

    return render(request, ' search.html', {"message":message, "users":searched_project})

  else:
    message="You haven't searched for any term."
    return render(request,'search.html',{"message":message})







class ProjectListView(ListView):
  model = Project
  template_name = 'main/index.html'
  context_object_name = 'awards'
  ordering = ['-posted']

class ProjectDetailView(DetailView):
  model = Project
  
  





    
