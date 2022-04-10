from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Picture, Gallery


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
    queryset = Gallery.objects.exclude(name='HomePage')
    context_object_name = 'galleries_list'
    template_name = 'galleries.html'

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
        context={'gallery':gallery, 'header_title': gallery.name,},
    )


