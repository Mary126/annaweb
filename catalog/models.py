from django.db import models


def directory_path(instance, filename):
    return 'images/{0}'.format(instance.title, )


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=200, unique=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='pictures')
    description = models.TextField(max_length=2000, blank=True)
    view_count = models.IntegerField(default=0)
    upload_date = models.DateField()
    image = models.ImageField(upload_to='images/', verbose_name='image')

    def __str__(self):
        return self.title