# Generated by Django 4.0.1 on 2022-04-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_book_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, upload_to='site_images/'),
        ),
    ]