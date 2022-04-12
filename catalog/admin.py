from django.contrib import admin
from .models import Gallery, Picture

admin.site.register(Gallery)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',
                    'view_count', 'upload_date')
