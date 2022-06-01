from django.urls import path

from books.views import (ApiRoot, AuthorListApiView, BookDetailApiView,
                         BookListApiView)

urlpatterns = [
    path('authors/', AuthorListApiView.as_view(), name='authors'),
    path('books/', BookListApiView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailApiView.as_view(), name='books-detail'),
    path('', ApiRoot.as_view()),
]
