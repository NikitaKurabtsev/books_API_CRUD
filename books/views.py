from django.db.models import Count
from rest_framework import permissions, serializers, status, generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book, Author
from books.selectors import get_book, get_books, get_authors_books_count
from books.services import create_book, create_author, delete_book, update_book


"""
CRUD operations with implementation
of services and selectors layers.
"""


class AuthorCreateApi(APIView):
    """
    Create a Author model object.

    *only admin users are able to acess this view.
    """
    permission_classes = [permissions.IsAdminUser]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_author(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class AuthorListApi(APIView):
    """
    View to list all authors.

    *only admin users are able to acess this view.
    """
    permission_classes = [permissions.IsAdminUser]

    class OutputSerializer(serializers.ModelSerializer):
        books_count = serializers.IntegerField(read_only=True)

        class Meta:
            model = Author
            fields = ('name', 'books_count')

    def get(self, request):
        """
        Return all authors and count all books that author own.
        """
        books = get_authors_books_count() #Author.objects.annotate(books_count=Count('books'))

        serializer = self.OutputSerializer(books, many=True)

        return Response(serializer.data)


class BookCreateApi(APIView):
    """
    View to create books.

    *only admin users are able to acess this view.
    """
    permission_classes = [permissions.IsAdminUser]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        category = serializers.CharField()
        release_date = serializers.DateField()
        is_read = serializers.BooleanField(default=False)
        author = serializers.CharField()

    def post(self, request):
        """
        Create a Book model object.
        """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_book(**serializer.validated_data) # serializer.save() / validated_data -> OrderedDict

        return Response(status=status.HTTP_201_CREATED)


class BookUpdateApi(APIView):
    """
    View to update books.

    *only admin users are able to acess this view.
    """
    permission_classes = [permissions.IsAdminUser]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        category = serializers.CharField()
        release_date = serializers.DateField()
        is_read = serializers.BooleanField(default=False)
        author = serializers.CharField()

    def post(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        update_book(id=pk, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


class BookListApi(APIView):
    """
    View to list all books.

    *only admin users are able to acess this view.
    """
    permission_classes = [permissions.IsAdminUser]

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
        """
        Return a list of all books.
        """
        books = get_books() # services.py -> Books.objects.all()

        serializer = self.OutputSerializer(books, many=True)

        return Response(serializer.data)


class BookDetailApi(APIView):
    """
    View to detail book.

    *only admin users are able to acess this view.
    """
    permission_classes = [permissions.IsAdminUser]

    class OutputSerializer(serializers.ModelSerializer):
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
        """
        Return a Book model object detail.
        """
        book = get_book(id=pk) # services.py -> Books.objects.get(pk=pk)

        serializer = self.OutputSerializer(book)

        return Response(serializer.data)


class BookDeleteApi(APIView):
    """
    View to delete book.

    *only admin users are able to acess this view.
    """
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, pk):
        """
        Delete a Book model object.
        """
        delete_book(id=pk)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ApiRoot(generics.GenericAPIView):
    name = 'Api Root'

    def get(self, request, *args, **kwarkgs):

        return Response(
            {
                'Lists': {
                    'books': reverse('books-list', request=request),
                    'authors': reverse('authors-list', request=request)
                }
            }
        )
