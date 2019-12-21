from django.contrib import admin
from .models import Post, Blog, Comment

admin.site.register([Post, Blog, Comment])