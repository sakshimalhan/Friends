# Generated by Django 3.0.7 on 2020-06-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
