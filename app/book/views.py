from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import BookModel


class BookView(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Created', status=status.HTTP_201_CREATED)
        return Response('Internal Server Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        book = BookModel.objects.all()
        serializer = self.serializer_class(book, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No Content', status=status.HTTP_204_NO_CONTENT)
