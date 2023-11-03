from django.views.generic.list import ListView
from django.views.generic import DetailView

from apps.author.models import Author


class AuthorListView(ListView):
    model = Author
    template_name = "list.html"
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "detail.html"
    context_object_name = "author"
