from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions, serializers, status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from books.models import Author, Book
from books.selectors import AuthorSelector, BookSelector
from books.services import AuthorService, BookService


class AuthorCreateApi(LoginRequiredMixin, APIView):
    throttle_classes = [UserRateThrottle]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthorService.create_author(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthorListApi(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    class OutputSerializer(serializers.ModelSerializer):
        books_count = serializers.IntegerField(read_only=True)

        class Meta:
            model = Author
            fields = ('pk', 'name', 'books_count')

    def get(self, request):
        authors = AuthorSelector.get_authors()
        serializer = self.OutputSerializer(authors, many=True)
        
        return Response(serializer.data)


class BookCreateApi(LoginRequiredMixin, APIView):
    throttle_classes = [UserRateThrottle]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        category = serializers.CharField()
        release_date = serializers.DateField()
        is_read = serializers.BooleanField(default=False)
        author = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        BookService.create_book(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookListApi(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    class OutputSerializer(serializers.ModelSerializer):
        author = serializers.StringRelatedField()

        class Meta:
            model = Book
            fields = (
                'pk',
                'name',
                'category',
                'release_date',
                'is_read',
                'author'
            )

    def get(self, request):
        books = BookSelector.get_books()
        serializer = self.OutputSerializer(books, many=True)

        return Response(serializer.data)


class BookDetailApi(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class OutputSerializer(serializers.ModelSerializer):
        author = serializers.StringRelatedField()

        class Meta:
            model = Book
            fields = (
                'pk', 
                'name', 
                'category', 
                'release_date', 
                'is_read', 
                'author'
            )

    def get(self, request, pk):
        book = BookSelector.get_book(id=pk)
        serializer = self.OutputSerializer(book)

        return Response(serializer.data)


class BookUpdateApi(LoginRequiredMixin, APIView):
    throttle_classes = [UserRateThrottle]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        category = serializers.CharField()
        release_date = serializers.DateField()
        is_read = serializers.BooleanField(default=False)
        author = serializers.CharField()

    def put(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        BookService.update_book(id=pk, **serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDeleteApi(LoginRequiredMixin, APIView):
    def delete(self, request, pk):
        BookService.delete_book(id=pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
