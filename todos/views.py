from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import TodoSerializer, CommentSerializer
from .models import Todo, Comment
from rest_framework import status
from django.shortcuts import render

# Todo
class TodoView(APIView):
    def get(self, request,  **kwargs):
            if kwargs.get('todo_id') is None:
                todo_queryset = Todo.objects.all()
                todo_queryset_serializer = TodoSerializer(todo_queryset, many=True)
                return Response(todo_queryset_serializer.data, status=status.HTTP_200_OK)
            else:
                todo_id = kwargs.get('todo_id')
                todo_serializer = TodoSerializer(Todo.objects.get(todo_id=todo_id))
                return Response(todo_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        todo_serializer = TodoSerializer(data=request.data)
 
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        if kwargs.get('todo_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            todo_id = kwargs.get('todo_id')
            todo_object = Todo.objects.get(todo_id=todo_id)
 
            update_todo_serializer = TodoSerializer(todo_object, data=request.data)

            if update_todo_serializer.is_valid():
                update_todo_serializer.save()
                return Response(update_todo_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, **kwargs):
        if kwargs.get('todo_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            todo_id = kwargs.get('todo_id')
            todo_object = Todo.objects.get(todo_id=todo_id)
            todo_object.delete()
            return Response("delete completed", status=status.HTTP_200_OK)
 


# Comment
class CommentView(APIView):
    def get(self, request, **kwargs):
            if kwargs.get('todo_id') is None:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
            else:
                comment_queryset = Comment.objects.filter(todo_id=kwargs.get('todo_id'))
                comment_queryset_serializer = CommentSerializer(comment_queryset, many=True)
                return Response(comment_queryset_serializer.data, status=status.HTTP_200_OK)


    def post(self, request, **kwargs):
        comment_serializer = CommentSerializer(data=request.data)
 
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, **kwargs):
        if kwargs.get('comment_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            comment_id = kwargs.get('comment_id')
            comment_object = Comment.objects.get(comment_id=comment_id)

            update_comment_serializer = CommentSerializer(comment_object, data=request.data)

            if update_comment_serializer.is_valid():
                update_comment_serializer.save()
                return Response(update_comment_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('comment_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            comment_id = kwargs.get('comment_id')
            comment_object = Comment.objects.get(comment_id=comment_id)
            comment_object.delete()
            return Response("delete completed", status=status.HTTP_200_OK)