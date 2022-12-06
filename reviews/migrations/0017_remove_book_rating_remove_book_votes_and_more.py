# Generated by Django 4.0.1 on 2022-09-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0016_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='book',
            name='votes',
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.CharField(default='', max_length=2083),
        ),
    ]