from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('galleries/<str:name>/', views.gallery_view),
    path('galleries/', views.GalleriesView.as_view(), name='galleries'),
]