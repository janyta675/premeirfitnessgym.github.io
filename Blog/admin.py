from django.contrib import admin
from .models import Author,Tag,Blog

class BlogAdmin(admin.ModelAdmin):
    list_filter=("title","author","date","tags")
    list_display=("title","date","author")
    prepopulated_fields={"slug":("title",)}
    
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("firstname", "email")
    list_display=("firstname","lastname","email")


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)