from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('galleries/<str:name>/', views.gallery_view),
    path('galleries/', views.GalleriesView.as_view(), name='galleries'),
    path('gallery/get_picture/<int:num>/', views.picture_view),
    path('galleries/add-gallery', views.add_gallery),
    path('galleries/<str:name>/delete', views.delete_gallery),
    path('gallery/<str:name>/delete-picture/<int:pk>', views.delete_picture),
    path('accounts/login/', views.LoginUser.as_view()),
    path('accounts/logout/', views.logout_view),
    path('galleries/<str:name>/add-picture', views.add_picture, name='login')
]