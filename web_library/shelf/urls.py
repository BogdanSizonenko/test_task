from django.urls import path
from shelf import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/books', views.BookViewSet, 'books')
router.register('api/authors', views.AuthorViewSet, 'authors')


urlpatterns = router.urls