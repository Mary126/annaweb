# Generated by Django 4.0.3 on 2022-04-08 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_picture_gallery_picture_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.gallery'),
        ),
    ]
