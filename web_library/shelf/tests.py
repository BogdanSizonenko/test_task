import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Book, Author
from django.test.client import encode_multipart

@pytest.fixture
def setUp():
    client = APIClient()
    return client

#Тест Post, Get запросов 
@pytest.mark.django_db
def test_create_book(client):
    data = {
        'title' : 'Евгений Онегин'
    }
    response = client.post('/api/books/', data)
    assert response.status_code == 201
    assert Book.objects.count() == 1
    assert Book.objects.first().title == 'евгений онегин'
    response = client.get('/api/books/')
    assert response.status_code == 200

# Тест Put, Delete запросов
@pytest.mark.django_db
def test_delete_book(client):
    book = Book.objects.create(title='евгений онегин')
    data_1 = {
        'title' : 'Война и Мир',
    }
    data_1 = encode_multipart('BoUnDaRyStRiNg', data_1)
    content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    response = client.put(reverse('books-detail', kwargs={'pk':book.id}), data_1, content_type=content_type)
    book.refresh_from_db()
    assert response.status_code == 200
    assert book.title == 'война и мир'
    response = client.delete(reverse('books-detail', kwargs={'pk':book.id}))
    assert response.status_code == 204
    assert not Book.objects.filter(title='война и мир').exists()
    
#Тест Post, Get запросов    
@pytest.mark.django_db
def test_create_author(client):
    data = {
        'name' : 'Александр Пушкин'
    }
    response = client.post('/api/authors/', data)
    assert response.status_code == 201
    assert Author.objects.count() == 1
    assert Author.objects.first().name == 'александр пушкин'
    response = client.get('/api/authors/')
    assert response.status_code == 200
# Тест Put, Delete запросов
@pytest.mark.django_db
def test_delete_author(client):
    author = Author.objects.create(name='александр пушкин')
    data_1 = {
        'name' : 'лев толстой',
    }
    data_1 = encode_multipart('BoUnDaRyStRiNg', data_1)
    content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    response = client.put(reverse('authors-detail', kwargs={'pk':author.id}), data_1, content_type=content_type)
    author.refresh_from_db()
    assert response.status_code == 200
    assert author.name == 'лев толстой'
    response = client.delete(reverse('authors-detail', kwargs={'pk':author.id}))
    assert response.status_code == 204
    assert not Author.objects.filter(name='лев толстой').exists()