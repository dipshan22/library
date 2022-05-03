from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .views import *
from .forms import *
from . models import*
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

@login_required
def add_author(request):
    if request.method =="GET":
        author_add_form = AddAuthorForm()
        return render(request, "add_author.html", context={'form':author_add_form})
    elif request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        author = Author.objects.create(name = name , age = age)
        return HttpResponse('Author saved in database')
@login_required
def add_books(request):
    if request.method == "GET":
        book_add_form = BooksModelForm()
        return render(request,"add_books.html" , context={"book_forms":book_add_form})
    else:
        book_add_form = BooksModelForm(request.POST)
        if book_add_form.is_valid():
            book_add_form.save()
            return redirect(list_books)
    return render(request,'add_books.html', context={'book_forms': book_add_form})
@login_required
def edit_books(request,id):
    book = Books.objects.get(id = id)
    if request.method == "GET":
        form = BooksModelForm(instance=book)
        return render(request, "edit_books.html", context={"form":form})
    elif request.method == "POST":
        form = BooksModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(list_books)
    return render(request,"add_books.html", context={"form":form})
@login_required
def delete_books(request,id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect(list_books)

@login_required
def list_books(request):
    list_book = Books.objects.all()
    return render(request, 'list_books.html', context={'books':list_book})