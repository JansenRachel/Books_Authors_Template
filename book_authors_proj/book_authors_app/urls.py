from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  #home- books page
    path('create_book', views.create_book),   #adds a book to books page
    path('view_book/<int:book_id>', views.view_book), #views one books info on book_display page
    path('add_author', views.add_author),#adds an author from existing db to a book on book_display page

    path('authors', views.authors),
    path('create_author', views.create_author),
    path('view_author/<int:author_id>', views.view_author), #views one books info on book_display page
    path('add_book', views.add_book)
]
