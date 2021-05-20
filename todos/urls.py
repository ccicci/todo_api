from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoView.as_view()),
    path('<int:todo_id>', views.TodoView.as_view()),
    path('<int:todo_id>/comments/', views.CommentView.as_view()),
    path('<int:todo_id>/comments/<int:comment_id>', views.CommentView.as_view()),
]