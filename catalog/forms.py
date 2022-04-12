from django import forms
from django.forms import ModelForm
from .models import Picture, Gallery


# class PictureForm(forms.Form):
#     title = forms.CharField(label='title', max_length=200)
#     description = forms.CharField(widget=forms.Textarea, required=False)
#     gallery = forms.ModelChoiceField(queryset=Gallery.objects.exclude(name='HomePage'))
#     upload_date = date.today()


class GalleryForm(forms.Form):
    name = forms.CharField(label='name', max_length=200)
    pictures = forms.ModelMultipleChoiceField(label='images', queryset=Picture.objects.filter(gallery=None))


class PictureForm(ModelForm):
    description_field = forms.CharField(label='Description', max_length=200, required=False)
    gallery_field = forms.ModelChoiceField(queryset=Gallery.objects.all(), empty_label=None, required=True)
    class Meta:
        model = Picture
        fields = ['title', 'gallery_field', 'description_field', 'image']