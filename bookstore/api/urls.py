from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet, UserProfileViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('reviews', ReviewViewSet)
router.register('profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
     path('books/', views.book_list, name='book-list'),
]
