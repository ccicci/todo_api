from django.contrib import admin
from todos.models import Todo, Comment

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo_id', 'title', 'is_completed', 'created_at', 'updated_at']
    list_display_links = ['todo_id', 'title']
    list_per_page = 10
    list_filter = ['is_completed', 'created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'contents', 'created_at', 'updated_at', 'todo_id']
    list_display_links = ['comment_id', 'contents']
    list_per_page = 10
    list_filter = ['todo_id', 'created_at']
