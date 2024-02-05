from django.contrib import admin
from .models import BlogsDetail
# Register your models here.

@admin.register(BlogsDetail)
class BlogsDetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}