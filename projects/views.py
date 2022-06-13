from django.shortcuts import render
from .models import Project

def search_post(request):
    query = request.GET.get('query')
    if query != None:
        projects = Project.objects.filter(title__contains=query)

    context = {
        'projects': projects,
        'title':'search posts'
    }

    return render(request, 'projects/search.html', context)

def home(request):
    return render(request, 'projects/home.html')

def detail(request,pk):
    return render(request, 'projects/detail.html')
