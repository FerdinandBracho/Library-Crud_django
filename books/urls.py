from django.urls import path
from .views import (
    CreateViewBook, 
    BooksListView, 
    DeleteBookView, 
    BookDetailView,
    BookUpdateView)

app_name = 'books'

urlpatterns = [
    path('', BooksListView.as_view(), name='list'),
    path('list/', BooksListView.as_view(), name='list'),
    path('create/', CreateViewBook.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteBookView.as_view(), name='delete'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='update'),
]