from django.contrib import admin
from books.models import PublishingHouse, Author, Book

# Register your models here.
@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('author',)