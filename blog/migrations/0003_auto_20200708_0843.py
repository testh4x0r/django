# Generated by Django 3.0.7 on 2020-07-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='blog_images'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
