from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from books.models import Author, Book
from books.selectors import BookSelector, AuthorSelector
from books.services import BookService, AuthorService, test_create_author


class AuthorListCreateApiView(APIView):
    """
    List all authors or create a new one.

    *only authenticate users are able to create authors.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        books_count = serializers.IntegerField(read_only=True)

        class Meta:
            model = Author
            fields = ('name', 'books_count')

    # @method_decorator(cache_page(60*60*2))
    def get(self, request):
        """
        Return a collection authors.
        """
        authors = AuthorSelector.get_authors()
        serializer = self.OutputSerializer(authors, many=True)
        
        return Response(serializer.data)        

    def post(self, request):
        """
        Create a Author model object.
        """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthorService.create_author(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookListCreateApiView(APIView):
    """
    List all books or create a new one.

    *only authenticate users are able to create books.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        category = serializers.CharField()
        release_date = serializers.DateField()
        is_read = serializers.BooleanField(default=False)
        author = serializers.CharField()

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

    # @method_decorator(cache_page(60*60*2))
    def get(self, request):
        """
        Return a collection of books.
        """
        books = BookSelector.get_books() # services.py -> Books.objects.all()
        serializer = self.OutputSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        Create a Book model object.
        """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        BookService.create_book(**serializer.validated_data) # serializer.save() / validated_data -> OrderedDict

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailApiView(APIView):
    """
    Retrieve, update or delete book.

    *only authenticate users are able to edit a book.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        category = serializers.CharField()
        release_date = serializers.DateField()
        is_read = serializers.BooleanField(default=False)
        author = serializers.CharField()

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
        """
        Return a Book model object detail.
        """
        book = BookSelector.get_book(id=pk) # services.py -> Books.objects.get(pk=pk)
        serializer = self.OutputSerializer(book)

        return Response(serializer.data)

    def put(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        BookService.update_book(id=pk, **serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """
        Delete a Book model object.
        """
        BookService.delete_book(id=pk)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ApiRoot(generics.GenericAPIView):
    name = 'Api Root'

    def get(self, request, *args, **kwarkgs):

        return Response(
            {
                'Lists': {
                    'books': reverse('books', request=request),
                    'authors': reverse('authors', request=request)
                }
            }
        )


# class AuthorCreateApi(APIView):
#     """
#     Create a Author model object.

#     *only authenticate users are able to acess this view.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     class InputSerializer(serializers.Serializer):
#         name = serializers.CharField()

#     def post(self, request):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         create_author(**serializer.validated_data)

#         return Response(status=status.HTTP_201_CREATED)


# class AuthorListApi(APIView):
#     """
#     View to list all authors.

#     *only authenticate users are able to acess this view.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     class OutputSerializer(serializers.ModelSerializer):
#         books_count = serializers.IntegerField(read_only=True)

#         class Meta:
#             model = Author
#             fields = ('name', 'books_count')

#     def get(self, request):
#         """
#         Return all authors and count all books that author own.
#         """
#         books = get_authors_books_count() #Author.objects.annotate(books_count=Count('books'))

#         serializer = self.OutputSerializer(books, many=True)

#         return Response(serializer.data)


# class BookCreateApi(APIView):
#     """
#     View to create books.

#     *only authenticate users are able to acess this view.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     class InputSerializer(serializers.Serializer):
#         name = serializers.CharField()
#         category = serializers.CharField()
#         release_date = serializers.DateField()
#         is_read = serializers.BooleanField(default=False)
#         author = serializers.CharField()

#     def post(self, request):
#         """
#         Create a Book model object.
#         """
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         create_book(**serializer.validated_data) # serializer.save() / validated_data -> OrderedDict

#         return Response(status=status.HTTP_201_CREATED)


# class BookUpdateApi(APIView):
#     """
#     View to update books.

#     *only authenticate users are able to acess this view.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     class InputSerializer(serializers.Serializer):
#         name = serializers.CharField()
#         category = serializers.CharField()
#         release_date = serializers.DateField()
#         is_read = serializers.BooleanField(default=False)
#         author = serializers.CharField()

#     def post(self, request, pk):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         update_book(id=pk, **serializer.validated_data)

#         return Response(status=status.HTTP_200_OK)


# class BookListApi(APIView):
#     """
#     View to list all books.

#     *only authenticate users are able to acess this view.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     class OutputSerializer(serializers.ModelSerializer):
#         author = serializers.StringRelatedField()

#         class Meta:
#             model = Book
#             fields = (
#                 'pk', 
#                 'name', 
#                 'category', 
#                 'release_date', 
#                 'is_read', 
#                 'author'
#             )

#     def get(self, request):
#         """
#         Return a list of all books.
#         """
#         books = get_books() # services.py -> Books.objects.all()

#         serializer = self.OutputSerializer(books, many=True)

#         return Response(serializer.data)


# class BookDetailApi(APIView):
#     """
#     View to detail book.

#     *only authenticate users are able to acess this view.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     class OutputSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Book
#             fields = (
#                 'pk', 
#                 'name', 
#                 'category', 
#                 'release_date', 
#                 'is_read', 
#                 'author'
#             )

#     def get(self, request, pk):
#         """
#         Return a Book model object detail.
#         """
#         book = get_book(id=pk) # services.py -> Books.objects.get(pk=pk)

#         serializer = self.OutputSerializer(book)

#         return Response(serializer.data)


# class BookDeleteApi(APIView):
#     """
#     View to delete book.

#     *only authenticate users are able to acess this view.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     def delete(self, request, pk):
#         """
#         Delete a Book model object.
#         """
#         delete_book(id=pk)

#         return Response(status=status.HTTP_204_NO_CONTENT)
