from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from .models import Picture, Gallery
from .forms import PictureForm, GalleryForm


def index_view(request):
    recent_pictures = Picture.objects.all().order_by('-upload_date')[:2]
    # popular_pictures = Picture.objects.all().order_by('-view_count')[:3]
    return render(
        request,
        'index.html',
        context={'recent_pictures': recent_pictures, 'page_title': 'Welcome',
                 'title_cover_image_url': '/static/images/home-page.jpg', 'page_description': 'Something home page'},
    )


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
        context['page_title'] = 'Galleries'
        context['page_description'] = 'Something galleries'
        return context


def about_view(request):
    return render(
        request,
        'about.html',
        context={'page_title': 'About me', 'page_description': 'This is who I am.'}
    )


def gallery_view(request, name):
    gallery = get_object_or_404(Gallery, name=name)
    return render(
        request,
        'gallery_pictures.html',
        context={'gallery': gallery, 'page_title': gallery.name, 'page_description': gallery.description, 'title_cover_image_url': gallery.pictures.all()[0].image.url,},
    )


def picture_view(request, num):
    if request.method == "GET":
        view_count = get_object_or_404(Picture, pk=num).view_count + 1
        Picture.objects.filter(pk=num).update(view_count=view_count)
        picture = get_object_or_404(Picture, pk=num)
        return JsonResponse({'title':picture.title, 'description': picture.description, 'url': picture.image.url,
                             'upload_date': picture.upload_date, 'view_count': picture.view_count})


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


