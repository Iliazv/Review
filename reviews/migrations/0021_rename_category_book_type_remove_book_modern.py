# Generated by Django 4.0.1 on 2022-09-02 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0020_remove_book_type_book_category_book_modern'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='book',
            name='modern',
        ),
    ]
