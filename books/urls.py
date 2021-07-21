from django.urls import path
from .views import CreateBookTemplateView, BooksListView, DeleteBookTemplateView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('', BooksListView.as_view(), name='list'),
    path('create/',CreateBookTemplateView.as_view(), name='create'),
    path('delete/', DeleteBookTemplateView.as_view(), name='delete'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail')
]