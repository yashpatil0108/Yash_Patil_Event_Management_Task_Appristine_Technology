from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EventViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
