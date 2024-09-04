from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Event, Comment, Category
from .serializers import EventSerializer, CommentSerializer, CategorySerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD + List operations for Event model.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD + List operations for Comment model.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD + List operations for Category model.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
