from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from .models import Picture, Gallery
from .forms import PictureForm, GalleryForm


class IndexView(ListView):
    context_object_name = 'gallery'
    template_name = 'index.html'

    def get_queryset(self):
        self.gallery = get_object_or_404(Gallery, name='HomePage')
        return Picture.objects.filter(gallery=self.gallery)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_active'] = 'home'
        context['header_title'] = 'Home'
        return context


class GalleriesView(ListView):
    context_object_name = 'galleries_list'
    template_name = 'galleries.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Gallery.objects.all()
        else:
            return Gallery.objects.exclude(name='HomePage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_active'] = 'galleries'
        context['header_title'] = 'Galleries'
        return context


def gallery_view(request, name):
    gallery = get_object_or_404(Gallery, name=name)
    return render(
        request,
        'gallery_pictures.html',
        context={'gallery':gallery, 'header_title': gallery.name},
    )


def picture_view(request, num):
    if request.method == "GET":
        Picture.objects.filter(pk=num).update(view_count=get_object_or_404(Picture, pk=num).view_count + 1)
        picture = get_object_or_404(Picture, pk=num)
        return JsonResponse({'title':picture.title, 'description': picture.description, 'url': picture.image.url,
                             'upload-date': picture.upload_date, 'view_count':picture.view_count})


@login_required
def add_picture(request, name):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.gallery = get_object_or_404(Gallery, name=name)
            form.upload_date = timezone.now()
            form.save()
            return HttpResponseRedirect('/galleries/' + name)
    else:
        form = PictureForm()

    return render(request, 'add_picture.html', {'form': form, 'url': '/galleries/' + name + '/add-picture'})


@login_required
def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/galleries/')
    else:
        form = GalleryForm()

    return render(request, 'add_gallery.html', {'form': form})


@login_required
def delete_picture(request, name, pk):
    get_object_or_404(Picture, pk=pk).delete()
    return HttpResponseRedirect('/galleries/' + name)


@login_required
def delete_gallery(request, name):
    get_object_or_404(Gallery, name=name).delete()
    return HttpResponse(200)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class LoginUser(LoginView):
    template_name = 'login.html'


