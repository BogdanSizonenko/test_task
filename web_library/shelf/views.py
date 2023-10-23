
from rest_framework import viewsets, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookSerializer
    paginate_by = 5
    
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer
    paginate_by = 5
