from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class BooksListView(ListView):
    template_name = 'books/list.html'
    model = Book
    page_title = 'List Books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_list'] = 'active'
        context['page_title'] = self.page_title
        context['count'] = Book.objects.count()
        return context

class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    page_title = 'Book Detail'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_detail'] = 'active'
        context['page_title'] = self.page_title
        return context

class DeleteBookView(PermissionRequiredMixin, DeleteView):
    permission_required = 'books.delete_book'
    template_name = 'books/delete.html'
    page_title = 'Delete Book'
    model = Book
    success_url = '/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_delete'] = 'active'
        context['page_title'] = self.page_title
        return context

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'books.change_book'
    template_name =  'books/create.html'
    page_title = 'Edit Book'
    model = Book
    fields = (
        'title',
        'author',
        'publishing_year',
        'publishing_house',
        'pages',
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_create'] = 'active'
        context['page_title'] = self.page_title
        context['book_pk'] = self.get_form().instance.id
        return context

class CreateViewBook(LoginRequiredMixin, CreateView):
    login_url = '/account/login'
    redirect_field_name = '/books/list/'

    template_name =  'books/create.html'
    page_title = 'Create Book'
    model = Book
    fields = (
        'title',
        'author',
        'publishing_year',
        'publishing_house',
        'pages',
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_text_create'] = 'active'
        context['page_title'] = self.page_title
        return context

