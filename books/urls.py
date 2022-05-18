from django.urls import path

from books.views import AuthorListApi, BookListApi, BookDetailApi, ApiRoot

urlpatterns = [
    path('authors/', AuthorListApi.as_view(), name='authors'),
    path('books/', BookListApi.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailApi.as_view()),
    path('', ApiRoot.as_view()),
]
