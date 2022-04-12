from django import forms
from django.forms import ModelForm
from .models import Picture, Gallery


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'description']


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'description', 'image']