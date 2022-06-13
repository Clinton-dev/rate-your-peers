from django.shortcuts import render,  get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Project, Rating
from users.forms import RatingForm

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

def detail(request,title):
    project = Project.objects.get(title=title)
    ratings = Rating.objects.filter(project=project)
    form = RatingForm()

    context = {
        'ratings': ratings,
        'project': project,
        'form' : form
    }

    return render(request, 'projects/detail.html', context)

class UserPictureListView(ListView):
    model= Project
    template_name='projects/user_projects.html' #<app-name>/<model>_<view-type>.html
    context_object_name='projects'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-created')
