from django.urls import path

from apps.author.views import AuthorListView, AuthorDetailView


urlpatterns = [
    path("list/", AuthorListView.as_view(), name="list"),
    path("detail/<int:pk>", AuthorDetailView.as_view(), name="detail"),
]
