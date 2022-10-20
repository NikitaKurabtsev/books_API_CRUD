from django.urls import path

from books.views import (ApiRoot, AuthorListCreateApiView, BookDetailApiView,
                         BookListCreateApiView)

urlpatterns = [
    path('authors/', AuthorListCreateApiView.as_view(), name='authors'),
    path('books/', BookListCreateApiView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailApiView.as_view(), name='books-detail'),
    path('', ApiRoot.as_view()),
]
