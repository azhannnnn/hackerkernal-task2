# library/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', author_list, name='author-list'),
    path('authors/add/', author_create, name='author-add'),
    path('books/', book_list, name='book-list'),
    path('books/add/', book_create, name='book-add'),
    path('borrowrecords/', borrowrecord_list, name='borrowrecord-list'),
    path('borrowrecords/add/', borrowrecord_create, name='borrowrecord-add'),
    path('export/excel/', export_to_excel, name='export-to-excel'),
]