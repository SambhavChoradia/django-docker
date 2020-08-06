from django.db import models


class BookModel(models.Model):
    book = models.CharField(max_length=20)
