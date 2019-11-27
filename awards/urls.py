from django.conf.urls import url
from . import views
from .views import ProjectListView,ProjectDetailView
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$',ProjectListView.as_view(),name = 'index'),
  url(r'^project/(\d+)',views.project,name='project-detail'),
  url(r'^project/new$', views.post,name='post'),
  url(r'^search/', views.search_results,name= 'search'),
  
]

if settings.DEBUG:

  urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)