from django.db import models

class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True, verbose_name='번호')
    title = models.CharField(max_length=126, null=False, verbose_name='제목')
    description = models.TextField(null=False, verbose_name='내용')
    is_completed = models.BooleanField(default=False, verbose_name='완료여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜')

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, verbose_name='번호')
    contents = models.TextField(null=False, verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

