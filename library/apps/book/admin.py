from django.contrib import admin

from apps.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
