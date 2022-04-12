from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('galleries/<str:name>/', views.gallery_view),
    path('galleries/', views.GalleriesView.as_view(), name='galleries'),
    path('gallery/getpicture/<int:num>/', views.picture_view),
    path('accounts/login/', views.LoginUser.as_view()),
    path('galleries/<str:name>/add-picture', views.add_picture, name='login')
]