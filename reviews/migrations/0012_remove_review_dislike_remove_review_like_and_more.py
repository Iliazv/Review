# Generated by Django 4.0.1 on 2022-04-25 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0011_alter_review_connect_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='review',
            name='like',
        ),
        migrations.AddField(
            model_name='review',
            name='dislikes',
            field=models.ManyToManyField(related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.ManyToManyField(related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
