from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)  
    nationality = models.CharField(max_length=100, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'author_image', null=True, blank = True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True, blank=True)
    publish_date = models.DateField(null=True, blank=True) 
    summary = models.TextField(null=True, blank=True)  
    page_count = models.PositiveIntegerField(null=True, blank=True)  
    language = models.CharField(max_length=50, default="English")
    available = models.BooleanField(default=True)  
