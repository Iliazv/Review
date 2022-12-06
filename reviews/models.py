from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#a

class Book(models.Model):
    book_name = models.CharField(max_length = 100, default = '')
    book_description = models.TextField(max_length = 2000, default = '')
    author_name = models.CharField(max_length = 200, default = '')
    link = models.CharField(max_length = 2083 , default = '')
    image = models.ImageField(upload_to = 'site_images/', blank = True)
    rank = models.CharField(max_length=100, default = '0')
    CATEGORY_CHOICES = (
            ('COMMON', 'Common'),
            ('MODERN', 'Modern'),
            ('POPULAR', 'Popular'),
            )
    type = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='COMMON')

    def __str__(self):
        return self.book_name

        
class Review(models.Model):
    connect_model = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    name_author = models.CharField(max_length = 50)
    name_review = models.CharField(max_length = 75, default = '')
    comment_text = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField('Date published')
    mark = models.IntegerField(default=0)
    liked = models.ManyToManyField(User, related_name='liked_posts')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.name_review
    
    def new_comment(self):
        return self.date + datetime.timedelta(days = 7) > timezone.now() and self.date < timezone.now()

class Email(models.Model):
    email = models.EmailField(max_length=100)
   
    def __str__(self):
        return self.email
    
#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    liked = models.ManyToManyField()