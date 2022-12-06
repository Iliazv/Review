from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from reviews.models import Book, Review, Email
from django.template import loader
from django.db.models import Q
from django.urls import reverse
from .forms import PostForm
from django.views.generic import CreateView
from django.utils import timezone
from django.db.models import Count
from django.core.mail import send_mail
import locale
import datetime


def main_page(request):
    list_books = Book.objects.all()
    liked = False
    content = {'list_books': list_books, 'liked': liked}
    template = loader.get_template('reviews/main.html')
    return HttpResponse(template.render(content, request))

def main_page_with_signal(request, signal):
    list_books = Book.objects.all()
    entered_email = request.POST.get('text')
    user_email = Email(email=entered_email)
    if Email.objects.filter(email=entered_email).exists() == False:
        user_email.save()
        send_mail('Subject here', 'Here is the message.', 'ilia.zhelenkov@gmail.com',
            ['ilia.zhelenkov@gmail.com'], fail_silently=False)        
    content = {'list_books': list_books, 'signal': signal}
    template = loader.get_template('reviews/main.html')
    return HttpResponse(template.render(content, request))    

def modern_page(request):
    list_books = Book.objects.all()
    content = {'list_books': list_books}
    template = loader.get_template('reviews/modern.html')
    return HttpResponse(template.render(content, request))

def popular_page(request):
    popular_books = Book.objects.all().annotate(cnt=Count('comments')).order_by('cnt')[::-1]
    content = {'popular_books': popular_books}
    template = loader.get_template('reviews/popular.html')    
    return HttpResponse(template.render(content, request))

def show_searched(request):
    entered_text = request.POST.get('top_input')
    entered_text = entered_text.capitalize()
    searched_books = Book.objects.filter(Q(book_name__istartswith=entered_text))
    content = {'searched_books': searched_books}
    template = loader.get_template('reviews/searched.html')        
    return HttpResponse(template.render(content, request))

@login_required
def home(request):
    return render(request, 'reviews/succes.html', {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect('main_page')
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})

@login_required
def auth_page(request):
    return render(request, 'reviews/auth_page.html')

def logout_view(request):
    logout(request)  
    return redirect(reverse('main_page'))

def content_book(request, book_id, total_likes=0, current_user=''):
    model = Review
    book = Book.objects.get(id=book_id)
    review_list = book.comments.all().annotate(cnt=Count('likes')).order_by('cnt')[::-1]
    marks = []
    reviews = book.comments.all()
    for review in reviews:
        marks.append(review.mark)
    try:
        rank = sum(marks) / len(marks)
        rank = str(rank)[:3]
        if str(rank)[-1] == '0' and len(str(rank)) == 3:
            rank = int(rank)
    except:
        rank = 0
    book.rank = rank
    book.save()
    URL = book.link
    photo = book.image
    return render(request, 'reviews/book_content.html', {'book': book, 'URL': URL, 'photo': photo, 'current_user': current_user,
                                                         'review_list': review_list, 'total_likes': total_likes, 'rank': rank})

def create_review(request, arg):
    connect_model = arg
    mark = request.POST.get('rating')
    name_review = request.POST.get('name_review')
    comment = request.POST.get('comment_text')
    comment = comment.replace('<p>', '')
    comment = comment.replace('</p>', '')
    comment = comment.replace('&quot;', '"')
    if comment == '':
        return redirect(reverse('add_review', args=[arg]))
    name_author = request.user.username
    date = timezone.now()
    book = Book.objects.get(id=arg)
    if name_author == '':
        name_author = 'Гость'
    book.comments.create(name_author=name_author, name_review=name_review,
                        comment_text=comment, date=date, mark=mark)
    return redirect(reverse('content_book', args=[arg]))

# arg1 - айди книги   arg2 - айди ревью
def like_score(request, arg1, arg2):
    post = get_object_or_404(Review, id=arg2)
    current_user = type(request.user)
    a = post.likes.all()
    
    if post.likes.filter(id=request.user.id).exists():
        try:
            post.likes.remove(request.user)
        except: 
            return redirect(reverse('register'))
    else: 
        try:
            post.likes.add(request.user)
        except: 
            return redirect(reverse('register'))
    total_likes = post.total_likes()
    liked = post.liked
    return redirect(reverse('content_book', args=[arg1, current_user]))

    
def dislike_score(request, arg):
    return redirect(reverse('content_book', args=[arg]))
    
class HomePageView(ListView):
    model = Book
    template_name = 'reviews/book_content.html'


def add_review(request, arg):
    model = Review
    form = PostForm
    book = Book.objects.get(id=arg)
    return render(request, 'reviews/new_review.html', {'book': book, 'form': form, 'model': model})


def example(request):
    return HttpResponse('My site')
