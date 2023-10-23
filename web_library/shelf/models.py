from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    authors = models.ManyToManyField('Author', related_name='books', blank=True)
    
    def save(self, **kwargs):
        self.title = self.title.lower()
        super().save()
        
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def save(self, **kwargs):
        self.name = self.name.lower()
        super().save()
    
    def __str__(self):
        return self.name



