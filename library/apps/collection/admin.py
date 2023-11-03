from django.contrib import admin

from apps.collection.models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass
