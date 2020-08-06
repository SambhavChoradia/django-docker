from rest_framework import serializers
from book.models import BookModel


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookModel
        fields = ('__all__')
