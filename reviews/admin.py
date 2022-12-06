from django.contrib import admin
from .models import Book, Review, Email

#a

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Email)