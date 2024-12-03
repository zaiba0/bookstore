from rest_framework import viewsets, permissions
from .models import Book, Review, UserProfile
from .serializers import BookSerializer, ReviewSerializer, UserProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404
from .models import Book
from .filters import BookFilter
from django.shortcuts import render
from .models import Profile


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})


def profile_view(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    return render(request, 'api/profile.html', {'profile': profile})




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'author']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

def book_list(request):
    # Get all books and apply filter using GET parameters
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, 'books/book_list.html', {'filter': book_filter})