# Generated by Django 5.0.1 on 2024-02-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_delete_courselbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_3d',
            field=models.FileField(default='', upload_to='product/3d_img'),
        ),
    ]
