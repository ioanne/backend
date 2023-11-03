from django.contrib import admin

from apps.category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
