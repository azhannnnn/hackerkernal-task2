from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import  *
from .forms import *
import django_excel as excel

def author_list(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 10)  # Show 10 authors per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'author_list.html', {'page_obj': page_obj})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book_list.html', {'page_obj': page_obj})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def borrowrecord_list(request):
    borrowrecords = BorrowRecord.objects.all()
    paginator = Paginator(borrowrecords, 10)  # Show 10 borrow records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'borrowrecord_list.html', {'page_obj': page_obj})

def borrowrecord_create(request):
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrowrecord-list')
    else:
        form = BorrowRecordForm()
    return render(request, 'borrowrecord_form.html', {'form': form})

def export_to_excel(request):
    authors = Author.objects.all().values_list('name', 'email', 'bio')
    books = Book.objects.all().values_list('title', 'genre', 'published_date', 'author__name')
    borrow_records = BorrowRecord.objects.all().values_list('user_name', 'book__title', 'borrow_date', 'return_date')

    data = {
        "Authors": [['Name', 'Email', 'Bio']] + list(authors),
        "Books": [['Title', 'Genre', 'Published Date', 'Author']] + list(books),
        "BorrowRecords": [['User Name', 'Book Title', 'Borrow Date', 'Return Date']] + list(borrow_records),
    }

    return excel.make_response_from_book_dict(data, 'xlsx', file_name="library_data.xlsx")
