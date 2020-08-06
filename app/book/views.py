from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from book.serializers import BookSerializer
from book.models import BookModel


class BookView(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response('created', status=status.HTTP_201_CREATED)

    def get(self, request):
        book = BookModel.objects.all()
        serializer = self.serializer_class(book, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('no content', status=status.HTTP_204_NO_CONTENT)
