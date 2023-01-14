from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    CLASSIC = 'Classic'
    DRAMA = 'Drama'
    HISTORY = 'History'
    BIOGRAPHY = 'Biography'
    TYPE_OF_CHOICES = (
        (CLASSIC, 'Classic'),
        (DRAMA, 'Drama'),
        (HISTORY, 'History'),
        (BIOGRAPHY, 'Biography')
    )
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=TYPE_OF_CHOICES, 
                                blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                                       related_name='books')
    release_date = models.DateField()
    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def clean(self):
        if str(self.release_date) > datetime.now().strftime('%Y-%m-%d'):
            raise ValidationError(
                {'error': 'Release date cannot be bigger then today'})