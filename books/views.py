from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book

# Create your views here.
class BooksListView(ListView):
    template_name = 'books/list.html'
    model = Book
    page_title = 'List Books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_list'] = 'active'
        context['page_title'] = self.page_title
        return context

class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    page_title = 'Detail Book'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_detail'] = 'active'
        context['page_title'] = self.page_title
        return context

class DeleteBookTemplateView(TemplateView):
    template_name = 'books/delete.html'
    page_title = 'Delete Book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_delete'] = 'active'
        context['page_title'] = self.page_title
        return context

class CreateBookTemplateView(TemplateView):
    template_name =  'books/create.html'
    page_title = 'Create Book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_create'] = 'active'
        context['page_title'] = self.page_title
        return context  