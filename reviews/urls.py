from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .views import HomePageView
from reviews.views import CreateView
from . import views

urlpatterns = [
    path('', views.main_page, name = 'main_page'),
    path('registered/', views.main_page, name = 'main_page'),
    path('modern_page/', views.modern_page, name = 'modern_page'),
    path('popular_page/', views.popular_page, name = 'popular_page'),
    path('login/', auth_views.LoginView.as_view(template_name = 'reviews/login.html'), name = 'login'),
    path('register/', views.register, name = 'register'),

    path('main_page/<str:signal>', views.main_page_with_signal, name = 'main_page'),
    path('content_book/<int:book_id>', views.content_book, name='content_book'),
    path('content_book/<int:book_id>/<current_user>', views.content_book, name='content_book'),
    path('example', views.example, name = 'example'),
    path('searched_books/', views.show_searched, name = 'show_searched'),
    path('home/', views.home, name = 'home'),
    path('auth_page/', views.auth_page, name = 'auth_page'),
    path('logout_view/', views.logout_view, name = 'logout_view'),
    path('add_review/<int:arg>/', views.add_review, name = 'add_review'),
    #path('add_review/<int:arg>/', views.AddPost.as_view(), name = 'add_review'),
    path('create_review/<int:arg>', views.create_review, name = 'create_review'),
    path('like_score/<int:arg1>/<int:arg2>', views.like_score, name = 'like_score'),
    path('dislike_score/<int:arg>', views.dislike_score, name = 'dislike_score'),
    path('', HomePageView.as_view(), name='content'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)