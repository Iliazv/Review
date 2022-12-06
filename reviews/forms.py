from django import forms
from .models import *
from .models import Book, Review
from ckeditor.fields import RichTextField

    
    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('image',)
        
class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_review'].label = 'Заголовок рецензии'
        self.fields['comment_text'].label = 'Текст рецензии'
    
    class Meta:
        model = Review
        fields = ('name_review', 'comment_text')
        
        
        widgets = {
            'name_review': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'comment_text': forms.Textarea(attrs={'class': 'myfieldclass'}),
        }