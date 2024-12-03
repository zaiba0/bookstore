from django.contrib import admin
from .models import Book, Review, Profile



# Register your models
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Profile)
