from django.contrib import admin

from apps.author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
