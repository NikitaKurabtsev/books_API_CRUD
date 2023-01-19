from django.urls import path, include

from books.views import (
    AuthorCreateApi,
    AuthorListApi,
    BookCreateApi,
    BookListApi,
    BookDetailApi,
    BookUpdateApi,
    BookDeleteApi,
)


author_patterns = [
    path('', AuthorListApi.as_view(), name='list'),
    path('create/', AuthorCreateApi.as_view(), name='create'),
]

book_patterns = [
    path('', BookListApi.as_view(), name='list'),
    path('<int:pk>/', BookDetailApi.as_view(), name='detail'),
    path('create/', BookCreateApi.as_view(), name='create'),
    path('<int:pk>/update/', BookUpdateApi.as_view(), name='update'),
    path('<int:pk>/delete/', BookDeleteApi.as_view(), name='delete'),
]

urlpatterns = [
    path('authors/', include((author_patterns, 'books'), namespace='authors')),
    path('books/', include((book_patterns, 'books'), namespace='books')),
]
