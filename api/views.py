from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from api.serializers import TaskSerializer
from api.models import Task

# Create your views here.

@extend_schema_view(
    list=extend_schema(description='list tasks'),
    retrive=extend_schema(description='list for id task'),
    create=extend_schema(description='create task'),
    update=extend_schema(description='update a task'),
    destroy=extend_schema(description='delete a task'))

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()