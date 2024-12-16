from django.contrib import admin
from web.models import Book,Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_of_birth', 'nationality', 'biography', 'image']  

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publish_date', 'summary', 'page_count', 'language', 'available']  

admin.site.register(Book, BookAdmin)
