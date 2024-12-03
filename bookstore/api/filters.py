# api/filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']  # Fields to filter by
