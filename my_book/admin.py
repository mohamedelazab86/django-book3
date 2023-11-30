from django.contrib import admin
from .models import Book,Author,Review


class Bookadmin(admin.ModelAdmin):
    list_display=['title','author','price']
    list_filter=['price']
    search_fields=['title']

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)

