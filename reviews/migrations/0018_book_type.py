# Generated by Django 4.0.1 on 2022-09-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_remove_book_rating_remove_book_votes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.CharField(choices=[('COMMON', 'Common'), ('MODERN', 'Modern'), ('POPULAR', 'Popular')], default='COMMON', max_length=100),
        ),
    ]