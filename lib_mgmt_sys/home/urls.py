from django.urls import path
from  . import views 

# from .import *

urlpatterns = [
    path('',views.home, name = "home"),
    path('contact/',views.contact, name = "contact"),
    path('about/', views.about, name = "about"),
    path('add_author/', views.add_author, name = "add_author"),
    path('add_books/', views.add_books, name= "add_books"),
    path('edit_books/<int:id>/',views.edit_books, name = "edit_books"),
    path('delete_books/<int:id>/', views.delete_books, name = 'delete_books'),
    path('list_books/', views.list_books, name = 'list_books')
    ]