from django.contrib import admin
from .models import Post, Project

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    list_filter = ('status', 'published')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',  'status')
    list_filter = ('status', 'published')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
    ordering = ('status', 'published')
