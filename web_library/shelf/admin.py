from django.contrib import admin
from django.contrib import admin
from .models import Author, Book


 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'books')
    list_display_links = ('id', 'name', 'books')
    search_fields = ('id', 'name', 'books')
    

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title', 'authors')
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "authors":
            kwargs["queryset"] = Author.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    

admin.site.register(Book, BookAdmin)
