from django.urls import path

from books.views import (AuthorCreateApi, AuthorListApi, BookCreateApi, BookDeleteApi,
                          BookDetailApi, BookListApi, BookUpdateApi, ApiRoot, AuthorListCreateApi)

urlpatterns = [
    path('authors-create/', AuthorCreateApi.as_view()),
    path('authors-list/', AuthorListApi.as_view(), name='authors-list'),
    path('books-create/', BookCreateApi.as_view()),
    path('books-list/', BookListApi.as_view(), name='books-list'),
    path('books-detail/<int:pk>/', BookDetailApi.as_view()),
    path('books-delete/<int:pk>/', BookDeleteApi.as_view()),
    path('books-update/<int:pk>/', BookUpdateApi.as_view()),
    path('', ApiRoot.as_view()),
    path('authors', AuthorListCreateApi.as_view())
]
