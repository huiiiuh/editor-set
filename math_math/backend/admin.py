from django.contrib import admin
from .models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display       = ("id", "title", "content_ueditor", "content_ckeditor")
    list_display_links = ("id", "title", "content_ueditor", "content_ckeditor")
    search_fields      = ("id", "title", "content_ueditor", "content_ckeditor")


admin.site.register(Blog, BlogAdmin)
