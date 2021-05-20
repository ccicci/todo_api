# Generated by Django 3.2.3 on 2021-05-20 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='번호')),
                ('title', models.CharField(max_length=126, verbose_name='제목')),
                ('description', models.TextField(verbose_name='내용')),
                ('is_completed', models.BooleanField(default=False, verbose_name='완료여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='번호')),
                ('contents', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
                ('todo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.todo')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]