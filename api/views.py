from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Project List':'/project-list/',
        'Detail View': '/project-detail/<str:pk>/',
        'Create': '/project-create/',
        'Update': '/project-update/<str:pk>/',
        'Delete': '/project-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projectDetail(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def projectCreate(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('data saved')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def projectUpdate(request, pk):
    task = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def projectDelete(request, pk):
    task = Project.objects.get(id=pk)
    task.delete()
    return Response("Item successfully deleted!")