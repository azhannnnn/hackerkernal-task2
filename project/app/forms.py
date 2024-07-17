from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']
        widgets = {
            'published_date': forms.SelectDateWidget,
        }

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']
        widgets = {
            'borrow_date': forms.SelectDateWidget,
            'return_date': forms.SelectDateWidget,
        }
