from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(
        "author.Author", on_delete=models.CASCADE, related_name="books"
    )
    collection = models.ForeignKey("collection.Collection", on_delete=models.CASCADE)
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
